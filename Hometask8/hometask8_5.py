class CompNum:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return f'Сумма равна: {self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        return f'Произведение равно: {self.a * other.a - (self.b * other.b)} + {self.a * other.b} * i'


com_1 = CompNum(4, -8)
com_2 = CompNum(6, 11)
print(com_1 + com_2)
print(com_1 * com_2)

# hfhdh