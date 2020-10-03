import pyxel

pyxel.init(200, 200)
pyxel.cls(7)
for i in range(0, 210, 10):
    pyxel.line(i, 0, 0, 200 - i, 0)
pyxel.show()
