def fms():
    return sum(list(map(lambda x: x ** 2, filter(lambda x: x % 9 == 0, range(10, 100)))))

print(fms())
