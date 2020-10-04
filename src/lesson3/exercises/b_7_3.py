import pyxel

pyxel.init(200, 200)
pyxel.mouse(True)

beginX = -1
beginY = -1
endX = -1
endY = -1


def update():
    pass


def draw():
    global beginX
    global beginY
    global endX
    global endY
    pyxel.cls(7)
    if pyxel.btnp(pyxel.KEY_SPACE):
        endX = -1
        endY = -1
        beginX = pyxel.mouse_x
        beginY = pyxel.mouse_y
    if pyxel.btn(pyxel.KEY_SPACE):
        pyxel.line(beginX, beginY, pyxel.mouse_x, pyxel.mouse_y, 0)
    if pyxel.btnr(pyxel.KEY_SPACE):
        endX = pyxel.mouse_x
        endY = pyxel.mouse_y
    if beginX >= 0 and beginY >= 0 and endX >= 0 and endY >= 0:
        pyxel.line(beginX, beginY, endX, endY, 0)


pyxel.run(update, draw)
