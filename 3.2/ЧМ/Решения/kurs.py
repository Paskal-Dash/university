from sympy import Symbol

#Решение краевой задачи для ОДУ 2-го порядка 
#с помощью разностной схемы метода сплайн-коллокаций

q = lambda x: -3 / (x+1)**2
r = lambda x: -1.5 / (x+1)**(1/2)
func = lambda x: 2/3 * (x+1)**(3/2)          #точное решение
N = lambda h0, h1: h0/(h1 + h0)
L = lambda h0, h1: h1/(h1 + h0)

alpha_0, alpha_1 = 3, 0
beta_0, beta_1 = -1, 1
gamma_0, gamma_1 = 1, 2**(1/2)
                                            #вышеуказанные параметры могут изменяться


def Spline(X):                              
    Q, R, h, Eps = [], [], [], []
    u = [0 for i in range(len(X))]

    for x in X:
        Q.append(q(x))
        R.append(r(x))

    for i in range(len(X)-1):
        h.append(X[i+1] - X[i])

    for i in range(1, len(X)-1):
        Eps.append(h[i])

    F = lambda h0, h1, e, r0, r1, r2: h0*h1/6 * (N(h0, h1)*(1-e**2/h0**2)*r0 +(2+e**2/(h0*h1))*r1 + L(h0, h1)*(1 - e**2/h1**2)*r2)

    a = [L(h[i-1], h[i])*(1 + (h[i-1]**2 - Eps[i-1]**2)/6 * Q[i-1]) for i in range(1, len(X)-1)]
    c = [N(h[i-1], h[i])*(1 + (h[i]**2 - Eps[i-1]**2)/6 * Q[i+1]) for i in range(1, len(X)-1)]
    b = [-(1 - (2*h[i]*h[i-1] + Eps[i-1]**2)/6 * Q[i]) for i in range(1, len(X)-1)]
    f = [F(h[i-1], h[i], Eps[i-1], R[i-1], R[i], R[i+1]) for i in range(1, len(X)-1)]

    A, B = [], []

    A.append(-c[0]/b[0])
    B.append(f[0]/b[0])

    for i in range(1, len(X)-2):
        z = a[i]*A[i-1] + b[i]
        A.append(-c[i]/z)
        B.append((f[i] - a[i]*B[i-1])/z)

    u[-2] = (f[-1] - a[-1]*B[-1])/(b[-1] + a[-1]*A[-1])

    for i in range(len(X)-3, 0, -1):
        u[i] = A[i-1]*u[i+1] + B[i-1]

    u[-1] = (gamma_1*h[-1] - 1/6 * beta_1 * h[-1]**2 *(R[-2] + 2*R[-1]) - u[-2]*beta_1*(-1 - 1/6 * h[-1]**2 * Q[-2])) / (alpha_1*h[-1] + beta_1*(1-1/3 * h[-1]**2 * Q[-1]))
    u[0] = (gamma_0*h[0] + 1/6 * beta_0 * h[0]**2 *(2*R[0] + R[1]) - u[1] * beta_0 * (1 + 1/6 * Q[1] * h[0]**2)) / (alpha_0*h[0] - beta_0*(1 - 1/3 * Q[0] * h[0]**2))

    M = []
    for i in range(len(X)):
        M.append(R[i] - Q[i]*u[i])

    Y = []
    x = Symbol('x')
    for i in range(len(X)-1):
        t = (x-X[i])/h[i]
        Y.append(u[i] * (1 - t) + u[i+1] * t - (h[i]**2)/6 * t * (1 - t) * ((2 - t)* M[i] + (1 + t)*M[i+1]))

    return Y

X = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]

Y = Spline(X)

x = Symbol('x')
for i in range(len(X)-1):
    print('({}; {}) ({}; {})'.format(str(X[i]), str(Y[i].subs(x, X[i])), str(X[i+1]), str(Y[i].subs(x, X[i+1]))))

