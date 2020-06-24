from math import sin
#/////////// Function parameters ///////////////////////////////////////////////////////////////////

q = lambda x: 1
r = lambda x: -x

func = lambda x: sin(x) / sin(1) - x

alpha_0, alpha_1 = 1, 1
beta_0, beta_1 = 0, 0   
gamma_0, gamma_1 = 0, 0

Lmbd = lambda h0, h1: 1 - Nu(h0, h1)
Nu = lambda h0, h1: h0 / (h0 + h1)

#///////////////////////////////////////////////////////////////////////////////////////////////////

def Spline(X):

    #/////////// Initialization ////////////////////////////////////////////////////////////////////
    
    sizeX = len(X)
    h = [X[i+1] - X[i] for i in range(sizeX-1)]

    eps = [max(h[i], h[i+1]) for i in range(sizeX-2)]

    index_A = lambda h0, eps: 1 - eps**2/h0**2
    index_B = lambda h0, h1, eps: 2 + eps**2/(h0*h1)
    index_C = lambda h1, eps: 1 - eps**2/h1**2

    index_f0 = alpha_0 * h[0] - beta_0 * (1 - q(X[0]) * h[0]**2 / 3)
    index_f1 = beta_0 * (1 + q(X[1]) * h[0]**2 / 6)
    index_f2 = gamma_0 * h[0] + beta_0 * h[0]**2 * (2 * r(X[0]) + r(X[1])) / 6
    
    index_l0 = beta_1 * (-1 - h[-1]**2 * q(X[-2]) / 6)
    index_l1 = alpha_1 * h[-1]**2 + beta_1 * (1 - h[-1]**2 * q(X[-1]) / 3)
    index_l2 = gamma_1 * h[-1] - beta_1 * h[-1]**2 * (r(X[-2]) + 2 * r(X[-1])) / 6

    a = [0]
    b = [index_f0]
    c = [index_f1]
    f = [index_f2]

    for i in range(1, sizeX-1):
        a.append(Lmbd(h[i-1], h[i]) * (1 + h[i-1]**2 * q(X[i-1]) * index_A(h[i-1], eps[i-1]) / 6))
        b.append(-1 + h[i] * h[i-1] * q(X[i]) * index_B(h[i-1], h[i], eps[i-1]) / 6)
        c.append(Nu(h[i-1], h[i]) * (1 + h[i]**2 * q(X[i+1]) * index_C(h[i], eps[i-1]) / 6))
        f.append(h[i-1] * h[i] * (Nu(h[i-1], h[i]) * index_A(h[i-1], eps[i-1]) * r(X[i-1]) + index_B(h[i], h[i-1], eps[i-1]) * r(X[i]) + Lmbd(h[i], h[i-1]) * index_C(h[i], eps[i-1]) * r(X[i+1])) / 6)

    a.append(index_l0)
    b.append(index_l1)
    c.append(0)
    f.append(index_l2)

    #/////////// Run-Through Method ////////////////////////////////////////////////////////////////

    A, B = [-c[0]/b[0]], [f[0]/b[0]]

    for i in range(1, sizeX):
        e = a[i] * A[i-1] + b[i]
        A.append(-c[i] / e)
        B.append((f[i] - a[i] * B[i-1]) / e)

    u = [0 for i in range(sizeX)]

    u[-1] = (f[-1] - a[-1] * B[-1]) / (b[-1] + a[-1] * A[-1])

    for i in range(sizeX-2, -1, -1):
        u[i] = A[i] * u[i+1] + B[i]             

    #/////////// Сalculation  M ///////////////////////////////////////////////////////////////////

    M = [r(X[i]) - u[i] * q(X[i]) for i in range(sizeX)]

    #/////////// Getting Splines //////////////////////////////////////////////////////////////////  

    Y = []

    for i in range(sizeX-1):
        for j in range(i, i+2):
            t = (X[j] - X[i]) / h[i]

            Y.append((X[j], u[i] * (1 - t) + t * u[i+1] - t * (1 - t) * h[i]**2 * ((2 - t) * M[i] + (1 + t) * M[i+1]) / 6))

    return Y 


#///////////////////////////////////////////////////////////////////////////////////////////////////


X = [0, 0.19, 0.33, 0.54, 0.81, 1]
#X = [0, 0.2, 0.4, 0.6, 0.8, 1]

#for i in range(len(X)):
#    print('({}; {})'.format(str(X[i]), str(round(func(X[i]), 4))))

#print()

#for pair in Spline(X):
#    print('({}; {})'.format(str(pair[0]), str(round(pair[1], 4))))

Y = list(frozenset(Spline(X)))

for i in range(len(X)):
    print('{} {}'.format(str(Y[i][0]), str(round(abs(round(abs(func(Y[i][0])), 4) - round(abs(Y[i][1]), 4)), 4))))