import socketserver
import pickle
import json
import os.path
from os import path
from Crypto import Random
from Crypto.Util import number
import SimulationPage



HEADERSIZE = 10
COMMITS_FILE = "commitments.txt"
DRAW_FILE="draw.txt"

class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def setup(self):
        self.draw=11111111
        print("setup done")


    def handle(self):
        full_msg = b''
        new_msg = True
        # self.request is the TCP socket connected to the client
        msg = self.request.recv(1024)
        if new_msg:
            print(f'new message length: {msg[:HEADERSIZE]}')
            msglen = int(msg[:HEADERSIZE])
            new_msg = False
        full_msg += msg
        if len(full_msg) - HEADERSIZE == msglen:
            print(full_msg[HEADERSIZE:])
            self.data = pickle.loads(full_msg[HEADERSIZE:])
            new_msg = True
            full_msg = b''
            print(type(self.data))
            if str(type(self.data)) == "<class 'int'>":
                if(int(self.data)==1):
                    self.__getDraw()
                if (int(self.data)>=10000000 and int(self.data)<=99999999 ):
                    self.__setDraw()

            if str(type(self.data)) == "<class 'dict'>":
                self.__writeCommit()
            else:
                if str(type(self.data)) =="<class 'list'>":
                    self.__checkCommit()

    def generate(self,par):
        q = par[1]
        g = par[2]
        h = par[3]
        return q, g, h

    def __setDraw(self):
        draw = int(self.data)
        self.request.send(str(self.draw).encode('utf-8'))
        f = open(DRAW_FILE, "w")
        f.write(str(draw))
        f.close()
        self.request.send(str(draw).encode('utf-8'))


    # def setup(self, security):
    #
    #     p = number.getPrime(2 * security, Random.new().read)
    #     q = 2 * p + 1
    #
    #     g = number.getRandomRange(1, q - 1)
    #     s = number.getRandomRange(1, q - 1)
    #     print("Secret value:\t", s)
    #     h = pow(g, s, q)
    #
    #     param = (p, q, g, h)
    #     print("p=", p)
    #     print("q=", q)
    #     print("g=", g)
    #     print("h=", h)
    def __getDraw(self):
        print(self.draw)
        # msg = pickle.dumps(self.draw)
        # msg = bytes(f'{len(msg): <{1}}', 'utf-8') + msg
        # print("msg:",msg)
        with open(DRAW_FILE, 'r') as f:
            for line in f:
                num = int(line)
                print("num is",num)
        self.request.send(str(num).encode('utf-8'))

    def __writeCommit(self):
        self.request.send(b'Commitment Recived')
        if path.exists(COMMITS_FILE):
            with open(COMMITS_FILE, mode='r',encoding='utf-8') as commsjson :
                comms = json.load(commsjson)

            with open(COMMITS_FILE, mode='w', encoding='utf-8') as commsjson:
                entry = {}
                key = list(self.data.keys())
                comms[key[0]] = self.data[key[0]]
                print("12121\t",comms)
                json.dump(comms, commsjson)
        else:
            with open(COMMITS_FILE, mode='w',encoding='utf-8') as commsjson :
                json.dump(self.data, commsjson)

    def __checkCommit(self):#add Loterry Numbers Implimentation
        q, g, h = self.generate(self.data[0])
        with open(COMMITS_FILE, mode='r', encoding='utf-8') as commsjson:
            comms = json.load(commsjson)
            for i in comms.keys():
                sum = int(comms[i][0])
                res = (pow(g, self.data[1], q) * pow(h, sum, q)) % q
                if int(i) == res:
                    j = comms[i][1]
                    sum = comms[i][2]
                    res = (pow(g, self.draw, q) * pow(h, sum, q)) % q
                    if int(j) == res:
                        print("Id:{} has won".format(self.data[1]))
                        self.request.send(b'Has won congratulations')
        self.request.send(b'Did not win')


if __name__ == "__main__":
    HOST, PORT = "localhost", 9999


    # Create the server, binding to localhost on port 9999
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        # Activate the server; this will keep running until you
        # interrupt the program with Ctrl-C
        server.serve_forever()
