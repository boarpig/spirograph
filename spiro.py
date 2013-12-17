#!/usr/bin/python

from math import sin, cos, pi
from PIL import Image, ImageDraw

class line(object):

    def __init__(self, length=1, speed=1):
        self.length = length
        self.speed = speed
        self.rotation = 0

    def step(self):
        self.rotation += self.speed

    def get_vector(self):
        rads = pi * self.rotation / 360
        x = self.length * cos(rads)
        y = self.length * sin(rads)
        return x, y

spiro = []
spiro.append(line(length=100, speed=7))
spiro.append(line(length=40, speed=17))

spirolen = 0
for i in spiro:
    spirolen += i.length

size = spirolen * 2 + 20
center = [spirolen + 10, spirolen + 10]

im = Image.new("RGB", (size, size))
draw = ImageDraw.Draw(im)
prev = center[:]
prev[0] += spirolen
for i in range(10000):
    new = center[:]
    for part in spiro:
        part.step()
        vector = part.get_vector()
        new[0] += vector[0]
        new[1] += vector[1]
    draw.line((tuple(prev), tuple(new)), fill=128)
    prev = new[:]
del draw
im.save("output.png")
    



