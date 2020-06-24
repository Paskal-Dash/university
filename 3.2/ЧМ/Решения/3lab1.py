def IRK_2(arr, h):                      #Ixplicit second-degree Runge-Kutta method (#5)
    for i in range(0, int(len(arr))-1):
        x, y = arr[i]
        k1 = func(x+h, IEM(x, y, h))
        k2 = func(x, IEM(x, y, h) - h * k1)
        arr[i+1][1] = y + (h/2) * (k1 + k2)

    return arr


def IEM(x, y, h):                       #The explicit formula of Euler
    return y + h * func(x, y)

def func(x, y):
    return x + y

h = 0.1
ans = [[h*i for j in range(2)] for i in range(101)]
ans[0][1] = 1


for x, y in IRK_2(ans, h):
    print('({}; {})'.format(round(x, 1), round(y, 7)))