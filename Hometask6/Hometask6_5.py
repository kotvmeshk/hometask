class Stationery:
    def __init__(self, title):
        self.title = title
    def draw(self):
        return f'запущена отрисовка'

class Pen (Stationery):
    def __init__(self, title):
        super().__init__( title)
    def draw(self):
        return f'запущена отрисовка {self.title}'

class Pencil (Stationery):
    def __init__(self, title):
        super().__init__( title)
    def draw(self):
        return f'запущена отрисовка {self.title}'

class Handle (Stationery):
    def __init__(self, title):
        super().__init__( title)
    def draw(self):
        return f'запущена отрисовка {self.title}'

a = Pen ('pen')
print (a.draw())

b = Pencil ('green pencil')
print (b.draw())

c = Handle ('red handle')
print (c.draw())

