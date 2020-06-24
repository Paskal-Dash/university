n = int(input())
files = dict((lambda x: (x[0], x[1:]))(input().split()) for _ in range(n))
delta = {'execute': 'X', 'read': 'R', 'write': 'W'}
for i in range(int(input())):
    obj = input().split()
    if any(delta[obj[0]] == file1 for file1 in files[obj[1]]):
        print('OK')
    else:
        print('Access denied') 