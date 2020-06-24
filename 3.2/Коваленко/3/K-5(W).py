def Tree(dic, father = None, rezult = {}, count = 0):
    if father == None:
        for key, item in dic.items():
            rezult[key] = Tree(dic, item, rezult, 1)[1]
        return sorted(rezult.items()), count
    else:
        if father in rezult.keys():
            return rezult, rezult[father] + count
        elif father in dic.keys():
            return Tree(dic, dic[father], rezult, count + 1)
        else:
            rezult[father] = 0
            return rezult, count
    

with open('input.txt', 'r',  encoding='utf-8') as f:
    dic = dict()
    rezult = dict()
    for _ in range(int(f.readline())-1):
        child, father = f.readline().split()
        dic[child] = father
            
    rezult = Tree(dic)[0]

    for arr in rezult:
       print('{} {}'.format(arr[0], arr[1]))
        