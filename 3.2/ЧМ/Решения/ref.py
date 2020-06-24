from math import exp

def Runge_Kutta_3(y0, h):
    y = [0 for i in range(int(1/h)+1)]
    x = [h*i for i in range(int(1/h)+1)]
    y[0] = y0

    k0 = lambda x, y: h*func(x, y)
    k1 = lambda x, y: h*func(x + h/2, y + k0(x, y)/2)
    k2 = lambda x, y: h*func(x + h, y + 2*k1(x, y) - k0(x, y))
    Y = lambda x, y: y + (k0(x, y) + 4*k1(x, y) + 2*k2(x, y))/6
    for i in range(1, int(1/h)+1):
         y[i] = round(Y(x[i-1], y[i-1]), 5)

    return x, y

def Runge_Kutta_4(y0, h):
    y = [0 for i in range(int(1/h)+1)]
    x = [h*i for i in range(int(1/h)+1)]
    y[0] = y0

    k0 = lambda x, y: h*func(x, y)
    k1 = lambda x, y: h*func(x + h/2, y + k0(x, y)/2)
    k2 = lambda x, y: h*func(x + h/2, y + k1(x, y)/2)
    k3 = lambda x, y: h*func(x + h, y + k2(x, y))
    Y = lambda x, y: y + (k0(x, y) + 2*k1(x, y) + 2*k2(x, y) + k3(x, y))/6
    for i in range(1, int(1/h)+1):
         y[i] = round(Y(x[i-1], y[i-1]), 5)

    return x, y

def Runge_Kutta_5(y0, h):
    y = [0 for i in range(int(1/h)+1)]
    x = [h*i for i in range(int(1/h)+1)]
    y[0] = y0

    k0 = lambda x, y: h*func(x, y)
    k1 = lambda x, y: h*func(x + h/2, y + k0(x, y)/2)
    k2 = lambda x, y: h*func(x + h/2, y + k1(x, y)/2)
    k3 = lambda x, y: h*func(x + h/2, y + k2(x, y)/2)
    k4 = lambda x, y: h*func(x + h, y + k3(x, y))
    Y = lambda x, y: y + (k0(x, y) + 2*k1(x, y) + 2*k2(x, y) + 2*k3(x, y) + k4(x, y))/8
    for i in range(1, int(1/h)+1):
        y[i] = round(Y(x[i-1], y[i-1]), 5)

    return x, y

def func(x, y):
    return 2*y - 2

def func1(x):
    return 1 - exp(2*x)


h = 0.1
y0 = 0
ans1 = Runge_Kutta_3(y0, h)[1]
ans2 = Runge_Kutta_4(y0, h)[1]
ans3 = Runge_Kutta_5(y0, h)[1]
ans = []

for i in range(int(1/h)+1):
    print(round(func1(i*h), 5), ans1[i], ans2[i], ans3[i], sep=' '*(25-len(str(ans1[i]))))