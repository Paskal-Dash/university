from numpy import array, zeros, diag, diagflat, dot, amax

def Jacobi(n, h):
    x = [i * h for i in range(n)]
    y = [i * h for i in range(n)]
    A = zeros(shape = (n*n, n*n))

    func = lambda x, y: 2 * x**2 + 3 * y**2

    u = zeros(n*n)
    N = n-1    

    for i in range(n*n):
        if i < n:
            u[i] = func(x[i], y[0])
            continue
        if n*n - i - 1 < n:
            u[i] = func(x[i % n], y[N])
            continue
        if i % n == 0:
            u[i] = func(x[0], y[i // n])
            continue
        if i % n == n-1:
            u[i] = func(x[N], y[i // n])
            continue

    u_prev = zeros(n*n)
    for i in range(n*n):
        A[i, i] = 1
        if i < n or n*n - i - 1 < n or i % n == 0 or i % n == n - 1:
            continue
        A[i, i + 1] = 0.2
        A[i, i - 1] = 0.2
        A[i, i + n] = 0.2 
        A[i, i - n] = 0.2

    f = zeros(n*n)
    for _ in range(100):
        for i in range(n):
            S = sum([A[i, j] * u_prev[j] if i != j else 0 for j in range(n)])
            u[i] = (f[i] - S) / A[i, i]
        u_prev = u

    return u




N, h = 10, 0.1
u = Jacobi(N, h)
for i in range(N):
    print(u[(N*i):(N*(i+1))])