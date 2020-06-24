from math import exp
import matplotlib.pyplot as plt
import matplotlib as mpl

def isP(x):
    return -x+1

def isQ(x):
    return -1

def isR(x, h):
    return (isP(x)/2) * h

def isA(x, h):
    return (1/(h**2)) * (1 - isR(x, h))

def isC(x, h):
    return (1/(h**2)) * (1 + isR(x, h))

def isB(x, a, c):
    return isQ(x) - a - c

def func(x):
    return 2 / (x + 1)**3

def MMS(h, N):
    X = [h*i for i in range(N+1)]
    d = [func(x) for x in X]
    a = [isA(x, h) for x in X]
    c = [isC(x, h) for x in X]
    b = [isB(X[i], a[i], c[i]) for i in range(N+1)]
    a[0] = c[N] = 0
    b[0], b[N] = isB(X[0], 0, c[0]), isB(X[N], a[N], 0)
    A, B = [], []

    A.append(1)
    B.append(0)

    for i in range(1, N+1):
        z = a[i]*A[i-1] + b[i]
        A.append(-c[i]/z)
        B.append((d[i] - a[i]*B[i-1])/z)

    Y = [0 for i in range(N+1)]
    Y[N] = 0.5

    for i in range(N-1, -1, -1):
        Y[i] = A[i] * Y[i+1] + B[i]

    return Y


N, h = 10, 0.1

Y = MMS(h, N)


Y1 = []
for i in range(N+1):
    Y1.append(1/(h*i + 1))

for i in range(N+1):
    print(Y1[i], Y[i], sep = ' '*(25-len(str(Y1[i]))))

plt.plot([h*i for i in range(N+1)], Y)
plt.plot([h*i for i in range(N+1)], Y1)
plt.show() 
