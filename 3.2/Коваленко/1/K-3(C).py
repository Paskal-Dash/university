class BaseObject():

    def __init__(self, x, y, z):
        self._x = x
        self._y = y
        self._z = z
    
    def get_coordintates(self):
        return list(self._x, self._y, self._z)

class Block(BaseObject):

    def shatter(self):
        self._x = None
        self._y = None
        self._z = None

class Entity(BaseObject):

    def move(self, x, y, z):
        self._x = x
        self._y = y
        self._z = z

class Thing(BaseObject):
    pass
