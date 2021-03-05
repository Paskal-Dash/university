#Option #10

N, k, alpha, n, A = 10, 10, 1/6, 4, 20

X = [N * pow(10, 4)]
Z, u = [], []

q = (3 + N * 0.1) * 0.01
c = (10 + N * 0.3) * 0.01
cwave = c / q**(1 / alpha)

beta = alpha / (1 - alpha)


#Ex. 1 & 2 

def bellman():

    for i in range(1, n + 1):

        count = 0
        for j in range(0, n - i + 1): count += cwave**(j * beta)

        Z.append(q**(n - k) * (X[i - 1] * count**(1 / beta))**alpha)

    return


def optional_solution():
    
    for i in range(1, n + 1):
        
        count = 0
        for j in range(0, i + 1): count += cwave**(j * beta)

        u.append(X[i - 1] / count)
        X.append(c*(X[i - 1] - u[-1]))

    return

optional_solution()
bellman()

print("1. Оптимальное решение u* = {};\n2. Оптимальная траектория X* = {};\n3. Оптимальное значение целевой функции на всем интервале в n = {} периодов: F*(x0) = {}".format(u, X, str(n), str(A*q*Z[0])))
print("4. Функция Беллмана от 1 по n = {}: Z* = {}".format(str(n), Z))


#Ex. 3 

def next_bellman():

    new_c = c
    new_cwave = cwave
    for i in range(1, n + 1):

        if i == 2:
            new_c = (18 + 0.3 * N) * 0.01
            new_cwave = new_c / q**(1 / alpha)

        count = 0
        for j in range(0, n - i + 1): count += new_cwave**(j * beta)

        Z.append(q**(n - k) * (X[i - 1] * count**(1 / beta))**alpha)

    return


def next_optional_solution():

    new_c = c
    new_cwave = cwave
    for i in range(1, n + 1):

        if i == 2:
            new_c = (18 + 0.3 * N) * 0.01
            new_cwave = new_c / q**(1 / alpha)
        
        count = 0
        for j in range(0, i + 1): count += new_cwave**(j * beta)

        u.append(X[i - 1] / count)
        X.append(new_c*(X[i - 1] - u[-1]))

    return

#next_optional_solution()
#next_bellman()

#print("1. Оптимальное решение u* = {};\n2. Оптимальная траектория X* = {};\n3. Оптимальное значение целевой функции на всем интервале в n = {} периодов: F*(x0) = {}".format(u, X, str(n), str(A*q*Z[0])))
#print("4. Функция Беллмана от 1 по n = {}: Z* = {}".format(str(n), Z))
