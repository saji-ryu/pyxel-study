import pyxel
import math

pyxel.init(200, 200)
pyxel.cls(7)
for a in range(0, 360, 10):
    b = math.radians(a)
    pyxel.line(100, 100, 100 + 100 * math.sin(b), 100 + 100 * math.cos(b), 0)
pyxel.show()
