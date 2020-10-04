import pyxel
import random

pyxel.init(200, 200)
pyxel.cls(7)

for a in range(0, 10):
    x = random.randint(0, 199)
    y = random.randint(0, 199)
    r = random.randint(5, 20)
    c = random.randint(0, 15)
    pyxel.circ(x, y, r, c)
    pyxel.flip()
pyxel.show()
