import pyxel

pyxel.init(200, 200)
pyxel.mouse(True)

memoryX = -1
memoryY = -1


def update():
    pass


def draw():
    global memoryX
    global memoryY
    pyxel.cls(7)
    if pyxel.btn(pyxel.KEY_SPACE):
        memoryX = -1
        memoryY = -1
        pyxel.line(0, 0, pyxel.mouse_x, pyxel.mouse_y, 0)
    if pyxel.btnr(pyxel.KEY_SPACE):
        memoryX = pyxel.mouse_x
        memoryY = pyxel.mouse_y
    if memoryX >= 0 and memoryY >= 0:
        pyxel.line(0, 0, memoryX, memoryY, 0)


pyxel.run(update, draw)
