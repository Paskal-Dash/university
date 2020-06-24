from math import exp

def Adams_Moulton_1(arr, h):
    for i in range(0, int(2/h)):
        arr[i+1][1] = arr[i][1] + h * func(arr[i+1][0], IEM(arr[i][0], arr[i][1], h))
    return arr


def Adams_Moulton_2(arr, h):
    for i in range(1, int(2/h)):
        arr[i+1][1] = arr[i][1] + h * (func(arr[i+1][0], IEM(arr[i][0], arr[i][1], h)) + func(arr[i][0], arr[i][1])) / 2
    return arr

def Adams_Moulton_3(arr, h):
    for i in range(2, int(2/h)):
        arr[i+1][1] = arr[i][1] + h * (5 * func(arr[i+1][0], IEM(arr[i][0], arr[i][1], h)) + 8 * func(arr[i][0], arr[i][1]) - func(arr[i-1][0], arr[i-1][1])) / 12
    return arr

def Adams_Moulton_4(arr, h):
    for i in range(3, int(2/h)):
        arr[i+1][1] = arr[i][1] + h * (9 * func(arr[i+1][0], IEM(arr[i][0], arr[i][1], h)) + 19 * func(arr[i][0], arr[i][1]) - 5 * func(arr[i-1][0], arr[i-1][1]) + func(arr[i-2][0], arr[i-2][1])) / 24
    return arr

def func(x, y):
    return x + y

def IEM(x, y, h):
    return y + h * func(x, y)

h = 0.1
ans = [[h*i for j in range(2)] for i in range(21)]
ans[0][1], ans[1][1], ans[2][1], ans[3][1] = 1, 1.1103418361512953, 1.2428055163203395, 1.3997176151520065

for x, y in Adams_Moulton_1(ans, h):
    print('({}; {})'.format(x, y))

print('////////////////////////////////////////')
for x, y in Adams_Moulton_2(ans, h):
    print('({}; {})'.format(x, y))

print('////////////////////////////////////////')
for x, y in Adams_Moulton_3(ans, h):
    print('({}; {})'.format(x, y))

print('////////////////////////////////////////')
for x, y in Adams_Moulton_4(ans, h):
    print('({}; {})'.format(x, y))