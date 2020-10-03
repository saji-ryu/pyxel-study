import pyxel
import math

pyxel.init(200, 200)
pyxel.cls(7)
for i in range(0, 360, 1):
    iRadian = math.radians(i)
    if(i <= 90):
        pyxel.line(120, 80, 100 + 100 * math.cos(iRadian),
                   100 - 100 * math.sin(iRadian), 0)
    elif(i <= 180):
        pyxel.line(80, 80, 100 + 100 * math.cos(iRadian),
                   100 - 100 * math.sin(iRadian), 0)
    elif(i <= 270):
        pyxel.line(80, 120, 100 + 100 * math.cos(iRadian),
                   100 - 100 * math.sin(iRadian), 0)
    else:
        pyxel.line(120, 120, 100 + 100 * math.cos(iRadian),
                   100 - 100 * math.sin(iRadian), 0)
pyxel.show()
