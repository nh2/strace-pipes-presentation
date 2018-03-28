#!/usr/bin/env python2

from __future__ import print_function
import subprocess
from subprocess import PIPE
import sys


p = subprocess.Popen(['./command-client.py', "ls"], stdout=PIPE)

sys.stdout.write(p.communicate()[0])
