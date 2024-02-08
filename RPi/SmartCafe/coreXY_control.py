import RPi.GPIO as GPIO
from RpiMotorLib import RpiMotorLib
import time
from threading import Thread

D1= 22 # Direction (DIR) GPIO Pin
S1 = 23 # Step GPIO Pin
E1 = 24 # enable pin (LOW to enable)

D2 = 12
S2 = 5
E2 = 6

# Declare a instance of class pass GPIO pins numbers and the motor type
mymotortest1 = RpiMotorLib.A4988Nema(D1, S1, (21,21,21), "DRV8825")
GPIO.setup(E1,GPIO.OUT) # set enable pin as output

mymotortest2 = RpiMotorLib.A4988Nema(D2, S2, (21,21,21), "DRV8825")
GPIO.setup(E2,GPIO.OUT) # set enable pin as output


def north_r(i):
    GPIO.output(E1,GPIO.LOW) 
    mymotortest1.motor_go(False,"Full" ,i,.0005,False,.05)
    GPIO.output(E1,GPIO.HIGH)

def north_l(i):
    GPIO.output(E2,GPIO.LOW)
    mymotortest2.motor_go(True,"Full" ,i,.0005,False,.05)
    GPIO.output(E2,GPIO.HIGH)

def south_r(i):
    GPIO.output(E1,GPIO.LOW) 
    mymotortest1.motor_go(True,"Full" ,i,.0005,False,.05)
    GPIO.output(E1,GPIO.HIGH)

def south_l(i):
    GPIO.output(E2,GPIO.LOW)
    mymotortest2.motor_go(False,"Full" ,i,.0005,False,.05)
    GPIO.output(E2,GPIO.HIGH)

def west_r(i):
    GPIO.output(E1,GPIO.LOW) 
    mymotortest1.motor_go(False,"Full" ,i,.0005,False,.05)
    GPIO.output(E1,GPIO.HIGH)

def west_l(i):
    GPIO.output(E2,GPIO.LOW)
    mymotortest2.motor_go(False,"Full" ,i,.0005,False,.05)
    GPIO.output(E2,GPIO.HIGH)

def east_r(i):
    GPIO.output(E1,GPIO.LOW) 
    mymotortest1.motor_go(True,"Full" ,i,.0005,False,.05)
    GPIO.output(E1,GPIO.HIGH)

def east_l(i):
    GPIO.output(E2,GPIO.LOW)
    mymotortest2.motor_go(True,"Full" ,i,.0005,False,.05)
    GPIO.output(E2,GPIO.HIGH)


# go start
def startY():
    Thread(target = north_r(75)).start()
    Thread(target = north_l(75)).start()
def startX():
    Thread(target = west_r(60)).start()
    Thread(target = west_l(60)).start()

def go1X():
    Thread(target = west_r(650)).start()
    Thread(target = west_l(650)).start()
def go1Y():
    Thread(target = north_r(100)).start()
    Thread(target = north_l(100)).start()
def back1Y():
    Thread(target = south_r(100)).start()
    Thread(target = south_l(100)).start()
def back1X():
    Thread(target = east_r(650)).start()
    Thread(target = east_l(650)).start()

while True :
    order = input("Order: ")
    if order == "n":
        Thread(target = north_r(200)).start()
        Thread(target = north_l(200)).start()
    
    elif order == "s":
        Thread(target = south_r(200)).start()
        Thread(target = south_l(200)).start()
        
    elif order == "w":
        Thread(target = west_r(200)).start()
        Thread(target = west_l(200)).start()
        
    elif order == "e":
        Thread(target = east_r(200)).start()
        Thread(target = east_l(200)).start()

    elif order == "0":
        Thread(target = north_r(75)).start()
        Thread(target = north_l(75)).start()
        Thread(target = west_r(60)).start()
        Thread(target = west_l(60)).start()
    elif order == "1":
        go1X()
        go1Y()
    elif order == "-1":
        back1X()
        back1Y()
    elif order == "q":
        break

GPIO.cleanup() # clear GPIO allocations after run