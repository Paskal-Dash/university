with open(r'C:\Users\denis\Desktop\Программирование\Коваленко\input.txt', 'r',  encoding='utf-8') as f:
    dic = dict()
    for word in f.read().split():
        dic[word] = dic.get(word, 0) + 1
    
    rezult = dict(sorted(sorted(dic.items(), key = lambda x: x[0]), key = lambda x: x[1], reverse=True))
    print("\n".join(rezult.keys()))