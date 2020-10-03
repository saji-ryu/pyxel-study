import pyxel

pyxel.init(200, 200)
pyxel.cls(7)
for i in range(0, 210, 10):
    for j in range(0, 210, 10):
        if((i + j) % 20 == 0):
            pyxel.rect(i, j, 10, 10, 3)
        else:
            pyxel.rect(i, j, 10, 10, 0)

pyxel.show()
