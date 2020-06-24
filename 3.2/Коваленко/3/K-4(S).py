import re

with open(r'C:\Users\denis\Desktop\Программирование\Коваленко\input.txt', 'r',  encoding='utf-8') as f:
    dic = dict((lambda x: (x[0][:len(x[0])-1], x[1:]))(re.split(r'\W\s', f.readline().rstrip())) for i in range(int(f.readline())))
    rezult = dict()
    count = 0
    for pair in dic.items():
        key = pair[0]
        for word in pair[1]:
            if not word in rezult.keys():
                rezult.update({(word, 0)})
                rezult[word] = [key]
                count += 1
            else:
                arr = rezult[word]
                arr.append(key)
                rezult[word] = arr

    print(count)
    rezult = sorted(rezult.items(), key = lambda x: x[0])
    for arr in rezult:
        print('{} - {}'.format(arr[0], ', '.join(sorted(arr[1]))))