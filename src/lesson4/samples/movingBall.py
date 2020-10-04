import pyxel
import math

pyxel.init(200, 200)

ballx = 0
bally = 0
angle = math.radians(60)
vx = math.cos(angle)
vy = math.sin(angle)


def update():
    global ballx, bally, angle, vx, vy
    ballx += vx
    bally += vy
    if bally >= 200:
        ballx = 0
        bally = 0


def draw():
    global ballx, bally, angle, vx, vy
    pyxel.cls(7)
    pyxel.circ(ballx, bally, 10, 6)


pyxel.run(update, draw)
