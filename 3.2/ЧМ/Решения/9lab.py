from sympy import integrate, symbols, exp
from numpy import zeros
from numpy.linalg import solve


def Core(K, alpha, beta):
    s, x = symbols('s x')
    A = zeros(shape=(3, 3))
    f = zeros(3)
    for i in range(3):
        z = K + '*' + alpha[i]
        f[i] = float(integrate(z, (s, 0, 1)))
        for j in range(3):
            z = beta[i] + '*' + alpha[j]
            A[i, j] = float(integrate(z, (s, 0, 1)))*(-1)
        if i != 0:
            A[i, i] += 1

    C = zeros(3)
    C = solve(A, f)
    u = exp(-x) + C[0]*x + C[1]*(x**2) + C[2]*(x**3)
    f = u.subs(x, 0), u.subs(x, 0.5), u.subs(x, 1)
    return C, f


K = '(1+s)*(exp(0.2*s) - 1)'
alpha = ['s', 's**2', 's**3']
beta = ['(-0.2)*s*(1+s)', '(-0.02)*(s**2)*(1+s)', '(-0.00133)*(s**3)*(1+s)']


C, f = Core(K, alpha, beta)
print('C1 = {}, C2 = {}, C3 = {}\n'.format(str(round(C[0], 5)), str(round(C[1], 5)), str(round(C[2], 5))))
print('u(x) = exp(-x) + {}*x + {}*(x**2) + {}*(x**3)\n'.format(str(round(C[0], 5)), str(round(C[1], 5)), str(round(C[2], 5))))
print(f)