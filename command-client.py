#!/usr/bin/env python2

from __future__ import print_function
import socket
import sys

name = sys.argv[1]

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("localhost", 1234))

sock.sendall(name.encode('utf-8'))

while True:
  data = sock.recv(100)
  if len(data) == 0:
    break
  sys.stdout.write(data)
