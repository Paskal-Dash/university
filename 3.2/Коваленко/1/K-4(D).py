class Polynomial():

    def __init__(self, pol):
        self._pol = pol.copy()

    def __add__(self, pol):
        new_pol = []
        x = zip(self._pol, pol._pol)
        for i in x:
            new_pol.append(i[0] + i[1])
        for i in range(min(len(self._pol), len(pol._pol)), max(len(self._pol), len(pol._pol))):
            if max(len(self._pol), len(pol._pol)) == len(self._pol):
                new_pol.append(self._pol[i])
            else:
                new_pol.append(pol._pol[i])    
        return Polynomial(new_pol)

    def __call__(self, x):
        rezult = 0
        for i in range(len(self._pol)):
            rezult += pow(x, i) * self._pol[i]
        return rezult

a = [1,2,3]
p1 = Polynomial(a)
a.append(4)

print(p1(1))
