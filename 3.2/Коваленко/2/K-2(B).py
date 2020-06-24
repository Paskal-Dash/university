def simple_map(operation, values):
    rezult = []
    for value in values:
        rezult.append(operation(value))
    return rezult

values = [1, 3, 1, 5, 7]
operation = lambda x: x + 5
print(*simple_map(operation, values))