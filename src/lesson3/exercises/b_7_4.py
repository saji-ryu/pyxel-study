import pyxel

pyxel.init(200, 200)
pyxel.mouse(True)

beginX = -1
beginY = -1
endX = -1
endY = -1
lineStateCounter = 0


def update():
    pass


def draw():
    global beginX
    global beginY
    global endX
    global endY
    global lineStateCounter
    pyxel.cls(7)
    if pyxel.btnp(pyxel.KEY_SPACE):
        if(lineStateCounter == 0 or lineStateCounter == 2):
            beginX = pyxel.mouse_x
            beginY = pyxel.mouse_y
            lineStateCounter = 1
        elif (lineStateCounter == 1):
            endX = pyxel.mouse_x
            endY = pyxel.mouse_y
            lineStateCounter += 1

    if lineStateCounter == 2:
        pyxel.line(beginX, beginY, endX, endY, 0)
    elif lineStateCounter == 1:
        pyxel.line(beginX, beginY, pyxel.mouse_x, pyxel.mouse_y, 0)


pyxel.run(update, draw)
