with open(r'C:\Users\denis\Desktop\Программирование\Коваленко\input.txt', 'r',  encoding='utf-8') as f:

    words = [i.rstrip() for i in f.readlines()]
    rez = [[0 for i in range(2)] for j in range(len(words))]
    step = 0
    for word in words:
        obj = word.upper()
        count = 0
        for j in range(len(word)):
            count += ord(obj[j]) - ord('A') + 1
        rez[step][0] = count
        rez[step][1] = step
        step += 1
    rez.sort(key=lambda x: x[0])

    x = []
    step = 0
    while(step <= len(words)-1):
        if step == len(words)-1:
            x.append(words[rez[step][1]])
            break
        if rez[step][0] < rez[step+1][0]:
            x.append(words[rez[step][1]])
            step += 1
            continue
        else:
            count = step
            y = []
            y.append(words[rez[step][1]])
            while(True):
                if count == len(words)-1:
                    break
                if (rez[step][0] == rez[count + 1][0]):
                    y.append(words[rez[count + 1][1]])
                    count += 1
                else:
                    break
            y.sort()
            for word in y:
                x.append(word)
            step = count + 1

    for word in x:
        print(word)