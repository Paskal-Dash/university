def list_of_turns(cell):
    up_cell = ((ord(cell[0]) - ord('A') + 1), int(cell[1]))
    delta = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]
    rezult = []
    for i in range(8):
        x = (up_cell[0] + delta[i][0], up_cell[1] + delta[i][1])
        if onboard(x):
            rezult.append('{}{}'.format(chr(x[0] - 1 + ord('A')), x[1]))
    
    return rezult


def onboard(x):
    return 1 <= x[0] <= 8 and 1 <= x[1] <= 8
    

print(list_of_turns('E4'))
