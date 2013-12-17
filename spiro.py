#!/usr/bin/python

from math import sin, cos, pi
from PIL import Image, ImageDraw

class gear(object):

    def __init__(self, radius=1, speed=1):
        self.radius = radius
        self.speed = speed
        self.rotation = 0

    def step(self):
        self.rotation += self.speed

    def get_vector(self):
        rads = pi * self.rotation / 360
        x = self.radius * cos(rads)
        y = self.radius * sin(rads)
        return x, y


class Spirograph(object):

    def __init__(self):
        self.spiro = []
        self.size = 0

    def add_gear(self, gear):
        self.spiro.append(gear)
        self.size += gear.radius

    def run(self):
        img_size = self.size * 2 + 20
        img_center = [self.size + 10, self.size + 10]
        img = Image.new("RGB", (img_size, img_size))
        draw = ImageDraw.Draw(img)
        prev = img_center[:]
        prev[0] += self.size
        for i in range(10000):
            new = img_center[:]
            for part in self.spiro:
                part.step()
                vector = part.get_vector()
                new[0] += vector[0]
                new[1] += vector[1]
            draw.line((tuple(prev), tuple(new)), fill=128)
            prev = new[:]
        del draw
        img.save("output.png")


spiro = Spirograph()
spiro.add_gear(gear(radius=160, speed=7))
spiro.add_gear(gear(radius=160, speed=17))
spiro.run()
    



