#!bin/python3
#Socket programming in python

import socket
HOST = '127.0.0.1'
PORT = 5000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 5000))