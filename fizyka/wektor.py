class Wektor:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "(%d,%d)" % (self.x, self.y)

    def dodajWektor(self, v):
        self.x += v.x
        self.y += v.y
