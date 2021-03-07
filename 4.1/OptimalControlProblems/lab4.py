#Optional 10

CONST = -1
R, N, n= 4600, 10, 5            # R - equipment price

t0 = N % 4

c0, q0 = 3, 7


c = 1 + 0.1 * c0
q = 1 + 0.1 * q0

r = lambda x: 600 * c**x        # Operating costs
p = lambda x: 2500 * c**(-x)    # Operating income
S = lambda x: R * q**(-x)       # Sale price after operation

#EX 1  -  Minimal costs

def min_costs():
    #           { r(t) + Z[k+1](t), if equipment saved
    # Z[k] = min{                                                , k = 1, 2, 3, 4
    #           { R+r(0) - S(t) + Z[k+1](0), if  equipment sold

    Z = [CONST] * (n-1)
    Z.append([(-1)*S(t) for t in range(1, n+t0+1)])

    steps = {}

    for k in range(n-1, 1, -1):
        z = [CONST] * (n+t0)
        for t in range(1, k):
            min1 = r(t) + Z[k][t]
            min2 = R + r(0) - S(t) + Z[k][0]

            steps['({}, {})'.format(str(k), str(t))], z[t-1] = ('({}, {})'.format(str(k+1), str(t+1)), min1) if min1 <= min2 else ('({}, {})'.format(str(k+1), str(1)), min2)

        min1 = r(k+t0) + Z[k][k+t0]
        min2 = R + r(0) - S(k+t0) + Z[k][0]
        steps['({}, {})'.format(str(k), str(k+t0))], z[k+t0-1] = ('({}, {})'.format(str(k+1), str(k+t0+1)), min1) if min1 <= min2 else ('({}, {})'.format(str(k+1), str(1)), min2)

        Z[k-1] = z

    z = [CONST] * (n+t0)
    min1 = r(t0+1) + Z[1][t0+1]
    min2 = R + r(0) - S(t0+1) + Z[1][0]
    steps['({}, {})'.format(str(1), str(t0+1))], z[t0] = ('({}, {})'.format(str(2), str(t0+2)), min1) if min1 <= min2 else ('({}, {})'.format(str(2), str(1)), min2)

    Z[0] = z

    rez = ["(0, 0)", "(1, {})".format(t0+1)]
    for _ in range(1, n):
        rez.append(steps[rez[-1]])

    return S(t0)+Z[0][t0], rez, Z



#EX.2  -  Maximal income

def max_income():
    #           { p(t) + Z[k+1](t), if equipment saved
    # Z[k] = max{                                                   , k = 1, 2, 3, 4
    #           { S(t) + p(0) - R + Z[k+1](0), if  equipment sold

    Z = [CONST] * (n-1)
    Z.append([S(t) for t in range(1, n+t0+1)])

    steps = {}

    for k in range(n-1, 1, -1):
        z = [CONST] * (n+t0)
        for t in range(1, k):
            max1 = p(t) + Z[k][t]
            max2 = S(t) + p(0) - R + Z[k][0]

            steps['({}, {})'.format(str(k), str(t))], z[t-1] = ('({}, {})'.format(str(k+1), str(t+1)), max1) if max1 > max2 else ('({}, {})'.format(str(k+1), str(1)), max2)

        max1 = p(k+t0) + Z[k][k+t0]
        max2 = S(k+t0) + p(0) - R + Z[k][0]
        steps['({}, {})'.format(str(k), str(k+t0))], z[k+t0-1] = ('({}, {})'.format(str(k+1), str(k+t0+1)), max1) if max1 > max2 else ('({}, {})'.format(str(k+1), str(1)), max2)

        Z[k-1] = z

    z = [CONST] * (n+t0)
    max1 = p(t0+1) + Z[1][t0+1]
    max2 = S(t0+1) + p(0) - R + Z[1][0]
    steps['({}, {})'.format(str(1), str(t0+1))], z[t0] = ('({}, {})'.format(str(2), str(t0+2)), max1) if max1 > max2 else ('({}, {})'.format(str(2), str(1)), max2)

    Z[0] = z

    rez = ["(0, 0)", "(1, {})".format(t0+1)]
    for _ in range(1, n):
        rez.append(steps[rez[-1]])

    return Z[0][t0]-S(t0), rez, Z


#EX.3 - Maximum benefit

def max_benefit():
    #           { p(t) - r(t) + Z[k+1](t), if equipment saved
    # Z[k] = max{                                                           , k = 1, 2, 3, 4
    #           { S(t) + p(0) - (R + r(0)) + Z[k+1](0), if  equipment sold

    Z = [CONST] * (n-1)
    Z.append([S(t) for t in range(1, n+t0+1)])

    steps = {}

    for k in range(n-1, 1, -1):
        z = [CONST] * (n+t0)
        for t in range(1, k):
            max1 = p(t) - r(t) + Z[k][t]
            max2 = S(t) + p(0) - (R + r(0)) + Z[k][0]

            steps['({}, {})'.format(str(k), str(t))], z[t-1] = ('({}, {})'.format(str(k+1), str(t+1)), max1) if max1 > max2 else ('({}, {})'.format(str(k+1), str(1)), max2)

        max1 = p(k+t0) - r(k+t0) + Z[k][k+t0]
        max2 = S(k+t0) + p(0) - (R + r(0)) + Z[k][0]
        steps['({}, {})'.format(str(k), str(k+t0))], z[k+t0-1] = ('({}, {})'.format(str(k+1), str(k+t0+1)), max1) if max1 > max2 else ('({}, {})'.format(str(k+1), str(1)), max2)

        Z[k-1] = z

    z = [CONST] * (n+t0)
    max1 = p(t0+1) - r(t0+1) + Z[1][t0+1]
    max2 = S(t0+1) + p(0) - (R + r(0)) + Z[1][0]
    steps['({}, {})'.format(str(1), str(t0+1))], z[t0] = ('({}, {})'.format(str(2), str(t0+2)), max1) if max1 > max2 else ('({}, {})'.format(str(2), str(1)), max2)

    Z[0] = z

    rez = ["(0, 0)", "(1, {})".format(t0+1)]
    for _ in range(1, n):
        rez.append(steps[rez[-1]])

    return Z[0][t0] - S(t0), rez, Z


#1 cost, steps, Z = min_costs()
#2 cost, steps, Z = max_income()
cost, steps, Z = max_benefit()
print(cost, '\n\n', steps, '\n\n', Z)
