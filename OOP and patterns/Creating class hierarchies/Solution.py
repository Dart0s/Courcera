import pygame
import random
import math

SCREEN_DIM = (800, 600)


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

    def int_pair(self, vec):
        """Возвращает текущие координаты вектора"""
        return [vec.x - self.x, vec.y - self.y]


class Polyline:
    def __init__(self):
        self.points = []
        self.speeds = []

    def get_point(self, x, y, speed):
        """Добавляем точку в ломанную"""
        self.points.append([x, y])
        self.speeds.append(speed)
        return self

    def set_points(self):
        """функция перерасчета координат опорных точек"""
        for p in range(len(self.points)):
            self.points[p] = self.points[p] + self.speeds[p]
                if self.points[p][0] > SCREEN_DIM[0] or self.points[p][0] < 0:
                self.speeds[p] = (-self.speeds[p][0], self.speeds[p][1])
            if self.points[p][1] > SCREEN_DIM[1] or self.points[p][1] < 0:
                self.speeds[p] = (self.speeds[p][0], -self.speeds[p][1])

    def draw_points(self, style='points', width=3, color=(255, 255, 255)):
        """функция отрисовки точек на экране"""
        if style == 'line':
            for p_n in range(-1, len(self.points) - 1):
                pygame.draw.line(gameDisplay, color, (int(self.points[p_n][0]), int(self.points[p_n][1])),
                             (int(self.points[p_n + 1][0]), int(self.points[p_n + 1][1])), width)
        elif style == 'point':
            for p in self.points:
                pygame.draw.circle(gameDisplay, color, (int(p[0]), int(p[1])), width))


class Knot(Polyline):
    def get_knot(self):
        pass

    def get_point(self, x, y, speed):
        super().get_point(x, y, speed)
        self.get_knot()

    def set_points(self):
        super().set_points()
        self.get_knot()


if __name__ == "__main__":
    pass
