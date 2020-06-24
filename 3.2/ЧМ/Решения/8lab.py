from sympy import symbols, exp, diff, integrate
from sympy.solvers import solve
from numpy import zeros

def Collocation():
    x, y, z = symbols('x y z')
    u = [y*(5 - x**2)+z*(9 - x**4)]
    form = u[0]

    for _ in range(2):
        form = diff(form, x)
        u.append(form)

    func = (u[2])-(u[1])-2*(u[0])+3*exp(-x)
    ans = [func.subs(x, 0.1), func.subs(x, 0.5)]
    
    return solve(ans, [y, z])


def Ritz():
    x, y, z = symbols('x y z')
    u = [y*(5 - x**2)+z*(9 - x**4), diff(y*(5 - x**2)+z*(9 - x**4), x)]

    F = -3*exp(-x)
    Q = -2
    P = -1

    px = exp(integrate(P, (x, 0, x)))
    qx = px * Q
    fx = px * F

    J = (px)*(u[1])**2 - (qx)*(u[0])**2 + 2*fx*u[0]
    ans = []
    ans.append(integrate(diff(J, y), (x, 0, 1)))
    ans.append(integrate(diff(J, z), (x, 0, 1)))

    return solve(ans, [y, z])


basis = ['0', '(5 - x**2), (9 - x**4)']


ans = Collocation()
ans = Ritz()
#y, z = symbols('y z')
#print(ans)
#print('u(x) = {} - {}*x^2 - {}*x^4'.format(round(5*ans[y] + 9*ans[z], 4), abs(round(ans[y], 4)), abs(round(ans[z], 4))))