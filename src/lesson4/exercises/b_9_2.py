import pyxel
import math
import random


pyxel.init(200, 200)

ballx = random.randint(0, 199)
bally = 0
angle = math.radians(random.randint(30, 150))
vx = math.cos(angle)
vy = math.sin(angle)
speed = 1
padx = 100
score = 0
catchSucceed = False

pyxel.sound(0).set(
    "b3g3",
    "t",
    "7",
    "n",
    20,
)
pyxel.sound(1).set(
    "c1c1",
    "t",
    "7",
    "n",
    20,
)


def update():
    global ballx, bally, angle, vx, vy, padx, speed, score, catchSucceed
    ballx += vx * speed
    bally += vy * speed
    if ballx >= 200 or ballx <= 0:
        vx *= -1
    if bally >= 195 and ballx > padx - 20 and ballx < padx + 20:
        catchSucceed = True
    if bally >= 200:
        if catchSucceed:
            score += 1
            catchSucceed = False
            pyxel.play(0, 0)
        else:
            pyxel.play(0, 1)
        bally = 0
        speed += 1
        angle = math.radians(random.randint(5, 90))
        vx = math.cos(angle)
        vy = math.sin(angle)
        ballx = random.randint(0, 199)
    padx = pyxel.mouse_x


def draw():
    global ballx, bally, angle, vx, vy, padx, score
    pyxel.cls(7)
    pyxel.text(5, 5, "score : " + str(score), 0)
    pyxel.circ(ballx, bally, 10, 6)
    pyxel.rect(padx - 20, 195, 40, 5, 14)


pyxel.run(update, draw)
