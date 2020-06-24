from math import exp

def Adams_Bashfort_1(arr, h):
    for i in range(1, int(2/h)):
        arr[i+1][1] = arr[i][1] + h * func(arr[i][0], arr[i][1])
    return arr


def Adams_Bashfort_2(arr, h):
    for i in range(2, int(2/h)):
        arr[i+1][1] = arr[i][1] + h * (3 * func(arr[i][0], arr[i][1]) - func(arr[i-1][0], arr[i-1][1])) / 2
    return arr

def Adams_Bashfort_3(arr, h):
    for i in range(3, int(2/h)):
        arr[i+1][1] = arr[i][1] + h * (23 * func(arr[i][0], arr[i][1]) - 16 * func(arr[i-1][0], arr[i-1][1]) + 5 * func(arr[i-2][0], arr[i-2][1])) / 12
    return arr

def Adams_Bashfort_4(arr, h):
    for i in range(4, int(2/h)):
        arr[i+1][1] = arr[i][1] + h * (55 * func(arr[i][0], arr[i][1]) - 59 * func(arr[i-1][0], arr[i-1][1]) + 37 * func(arr[i-2][0], arr[i-2][1]) - 9 * func(arr[i-3][0], arr[i-3][1])) / 24
    return arr

def func(x, y):
    return x + y

h = 0.1
ans = [[h*i for j in range(2)] for i in range(21)]
ans[0][1], ans[1][1], ans[2][1], ans[3][1] = 1, 1.1103418361512953, 1.2428055163203395, 1.3997176151520065

for x, y in Adams_Bashfort_1(ans, h):
    print('({}; {})'.format(x, y))

print('////////////////////////////////////////')
for x, y in Adams_Bashfort_2(ans, h):
    print('({}; {})'.format(x, y))

print('////////////////////////////////////////')
for x, y in Adams_Bashfort_3(ans, h):
    print('({}; {})'.format(x, y))

print('////////////////////////////////////////')
for x, y in Adams_Bashfort_4(ans, h):
    print('({}; {})'.format(x, y))