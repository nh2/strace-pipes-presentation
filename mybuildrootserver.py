#!/usr/bin/env python3

import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serversocket.bind(("localhost", 1234))
serversocket.listen(5)

while True:
  (clientsocket, address) = serversocket.accept()

  name = clientsocket.recv(100)

  print("server got: " + str(name))

  log_messages = (b"log message " + (b"." * 100) + b"\n") * 600
  assert(len(log_messages) >= 2**16)
  clientsocket.sendall(log_messages)
  clientsocket.close()
