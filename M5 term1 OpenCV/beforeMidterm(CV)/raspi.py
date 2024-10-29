import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(17, GPIO.OUT) #change pins here
GPIO.setup(27, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(6, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)

GPIO_TRIGGER = 18
GPIO_ECHO = 24

GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

GPIO.output(GPIO_TRIGGER, False)
time.sleep(1)

GPIO.output(GPIO_TRIGGER, True)
time.sleep(0.00001)
GPIO.output(GPIO_TRIGGER, False)

while GPIO.input(GPIO_ECHO) == 0:
    stpulse = time.time()

while GPIO.input(GPIO_ECHO) == 1:
    enpulse = time.time()

duration = enpulse - stpulse
distance = duration * 17150
distance = round(distance, 2)
distance = round(distance, 2)
 

setoflight = [17, 27, 22, 23, 5, 6, 13, 19] #change pins here
if distance >= 5 and distance <= 20:
    count = 0
    for i in setoflight:
        count += 1
        GPIO.output(i, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(i, GPIO.LOW)
        time.sleep(0.5)
        if count == 5:
            break

elif distance >= 21 and distance <= 50:
    for i,e in setoflight,reversed(setoflight):
        GPIO.output(i, GPIO.HIGH)
        GPIO.output(e, GPIO.LOW)
        time.sleep(1)
        GPIO.output(i, GPIO.LOW)
        GPIO.output(e, GPIO.HIGH)
        time.sleep(1)

elif distance >= 51 and distance <= 100:
    oddsetoflight = [17, 22, 5, 13] #change pins here
    evensetoflight = [27, 23, 6, 19] #change pins here
    for i,e in oddsetoflight,evensetoflight:
        GPIO.output(i, GPIO.HIGH)
        GPIO.output(e, GPIO.LOW)
        time.sleep(1)
        GPIO.output(e, GPIO.HIGH)
        GPIO.output(i, GPIO.LOW)
        time.sleep(1)

elif distance >= 101 and distance <= 150:
    for i in setoflight:
        GPIO.output(i, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(i, GPIO.LOW)
        time.sleep(0.5)

elif distance >= 151 :
    for i in setoflight:
        GPIO.output(i, GPIO.LOW)