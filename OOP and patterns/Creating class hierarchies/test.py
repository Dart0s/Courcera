class Vec2d:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, vec):
        """возвращает сумму двух векторов"""
        return Vec2d(self.x + vec.x, self.y + vec.y)

    def __sub__(self, vec):
        """"возвращает разность двух векторов"""
        return Vec2d(self.x - vec.x, self.y - vec.y)

    def __mul__(self, k):
        """возвращает произведение вектора на число"""
        self.x *= k
        self.y *= k
        return self

    def length(self):
        return ((self.x * self.x) + (self.y * self.y)) ** 0.5



if __name__ == '__main__':
    a = Vec2d(1, 3)
    print(f'ax={a.x}, ay={a.y}')
    b = Vec2d(1, 4)
    print(f'bx={b.x}, ay={b.y}')
    a = a + b
    print(f'ax={a.x}, ay={a.y}')
    a = a * 10
    print(f'ax={a.x}, ay={a.y}')
    print(a.length())
