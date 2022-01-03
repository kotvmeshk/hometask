class road:
    def __init__(self, length, width):
        self._length = length
        self._width = width
        self.m_gost = 25
        self.high = 5
    def massa(self):
        m = self._length*self._width*self.m_gost*self.high/1000
        print( m)

r = road(2000,50)
r.massa()