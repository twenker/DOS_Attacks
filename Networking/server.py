#!/usr/bin/python

# Simple python server using port 12345

import socket

connectionCount = 5

# create socker
s = socket.socket()
# get local machine name
host = socket.gethostname()
print "hostname: " + host
# use port 12345
port = 12345
# bind host to port
s.bind((host, port))

s.listen(5)
while connectionCount:
    # c is new socket, addr address of client
    c, addr = s.accept()
    print 'Got connection from', addr
    # send string to client
    c.send('Thank you for connecting')
    c.close()
    connectionCount += -1

s.close()