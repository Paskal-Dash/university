def sorted2(data, key=None):
    rezult = []
    if key != None:
        for i in data:
            rezult.append(sorted(i, key=key))
    else:
        for i in data:
            rezult.append(sorted(i, reverse=True))
    return sorted(rezult, key = lambda x: key(x[-1]))

data = [[6, 5, 4], [3, 2], [1]]
key = lambda x: x
print(sorted2(data, key=key))