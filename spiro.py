#!/usr/bin/python

from math import sin, cos, pi
from PIL import Image, ImageDraw

class line(object):

    def __init__(self, direction=1, length=1, speed=1):
        self.direction = direction
        self.length = length
        self.speed = speed
        self.rotation = 0

    def step(self):
        self.rotation += direction * speed

    def delta(self):
        rads = pi * self.rotation / 360
        x = length * cos(rads)
        y = length * sin(rads)
        return x, y

spiro = []
spiro.append(line(length=100))
spiro.append(line(length=40, speed=10))
spiro.append(line(length=30))

spirolen = 0
for i in spiro:
    spirolen += i.length

size = spirolen * 2 + 20
center = spirolen + 10, spirolen + 10

im = Image.new("RGB", (size, size))
draw = ImageDraw.Draw(im)
prev = center + spirolen
for i in range(1000):
    new = center
    for part in spiro:
        part.step()
        delta = part.delta()
        new[0] += delta[0]
        new[1] += delta[1]
    draw.line(prev, new, fill=128)
    prev = new[:]
del draw
im.save("output.png")
    



