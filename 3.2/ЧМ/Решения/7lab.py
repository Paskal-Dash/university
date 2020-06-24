from numpy import zeros, set_printoptions

g = p = s = 0
a = 1
G0 = lambda t: t * (t-1)
G1 = lambda t: 3 * t ** 2


def SoE(n, h):
    N = n-1
    t = [i*h for i in range(n)]
    u = zeros(shape=(n, n))

    for i in range(n):
        u[i, 0] = p
        u[0, i] = G0(t[i])
        u[N, i] = G1(t[i])

    for i in range(1, N):
        u[i, 1] = u[i, 0] - (u[i-1, 0] - 2*u[i, 0] + u[i+1, 0])/2

    for i in range(1, N):
        for j in range(1, N):
            u[i, j+1] = u[i, j] - u[i, j-1] + u[i-1, j] + u[i+1, j]

    return u 


set_printoptions(precision = 3)
n, h = 11, 0.1
print(SoE(n, h))