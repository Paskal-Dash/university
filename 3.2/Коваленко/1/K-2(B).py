class MyVector():

    def __init__(self, x, y):
        self._x = x
        self._y = y

    def __add__(self, vector):
        new_vector_x = self._x + vector._x
        new_vector_y = self._y + vector._y
        return MyVector(new_vector_x, new_vector_y)

    def __sub__(self, vector):
        new_vector_x = self._x - vector._x
        new_vector_y = self._y - vector._y
        return MyVector(new_vector_x, new_vector_y)

    def __mul__(self, numb):
        new_vector_x = self._x * numb
        new_vector_y = self._y * numb
        return MyVector(new_vector_x, new_vector_y)

    def __rmul__(self, numb):
        new_vector_x = self._x * numb
        new_vector_y = self._y * numb
        return MyVector(new_vector_x, new_vector_y)

    def __str__(self):
        return 'MyVector({}, {})'.format(self._x, self._y)
    
    def __eq__(self, vector):
        return self._x == vector._x and self._y == vector._y

    def __ne__(self, vector):
        return self._x != vector._x or self._y != vector._y

    def __len__(self):
        return int(pow(pow(self._x, 2) + pow(self._y, 2), 1/2))

v1 = MyVector(-2, 5)
v2 = MyVector(3, -4)
print(len(v1))