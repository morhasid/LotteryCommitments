#!/usr/bin/env python3
import socket
import pickle

HOST = "localhost" # The server's hostname or IP address
PORT = 9999        # The port used by the server
HEADERSIZE = 10

def getDraw():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        msg = pickle.dumps(1)
        msg = bytes(f'{len(msg): <{HEADERSIZE}}', 'utf-8') + msg
        s.send(msg)
        data = s.recv(1024)
        print('Received', repr(data.decode()))
        return str(repr(data.decode()))

def makeComitment(data):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        msg = pickle.dumps(data)
        msg = bytes(f'{len(msg): <{HEADERSIZE}}', 'utf-8') + msg
        s.send(msg)
        data = s.recv(1024)
        print('Received', repr(data.decode()))
        return str(repr(data.decode()))



def verifyWin(data):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        msg = pickle.dumps(data)
        msg = bytes(f'{len(msg): <{HEADERSIZE}}', 'utf-8') + msg
        s.send(msg)
        data = s.recv(1024)
        print('Received', repr(data.decode()))
        return repr(data.decode())

def lotteryReques():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        msg = pickle.dumps(1)
        msg = bytes(f'{len(msg): <{HEADERSIZE}}', 'utf-8') + msg
        s.send(msg)
        data = s.recv(1024)
        print('Received', repr(data.decode()))
        return repr(data.decode())
#
# def setDraw():
