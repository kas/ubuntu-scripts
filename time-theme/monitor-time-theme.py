#!/usr/bin/env python3

# This script monitors the time. The global theme is set when the program starts. When the next sunrise or sunset happens, the global theme is updated.

from datetime import datetime
import argparse
import subprocess
import sys
import time

from log import Log
from sun import Sun

COORDINATES = {'latitude': 41.66128, 'longitude': -91.5232}
THEME_DAY = 'org.kde.breeze.desktop'
THEME_NIGHT = 'org.kde.breezedark.desktop'
UTC_HOUR_OFFSET = -5


def hour_to_current_timezone(decimal_time):
    hour = decimal_time // 1
    decimal = decimal_time - hour
    hour = hour + UTC_HOUR_OFFSET
    if hour < 0:
        hour += 24
    return hour + decimal


log = Log('monitor-time-theme-log')
log.log('Started')

parser = argparse.ArgumentParser()
parser.add_argument('-d', '--day', action='store_true')
parser.add_argument('-n', '--night', action='store_true')
args = parser.parse_args()

if args.day and args.night:
    log.log('Only pick one')
    sys.exit()

sun = Sun()

is_next_day = None
next_time = None

while True:
    sunrise_time_utc = sun.get_sunrise_time(COORDINATES)['decimal']
    sunrise_time = hour_to_current_timezone(sunrise_time_utc)
    sunset_time_utc = sun.get_sunset_time(COORDINATES)['decimal']
    sunset_time = hour_to_current_timezone(sunset_time_utc)

    now_time_utc = datetime.utcnow()
    now_time_utc = now_time_utc.hour + (now_time_utc.minute / 60)
    now_time = hour_to_current_timezone(now_time_utc)

    if is_next_day and now_time < sunrise_time:
        log.log('Setting is next day to False')
        is_next_day = False

    if next_time is None or now_time > next_time and not is_next_day:
        log.log(
            f'Next time: {next_time}, is next day: {is_next_day}, now time: {now_time}')

        theme = None
        if now_time > sunrise_time and now_time < sunset_time:
            theme = THEME_DAY
            next_time = sunset_time
            is_next_day = False
        else:
            theme = THEME_NIGHT
            next_time = sunrise_time
            is_next_day = now_time > next_time

        if args.day or args.night:
            if args.day:
                theme = THEME_DAY
            else:
                theme = THEME_NIGHT
            args.day = False
            args.night = False
            log.log('Manually setting theme: {theme}')

        log.log(
            f'Setting theme: {theme}, next time: {next_time}, is next day: {is_next_day}')

        subprocess.Popen(['lookandfeeltool', '-a', theme],
                         stderr=subprocess.STDOUT, stdout=subprocess.DEVNULL)

    time.sleep(60)
