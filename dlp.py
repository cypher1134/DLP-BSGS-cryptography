from prime import is_probable_prime
from math import sqrt
import random


#Exercice 1
#Q1


def bezout(a,b):
    r, u, v, rp, up, vp = a, 1, 0, b, 0, 1
    q=0
    while(rp!=0):
        q = r//rp
        rs = r
        us = u
        vs = v
        r = rp
        u = up
        v = vp
        rp = rs - q*rp 
        up = us - q*up
        vp = vs - q*vp

    return (r,u,v)


#Q2
def inv_mod(a, N):
    """ Return  l'inverse de a dans Z/NZ. """
    _,u,_ = bezout(a, N)
    return u

def invertibles(N):
    """ Return a list of all the invertibles in Z/NZ. """
    return [a for a in range(N) if bezout(a, N)[0] == 1]



#Q3
def phi(N):
    return len(invertibles(N))



#Exercice 2
#Q1
def exp(a,N,p):
    def decomposition_binaire(N):
        L=[]
        while (N>0):
            L.append(N%2)
            N=N//2
        L.reverse()
        return L
    inv=1
    for ei in decomposition_binaire(N):
        inv=(inv*inv)%p
        if (ei==1):
            inv=(inv*a)%p
    return inv
# def exp(x,y,p):
#     res=1
#     x=x%p #if x>p
#     if(x==0):
#         return 0
#     while(y>0):
#         if(y&1): #y i odd
#             res=(res*x)%p
#         y=y>>1 #y=y/2
#         x=(x*x)%p
#     return res




#Q2
def factor(n):
    def gen_all_factors(n):
        L=[]
        i=2 
        while n>1: 
            while n%i==0: 
                L.append(i)
                n=n/i 
            i=i+1
        return L
    

    factors_all = list(gen_all_factors(n))

    factors_set = set(factors_all)
    return [(p, factors_all.count(p)) for p in factors_set]




#Q3
def order(a, p, factors_p_minus1):
    a %= p #if a > p
    ord_a = p - 1
    for (q, e) in factors_p_minus1:
        ord_a //= q**e
        aa = exp(a, ord_a, p)
        for i in range(e + 1):
            if aa == 1:
                break
            aa = exp(aa, q, p)
            ord_a *= q
    return ord_a


#Q4
def find_generator(p, factors_p_minus1):
    
    a = random.randint(0, p - 1)
    while order(a, p, factors_p_minus1) != p - 1:
        a = random.randint(0, p - 1)
    return a



def generate_safe_prime(k):
    p = random.randint(2**(k-2), 2**(k-1) - 1)
    while not (is_probable_prime(p) and is_probable_prime(2 * p + 1)):
        p = random.randint(2**(k-1), 2**k - 1)
    return 2 * p + 1



#Q6
def bsgs(n, g, p):
    s = int(sqrt(p)) + 1
    tabg = dict()
    gs = exp(g, s, p)
    invgs = inv_mod(gs, p)
    tabg[n] = 0
    v = n
    for q in range(s):
        tabg[v] = q
        v = (v * invgs) % p
    tabb = 1
    for r in range(s):
        if tabb in tabg:
            log = (r + tabg[tabb] * s) % (p - 1)
            return log
        tabb = (tabb * g) % p
