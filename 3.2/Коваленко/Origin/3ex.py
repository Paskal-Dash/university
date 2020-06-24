with open(r'C:\Users\denis\Desktop\Программирование\Коваленко\input.txt', 'r',  encoding='utf-8') as f:

    n = int(f.readline())
    words = [i.rstrip().lower() for i in f.readlines()]
    mas = [True for i in range(n)]

    rez = []

    for i in range(n):
        if mas[i]:
            a = sorted(words[i])
            y = []
            y.append(words[i])
            for j in range(i+1, n):
                b = sorted(words[j])
                if a == b:
                    y.append(words[j])
                    mas[j] = False
            rez.append(y)

    rez.sort()

    for massive in rez:
        massive.sort()
        print(' '.join(massive))