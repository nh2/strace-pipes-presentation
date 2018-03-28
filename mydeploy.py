#!/usr/bin/env python3

import subprocess
from subprocess import PIPE
import sys


p = subprocess.Popen(['./mybuild.py', "test"], stdout=PIPE)

p.wait()
sys.stdout.buffer.write(p.stdout.read())

# sys.stdout.buffer.write(p.communicate()[0])
