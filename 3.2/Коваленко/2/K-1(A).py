with open(r'C:\Users\denis\Desktop\Коваленко\input.txt', 'r',  encoding='utf-8') as f:
    n = int(f.readline())
    flag = 1
    for i in range(n):
        if not all('0' != obj.rstrip().split()[1] for obj in [f.readline() for i in range(int(f.readline()))]):
            flag = 0
            break
    if flag: print('YES')
    else: print('NO')