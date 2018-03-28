#!/usr/bin/env python2

from __future__ import print_function
import socket
import subprocess
from subprocess import PIPE

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serversocket.bind(("localhost", 1234))
serversocket.listen(5)

def run_command_for_client(command, clientsocket):
  if command in ["ls", "dmesg"]:
    p = subprocess.Popen([command], stdout=PIPE)
    p.wait()
    out = p.stdout.read()
  else:
    out = b"command not allowed\n"
  clientsocket.sendall(out)

# Server loop
while True:
  (clientsocket, address) = serversocket.accept()

  command = clientsocket.recv(100).decode('utf-8')
  print("server got command: " + command)

  run_command_for_client(command, clientsocket)

  clientsocket.close()
