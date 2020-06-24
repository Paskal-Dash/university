with open(r'C:\Users\denis\Desktop\Программирование\Коваленко\input.txt', 'r',  encoding='utf-8') as f:
    dic = dict()
    for _ in range(int(f.readline())):
        cities = f.readline().split()
        for j in range(1, len(cities)): dic.update({(cities[j], cities[0])})
    n = f.readline()
    for city in f.read().split():
        print(dic[city])
