from graphlib import RGBLED

led = RGBLED(14,15,18)

for i in range(3):
    led.color(int(input("R :"))*0.0039, int(input("G :"))*0.0039, int(input("B :"))*0.0039)