# https://asecuritysite.com/encryption/ped

from Crypto import Random
from Crypto.Util import number
import Client
import sys


def generate(param):
    q = param[1]
    g = param[2]
    h = param[3]
    return q, g, h


class verifier:
    def setup(self, security):

        p = 1300726750356926024307137068697680561494928151357
        q = 2601453500713852048614274137395361122989856302715

        g = 966275592469109766944489735064204842622808098866
        s = 2032470758025326815604678846652732026179053192046
        print("Secret value:\t", s)
        h = pow(g, s, q)

        param = (p, q, g, h)
        print("p=", p)
        print("q=", q)
        print("g=", g)
        print("h=", h)

        return param

    def open(self, param, c, x, *r):
        result = "False"
        q, g, h = generate(param)
        sum = 0
        for i in r:
            sum += i

        res = (pow(g, x, q) * pow(h, sum, q)) % q

        if c == res:
            result = "True"
        return result

    def add(self, param, *cm):
        addCM = 1
        for x in cm:
            addCM *= x
        addCM = addCM % param[1]
        return addCM


class prover:
    def commit(self, param, x):
        q, g, h = generate(param)

        r = number.getRandomRange(1, q - 1)
        c = (pow(g, x, q) * pow(h, r, q)) % q
        return c, r

def commit(msg1,msg2):
    # msg1 = 321320994 id
    # msg2 = 12345671  guess
    security=80
    if (len(sys.argv) > 1):
        msg1 = int(sys.argv[1])
    if (len(sys.argv) > 2):
        msg2 = int(sys.argv[2])
    v = verifier()
    p = prover()
    param = v.setup(security) # All public values.
    c1, r1 = p.commit(param, msg1) # first commit c + random number r, ID
    c2, r2 = p.commit(param, msg2) # second ........................, Guess
    return Client.makeComitment({c1: (r1,c2,r2)})

    # Client.verifyWin([param, msg1])

    #addCM = v.add(param, c1, c2)

    # print("\nMsg1:", msg1)
    # print("Msg2:", msg2)

    # print("c1,r1:", c1, ",", r1)
    # print("c2,r2:", c2, ",", r2)
    #
    #print("\nWe can now multiply c1 and c2, which is same as adding Msg1 and Msg2")
    #print("\nCommitment of adding (Msg1+Msg2):\t", addCM)
    #
    # result1 = v.open(param, c1, msg1, r1)
    # result2 = v.open(param, c2, msg2, r2)

    # ID -> [c1, r1, c2, r2]

    #   man -> ID, guess -> (c1, r1, c2, r2) -> .....->  v.open(hash(ID)) --> save res value in v.open function


    # print("\nResult of verifying c1:\t\t", result1)
    # print("Result of verifying c2:\t\t", result2)

    #result = v.open(param, addCM, msg1 + msg2, r1, r2)

    #print("Result of verify Msg+Msg2:\t", result)
