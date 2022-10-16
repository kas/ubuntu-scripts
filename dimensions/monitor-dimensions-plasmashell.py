#!/usr/bin/env python3

# This script monitors the screen dimensions. When the screen dimensions change, plasmashell is restarted.

from datetime import datetime
from subprocess import Popen
import subprocess
import time

LOG = False


def log(message):
    line = f'{datetime.now()} {message}'
    print(line)
    if LOG:
        with open('monitor-dimensions-plasmashell-log', 'a') as file:
            file.write(line + '\n')


log('Started')

previous_dimensions = None

while True:
    popen = Popen('xdpyinfo', stdout=subprocess.PIPE)
    dimensions = subprocess.check_output(
        ['grep', 'dimensions'], stdin=popen.stdout)
    popen.wait()

    if previous_dimensions is None:
        previous_dimensions = dimensions
    elif previous_dimensions != dimensions:
        log('Replacing plasmashell')
        Popen(['plasmashell', '--replace'],
              stderr=subprocess.STDOUT, stdout=subprocess.DEVNULL)
        previous_dimensions = dimensions

    time.sleep(5)
