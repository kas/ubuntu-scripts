#!/usr/bin/env python3

# This script restarts the monitor-time-theme script

from os import path
from subprocess import DEVNULL, Popen, STDOUT
import subprocess
import sys

from log import Log

log = Log('time-theme-log')
log.log('Started')

if len(sys.argv) > 2:
    log.log('Only pick one')
    sys.exit()

pid = None
try:
    pid = subprocess.check_output(
        ['pgrep', '-f', '.*python.*monitor-time-theme.py']).decode()
    pid = pid.split()[0]
    log.log('Found pid: ' + pid)
except:
    log.log('Pid not found')

if pid is not None:
    Popen(['kill', '-15', pid],
          stderr=STDOUT, stdout=DEVNULL)
    log.log('Killed pid: ' + pid)

script_path = path.join(path.dirname(
    path.realpath(__file__)), 'monitor-time-theme.py')

arguments = ['/usr/bin/python3', script_path]
if len(sys.argv) > 1:
    arguments.append(sys.argv[1])

Popen(arguments,
      stderr=STDOUT, stdout=DEVNULL)
log.log('Started ' + ' '.join(arguments))
