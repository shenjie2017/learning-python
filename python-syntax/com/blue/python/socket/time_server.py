#!/usr/bin/env python

import socket
import time

HOST = "localhost"
PORT = 8888
BUFFSIZE = 4096

ADDR = (HOST, PORT)

ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ss.bind(ADDR)
ss.listen(5)

while True:
    print('waiting for connection...')
    cs, addr = ss.accept()
    print("connecting from:", addr)

    while True:
        data = cs.recv(BUFFSIZE)
        if not data:
            break
        print("receive data:", data)
        print("src data:[{}] time:[{}]".format(data, time.ctime()))
        cs.send(bytes("src data:[{}] time:[{}]".format(data, time.ctime()),'utf-8'))

    cs.close()
ss.close()
