X = [0, 0.2, 0.4, 0.6, 0.8, 1]

r = lambda x: -15 / (x+1)**(1/2)
q = lambda x: -3 / (x+1)**2
 
k = len(X)-2

b = [0] * k
a, c = [0.5] * k, [0.5] * k
f = [0] * k
h = 0.2

for i in range(1, len(X)-1):
    b[i-1] = (-2 + h**2 * q(X[i]))
    f[i-1] = (h**2 * r(X[i]))


print(b)
print(f)
M = []

u = [0.2996, 0.8848, 1.2956, 1.2786, 0.8472, 0.4939]


for i in range(k+2):
    M.append(r(X[i]) - u[i]*q(X[i]))
