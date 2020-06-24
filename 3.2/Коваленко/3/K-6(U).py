with open(r'C:\Users\denis\Desktop\Программирование\Коваленко\input.txt', 'r',  encoding='utf-8') as f:
    dic = dict()
    for string in f.readlines():
        name, product, count = string.split()
        if not name in dic.keys():
            dic[name] = {}
        if not product in dic[name].keys():
            dic[name][product] = str(count)
        else:
            dic[name][product] = str(int(dic[name][product]) + int(count))
    
    for lists in sorted(dic.items(), key=lambda x: x[0]):
        print('{}:'.format(lists[0]))
        for arr in sorted(lists[1].items(), key=lambda x: x[0]):
            print(' '.join(arr))
    