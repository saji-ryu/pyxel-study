import pyxel
import math

pyxel.init(200, 200)
pyxel.cls(7)
for i in range(0, 360, 1):
    iRadian = math.radians(i)
    lineColor = int(i * 7 / 360)
    pyxel.line(100, 100, 100 + 100 * math.sin(iRadian * 2),
               100 + 100 * math.cos(iRadian * 3), lineColor)
pyxel.show()
