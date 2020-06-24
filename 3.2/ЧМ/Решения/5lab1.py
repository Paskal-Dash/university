from math import exp, sin, pi
import matplotlib.pyplot as plt
import matplotlib as mpl

def Explicit_scheme(N, H):
    n = 0.02
    h = 0.4
    U = [[0 for i in range(H)] for j in range(N)]
    for i in range(H):
        U[0][i] = round(func(h*i, 0), 6)
    
    for i in range(1, N):
        U[i][0], U[i][H-1] = round(func(0, n * i), 6), round(func(4, n * i), 6)
        for j in range(1, H-1):
            U[i][j] = round(scheme(U[i-1][j-1], U[i-1][j], U[i-1][j+1], h, n), 6)

    return U

def func(x, t):
    return exp(-t * 3.14) * sin(pi * x/4)

def scheme(u0, u1, u2, h, g, a = 4/(pi**(1/2))):
    q = g / h**2
    return q*a*u0 + (1 - 2 * q*a)*u1 + q*a*u2



n = 6       #times steps
h = 11      #X's steps
X = [4/(h-1) * i for i in range(h)]

Y = [[] for i in range(n)]
for i in range(n):
    for j in range(h):
        Y[i].append(round(func(0.4*j, 0.02*i), 6))

T = [0, 0.02, 0.04, 0.06, 0.08, 0.1]
for arr in Explicit_scheme(n, h):
    for j in range(h):
        print('({}; {})'.format(str(X[j]), str(arr[j])))
    print()
    plt.plot(X, arr)

plt.show()