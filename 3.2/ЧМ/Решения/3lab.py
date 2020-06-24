from math import exp

def func(x, y):                         #y' = f(x,y)
    return x + y                         


def RK_2(arr, h):                      #Second-degree Runge-Kutta method (#1)
    for i in range(0, int(len(arr))-1):
        x, y = arr[i]
        k1 = func(x, y)
        k2 = func(x + h/3, y + (h/3) * k1)
        k3 = func(x + h/3, y + (h/3) * k2)
        arr[i+1][0] = x + h
        arr[i+1][1] = y + (h/4) * (k1 + 3 * k3)

    return arr


def RK_3(arr, h):                      #Third-degree Runge-Kutta method (#2)
    for i in range(0, int(len(arr))-1):
        x, y = arr[i]
        k1 = func(x, y)
        k2 = func(x + h/4, y + (h/4) * k1)
        k3 = func(x + h/2, y + (h/2) * k2)
        k4 = func(x + h, y + h * k1 - 2*h * k2 + 2*h * k3)
        arr[i+1][0] = x + h
        arr[i+1][1] = y + (h/6) * (k1 + 4 * k3 + k4)

    return arr


def RK_4(arr, h):                      #Fourth-degree Runge-Kutta method (#3)                   
    for i in range(0, int(len(arr))-1):
        x, y = arr[i]
        k1 = func(x, y)
        k2 = func(x + h/2, y + (h/2) * k1)
        k3 = func(x + h/2, y + (h/2) * k2)
        k4 = func(x + h, y + h * k3)
        arr[i+1][0] = x + h
        arr[i+1][1] = y + (h/6) * (k1 + 2 * k2 + 2 * k3 + k4)

    return arr


def M_Broken(arr, h):                   #an improved method broken (#4)
    for i in range(0, int(len(arr)) - 1):
        x, y = arr[i]
        k1 = func(x, y)
        k2 = (x + h/2, y + (h/2) * k1)
        arr[i+1][0] = x + h
        arr[i+1][1] = y + h * k2

    return arr


def IRK_2(arr, h):                      #Ixplicit second-degree Runge-Kutta method (#5)
    for i in range(0, int(len(arr))-1):
        x, y = arr[i]
        k1 = func(x+h, IEM(x, y, h))
        k2 = func(x, IEM(x, y, h) - h * k1)
        arr[i+1][0] = x + h
        arr[i+1][1] = y + (h/2) * (k1 + k2)

    return arr


def IEM(x, y, h):                       #The explicit formula of Euler
    return y + h * func(x, y)


def RK6_3(arr, h):                      #Third-degree Runge-Kutta method (#6)
    for i in range(0, int(len(arr))-1):
        x, y = arr[i]
        k1 = func(x, y)
        k2 = func(x + h/2, y + (h/2) * k1)
        k3 = func(x + h/4, y + (h/4) * k2)
        arr[i+1][0] = x + h
        arr[i+1][1] = y + (h/9) * (2*k1 + 3*k2 + 4 * k3)

    return arr


def RK7_2(arr, h):                      #Second-degree Runge-Kutta method (#7)
    for i in range(0, int(len(arr)) - 1):
        x, y = arr[i]
        k1 = func(x, y)
        k2 = (x + h/2, y + (h/2) * k1)
        arr[i+1][0] = x + h
        arr[i+1][1] = y + h * k2

    return arr


def ITF(arr, h):                        #an implicit formula of a trapezoid (#8)
    for i in range(0, int(len(arr)) - 1):
        x, y = arr[i]
        arr[i+1][0] = x + h
        arr[i+1][1] = y + h * func(x + h/2, (y + EF(x, y, h))/2)

    return arr


def EF(x, y, h):                        #Explicit formul
    return y + h * func(x + h/2, y + func(x, y) * h/2)


def RG9_3(arr, h):                      #Third-degree Runge-Kutta method (#9)
    for i in range(0, int(len(arr)) - 1):
        x, y = arr[i]
        k1 = func(x, y)
        k2 = func(x + h/2, y + (h/2) * k1)
        k3 = func(x + h, y - h*k1 - 2*h*k2)
        arr[i+1][0] = x + h
        arr[i+1][1] = y + (h/6) * (k1 + 4*k2 + k3)

    return arr


def RG10_4(arr, h):                     #Fourth-degree Runge-Kutta method (#10)
    for i in range(0, int(len(arr)) - 1):
        x, y = arr[i]
        k1 = func(x, y)
        k2 = func(x + h/3, y + (h/3) * k1)
        k3 = func(x + h/3, y + (h/3)*k2)
        k4 = func(x + h, y + h*k1 - h*k2 + h*k3)
        arr[i+1][0] = x + h
        arr[i+1][1] = y + (h/8) * (k1 + 3*k2 + 3*k3 + k4)

    return arr


def IRK_3(arr, h):                      #Ixplicit third-degree Runge-Kutta method (#11)
    for i in range(0, int(len(arr)) - 1):
        x, y = arr[i]
        r1 = func(x+h, ER_KF(x, y, h))
        r2 = func(x + 2*h/3, ER_KF(x, y, h) - (h/3) * r1)
        r3 = func(x + h/3, ER_KF(x, y, h) - (2*h/3)*r2)
        arr[i+1][0] = x + h
        arr[i+1][1] = y + (h/4) * (r1 + 3*r3)

    return arr


def ER_KF(x, y, h):                     #Explicit Runge-Kutta formula
    return y + (h/4) * (func(x, y) + 3 * func(x + h/3, y + (h/3) * func(x + h/3, y + (h/3) * func(x, y))))


def Adams_2(arr, h):                    #Second-degree Adams method (#12)
    arr[1] = [arr[0][0] + h, EK(arr[0][0], arr[0][1], h)]
    for i in range(0, int(len(arr)) - 2):
        x, y = arr[i]
        x1, y1 = arr[i+1]
        arr[i+2][0] = arr[i+1][0] + h
        arr[i+2][1] = y1 + (h/2) * (3*func(x1, y1) - func(x, y))

    return arr


def EK(x, y, h):                        #Euler-Koshi formul
    return y + (h/2) * (func(x, y) + func(x + h, y + h * func(x, y)))


def IRK(arr, h):                       #Ixplicit Runge-Kutta method (#13)
    for i in range(0, int(len(arr)) - 1):
        x, y = arr[i]
        k1 = func(x+h, EF(x, y, h))
        k2 = func(x + (h/2), EF(x, y, h) - (h/2) * k1)
        arr[i+1][0] = x + h
        arr[i+1][1] = y + h * k2

    return arr


def KH_2(arr, h):                      #Second_degree Curtis-Hirschfeld method (#14)
    arr[1] = [arr[0][0] + h, EK(arr[0][0], arr[0][1], h)]
    for i in range(0, int(len(arr)) - 2):
        x, y = arr[i]
        x1, y1 = arr[i+1]
        arr[i+2][0] = arr[i+1][0] + h
        arr[i+2][1] = (4/3) * y1 - (1/3) * y + (2*h/3) * func(x1 + h, EAF(x, y1, y, h))

    return arr


def EAF(x, y1, y0, h):                  #Explicit Adams formul
    return y1 + (h/2) * (3 * func(x + h, y1) - func(x, y0)) 