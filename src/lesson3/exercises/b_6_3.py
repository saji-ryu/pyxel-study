import pyxel

pyxel.init(200, 200)

vx1 = 1
vy1 = 1
x1 = 0
y1 = 0


def update():
    global vx1
    global vy1
    global x1
    global y1
    if (x1 > 200):
        vx1 = -1
    if(x1 < 0):
        vx1 = 1
    if (y1 > 200):
        vy1 = -1
    if(y1 < 0):
        vy1 = 1
    x1 += vx1
    y1 += vy1


def draw():
    global x1
    global y1
    pyxel.cls(7)
    pyxel.circ(x1, y1, 10, 0)


pyxel.run(update, draw)
