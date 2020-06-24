def Seidel(n):
    N = n - 1
    h = 1 / N
    x = [i * h for i in range(n)]
    y = [i * h for i in range(n)]
    
    u = [[0 for i in range(n)] for j in range(n)]
    M = 1
    eps = 0.0001

    for i in range(n):
        u[0][i] = func(x[0], y[i])
        u[N][i] = func(x[N], y[i])
        u[i][0] = func(x[i], y[0])
        u[i][N] = func(x[i], y[N])

    while eps < M:
        M = 0
        for i in range(1, N):
            for j in range(1, N):
                L = (u[i+1][j] + u[i-1][j] + u[i][j+1] + u[i][j-1]) / 4
                M = max(abs(u[i][j] - L), M)
                u[i][j] = L

    return u

def func(x, y):
    return 2 * x ** 2 + 3 * y ** 2




n = 11
for row in Seidel(n):
    print(' '.join(map(lambda x: str(round(x, 2)), row)))