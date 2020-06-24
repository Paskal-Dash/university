class Balance():

    def __init__(self):
        self._weight_right = 0
        self._weight_left = 0

    def add_right(self, weight):
        self._weight_right += weight

    def add_left(self, weight):
        self._weight_left += weight

    def result(self):
        if self._weight_left == self._weight_right:
            return "="
        elif self._weight_left > self._weight_right:
            return "L"
        else:
            return "R"

balance = Balance()
balance.add_right(10)
balance.add_left(9)
balance.add_left(2)
print(balance.result())