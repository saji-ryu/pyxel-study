import pyxel

pyxel.init(200, 200)
pyxel.cls(7)
for i in range(0, 201, 20):
    for j in range(0, 201, 20):
        pyxel.line(i, 0, j, 200, 0)
pyxel.show()
