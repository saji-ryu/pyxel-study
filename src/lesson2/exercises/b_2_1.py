import pyxel

pyxel.init(200, 200)
pyxel.cls(7)
for i in range(0, 110, 10):
    pyxel.line(i, 0, 100 + i, 200, 0)
pyxel.show()
