import pygame
import random
import math

SCREEN_DIM = (800, 600)


class Vec2d:
    def __init__(self, x=0., y=0.):
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

    def __str__(self):
        return f'{self.x}, {self.y}'

    def length(self):
        return ((self.x * self.x) + (self.y * self.y)) ** 0.5

    def int_pair(self):
        """Возвращает текущие координаты вектора"""
        return self.x, self.y


class Polyline:
    def __init__(self):
        self.points = []
        self.speeds = []

    def set_point(self, vector: Vec2d, speed: Vec2d):
        """
        Добавляет в ломанную точку
        :param vector: координаты точки
        :param speed: скорость точки
        """
        self.points.append(vector)
        self.speeds.append(speed)

    def set_points(self):
        for p in range(len(self.points)):
            self.points[p] = self.points[p] + self.speeds[p]
            if self.points[p].x > SCREEN_DIM[0] or self.points[p].x < 0:
                self.speeds[p].x = -self.speeds[p].x
            if self.points[p].y > SCREEN_DIM[1] or self.points[p].y < 0:
                self.speeds[p].y = -self.speeds[p].y

    def draw_points(self, width=3, color=(255, 255, 255)):
        for p in self.points:
            pygame.draw.circle(gameDisplay, color,
                               (int(p.x), int(p.y)), width)


def __init__(self, points, count=35):
    super().__init__()
    self.points = points
    self.count = count


def get_point(self, points, alpha, deg=None):
    if deg is None:
        deg = len(points) - 1
    if deg == 0:
        return points[0]
    return points[deg] * alpha + self.get_point(points, alpha, deg - 1) * (1 - alpha)


def get_points(self, base_points, count):
    alpha = 1 / count
    res = []
    for i in range(count):
        res.append(self.get_point(base_points, i * alpha))
    return res


def get_knot(self):
    if len(self.points) < 3:
        return []
    res = []
    for i in range(-2, len(self.points) - 2):
        ptn = []
        ptn.append((self.points[i] + self.points[i + 1]) * 0.5)
        ptn.append(self.points[i + 1])
        ptn.append((self.points[i + 1] + self.points[i + 2]) * 0.5)
        res.extend(self.get_points(ptn, self.count))
    return res

    def draw_knot(self, res, width=3, color=(255, 255, 255)):
        for p_n in range(-1, len(res) - 1):
            pygame.draw.line(gameDisplay, color, (int(res[p_n].x), int(res[p_n].y)),
                             (int(res[p_n + 1].x), int(res[p_n + 1].y)), width)

    def set_point(self, vector: Vec2d, speed: Vec2d):
        super(Knot, self).set_point(vector, speed)
        self.get_knot()

    def set_points(self):
        super(Knot, self).set_points()
        self.get_knot()


if __name__ == "__main__":
    pygame.init()
    gameDisplay = pygame.display.set_mode(SCREEN_DIM)
    pygame.display.set_caption("MyScreenSaver")

    working = True
    pause = True
    knot = Knot()

    hue = 0
    colors = pygame.Color(0)

    while working:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                working = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    working = False
                if event.key == pygame.K_p or event.key == pygame.K_SPACE:
                    pause = not pause
                if event.key == pygame.K_r:
                    knot.points = []
                    knot.speeds = []
                    knot.res = []

            if event.type == pygame.MOUSEBUTTONDOWN:
                point = Vec2d()
                point.x = event.pos[0]
                point.y = event.pos[1]
                speeds = Vec2d(random.random() * 2, random.random() * 2)
                knot.set_point(point, speeds)

        gameDisplay.fill((0, 0, 0))
        hue = (hue + 0.05) % 360
        colors.hsla = (hue, 100, 50, 100)
        knot.draw_points()

        if not pause:
            knot.set_points()

        knot.draw_knot(knot.get_knot(), color=colors)
        pygame.display.flip()

    pygame.display.quit()
    pygame.quit()
    exit(0)
