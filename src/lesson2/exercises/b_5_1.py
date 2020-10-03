import pyxel

pyxel.init(200, 200)
pyxel.cls(7)
for i in range(10, 200, 20):
    for j in range(10, 200, 20):
        if (j + i) <= 100:
            pyxel.circ(j, i, 10, 2)
        elif(j + i) <= 200:
            pyxel.circ(j, i, 10, 3)
        elif(j + i) <= 300:
            pyxel.circ(j, i, 10, 6)
        else:
            pyxel.circ(j, i, 10, 14)
pyxel.show()
