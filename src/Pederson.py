# https://asecuritysite.com/encryption/ped

from Crypto import Random
from Crypto.Util import number
import src.Client as Client
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
    print("commit value for ID: ", c1)
    print("commit value for Guess: ", c2)
    return Client.makeComitment({c1: (r1,c2,r2)})

