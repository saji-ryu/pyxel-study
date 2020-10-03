import pyxel
import math


pyxel.init(200, 200)
pyxel.cls(14)
lineCounter = 0
distance = 20
for i in range(distance, 210 + distance, distance * 2):
    for j in range(distance, 210, int(distance * math.sqrt(3))):
        for k in range(0, 360, 60):
            kRadian = math.radians(k)
            shortLineLength = int(distance * 2 / 3 * math.sqrt(3))
            if(lineCounter % 2 == 0):
                pyxel.line(i, j, i + shortLineLength * math.sin(kRadian),
                           j + shortLineLength * math.cos(kRadian), 0)
                pyxel.line(i, j, i + distance * math.cos(kRadian),
                           j + distance * math.sin(kRadian), 0)
            else:
                pyxel.line(i - distance, j, i - distance + shortLineLength *
                           math.sin(kRadian), j + shortLineLength * math.cos(kRadian), 0)
                pyxel.line(i - distance, j, i - distance + distance *
                           math.cos(kRadian), j + distance * math.sin(kRadian), 0)
        lineCounter += 1


pyxel.show()
