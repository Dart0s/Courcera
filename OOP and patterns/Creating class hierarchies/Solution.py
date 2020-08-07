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
        return [vec.x - self.x, vec.y - self.y]


class Polyline:
    pass


class Knot(Polyline):
    pass


if __name__ == "__main__":
    pass
