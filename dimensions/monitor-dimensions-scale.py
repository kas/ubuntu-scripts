#!/usr/bin/env python3

# This script monitors the screen dimensions. When the screen dimensions change, the screen scale is updated.

from datetime import datetime
from subprocess import PIPE, Popen, check_output
import subprocess
import time

EDP_SCREEN = 'eDP-1'
HDMI_SCREEN = 'HDMI-1'
LOG = False


def log(message):
    line = f'{datetime.now()} {message}'
    print(line)
    if LOG:
        with open('monitor-dimensions-scale-log', 'a') as file:
            file.write(line + '\n')


def update_scale():
    # xrandr | grep connected | grep -v disconnected | awk '{print $1}'
    # xrandr --output screen-name --scale 1x1
    # eDP-1
    # HDMI-1

    xrandr = Popen('xrandr', stdout=PIPE)
    connected = Popen(['grep', 'connected'], stdin=xrandr.stdout, stdout=PIPE)
    disconnected = Popen(['grep', '-v', 'disconnected'],
                         stdin=connected.stdout, stdout=PIPE)
    displays = check_output(
        ['awk', '{print $1}'], stdin=disconnected.stdout).decode()
    popen.wait()

    log('Displays: ' + displays)

    scale = None
    screen_name = None
    if HDMI_SCREEN in displays:
        scale = '1.25'
        screen_name = HDMI_SCREEN
    else:
        scale = '1'
        screen_name = EDP_SCREEN

    log(f'screen_name: {screen_name}, scale: {scale}')

    Popen(['xrandr', '--output', screen_name, '--scale',
          f'{scale}x{scale}'], stderr=subprocess.STDOUT, stdout=subprocess.DEVNULL)


log('Started')

previous_dimensions = None

while True:
    is_lockscreen_active = check_output(['qdbus', 'org.freedesktop.ScreenSaver', '/org/freedesktop/ScreenSaver',
                                        'org.freedesktop.ScreenSaver.GetActive']).decode().strip() == 'true'

    log('is_lockscreen_active: ' + is_lockscreen_active)

    if is_lockscreen_active:
        pass
    else:
        popen = Popen('xdpyinfo', stdout=PIPE)
        dimensions = check_output(
            ['grep', 'dimensions'], stdin=popen.stdout)
        popen.wait()

        if previous_dimensions != dimensions:
            log('Updating scale')
            update_scale()
            previous_dimensions = dimensions

    time.sleep(5)
