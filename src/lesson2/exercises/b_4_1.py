import pyxel

pyxel.init(200, 200)
pyxel.cls(7)
for i in range(10, 200, 20):
    for j in range(10, 200, 20):
        if ((j + i) / 20) % 2 == 0:
            pyxel.circ(j, i, 10, 14)
        else:
            pyxel.circ(j, i, 10, 6)
pyxel.show()
