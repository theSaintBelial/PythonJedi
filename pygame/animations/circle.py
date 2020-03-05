
import pygame

class Circle:
    def __init__(self, rad):
        self.rad = rad
        print("Ball rad {} has been created!".format(self.rad))

    def position(self, x, y):
        self.x = x
        self.y = y
        print("Ball with rad {} is in ({}, {}) position.".format(self.rad, self.x, self.y))

    def direction(self, dx, dy):
        self.dx = dx
        self.dy = dy
        print("Ball with rad {} has ({}, {}) direction.".format(self.rad, self.dx, self.dy))

    def __del__(self):
        print("Ball with rad {} has been deleted!".format(self.rad))