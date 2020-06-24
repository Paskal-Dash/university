from math import exp, sin, pi
import matplotlib.pyplot as plt
import matplotlib as mpl

def Implicit_scheme(N, H):
    n = 0.02
    h = 0.4
    U = [[0 for i in range(H)] for j in range(N)]
    for i in range(H):
        U[0][i] = round(func(h*i, 0), 6)    

    q = n/h**2
    a = -q * 4 / pi**(1/2)
    b = 1 - 2*a
    
    for i in range(1, N):
        A = [-a/b]
        B = [U[i-1][0]/b]
        for j in range(1, H):
            A.append(-a/(a*A[j-1] + b))
            B.append((U[i-1][j] - a*B[j-1])/(a*A[j-1] + b))

        U[i][0], U[i][H-1] = round(func(0, n * i), 6), round(func(4, n * i), 6)
        for j in range(H-2, 0, -1):
            U[i][j] = round(A[j] * U[i][j+1] + B[j], 6)

    return U

def func(x, t):
    return exp(-t * 3.14) * sin(pi * x/4)


n = 6       #times steps
h = 11      #X's steps

X = [4/(h-1) * i for i in range(h)]

for arr in Implicit_scheme(n, h):
    for j in range(h):
        print('({}; {}) '.format(str(X[j]), str(arr[j])))
    print()
    plt.plot(X, arr)

plt.show()