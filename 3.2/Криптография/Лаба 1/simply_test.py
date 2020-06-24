from random import randint
from timeit import default_timer

def MR(numb, k=30):
    d, s = factor(numb-1)
    if numb <= 1:
        return False
    if numb <= 3:
        return True
    if numb % 2 == 0:
        return False

    for _ in range(k):
        a = randint(2, numb-2 )
        x = Exponentiation(a, d, numb)
        if not (x == 1 or x == numb - 1):
            for j in range(s-1):
                x = Exponentiation(a, 2**(j+1) * d, numb)
                if x == 1: return False
                if x == numb-1: break
        else: return True
    return True

def SS(n, k=30):
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False

    for _ in range(k):
        a = randint(3, n-2)
        if gcd(a, n) != 1:
            return False
        if Exponentiation(a, (n-1)//2, n) != (jacobi(a, n) % n):
            return False
    return True

def gcd(a, b):
    while b:
        a %= b
        a, b = b, a
    return a

def jacobi(a, n):
    t = 1
    while a != 0:
        while a % 2 == 0:
            a /= 2
            r = n % 8
            if r == 3 or r == 5:
                t = -t
        a, n = n, a
        if a % 4 == n % 4 == 3:
            t = -t
        a %= n
    if n == 1:
        return t
    else:
        return 0

def Exponentiation(elem, degree, modulus):
    c = 1
    for _ in range(degree):
        c = (c * elem) % modulus
    return c

def factor(numb):
    n = numb
    count = 0
    while(True):
        if n % 2 == 1: return int(n), count
        n /= 2
        count += 1

def test(_range, algorithm):
    times = []

    for i in _range:
        t = default_timer()
        algorithm(2**i)
        times.append('{:.10f}'.format(default_timer() - t))
    return times

_range = range(5, 11)

print(test(_range, MR))
print(test(_range, SS))