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


def north_r():
    GPIO.output(E1,GPIO.LOW) 
    mymotortest1.motor_go(False,"Full" ,200,.0005,False,.05)
    GPIO.output(E1,GPIO.HIGH)

def north_l():
    GPIO.output(E2,GPIO.LOW)
    mymotortest2.motor_go(True,"Full" ,200,.0005,False,.05)
    GPIO.output(E2,GPIO.HIGH)

def south_r():
    GPIO.output(E1,GPIO.LOW) 
    mymotortest1.motor_go(True,"Full" ,200,.0005,False,.05)
    GPIO.output(E1,GPIO.HIGH)

def south_l():
    GPIO.output(E2,GPIO.LOW)
    mymotortest2.motor_go(False,"Full" ,200,.0005,False,.05)
    GPIO.output(E2,GPIO.HIGH)

def west_r():
    GPIO.output(E1,GPIO.LOW) 
    mymotortest1.motor_go(False,"Full" ,200,.0005,False,.05)
    GPIO.output(E1,GPIO.HIGH)

def west_l():
    GPIO.output(E2,GPIO.LOW)
    mymotortest2.motor_go(False,"Full" ,200,.0005,False,.05)
    GPIO.output(E2,GPIO.HIGH)

def east_r():
    GPIO.output(E1,GPIO.LOW) 
    mymotortest1.motor_go(True,"Full" ,200,.0005,False,.05)
    GPIO.output(E1,GPIO.HIGH)

def east_l():
    GPIO.output(E2,GPIO.LOW)
    mymotortest2.motor_go(True,"Full" ,200,.0005,False,.05)
    GPIO.output(E2,GPIO.HIGH)

def down():
    pass

def up():
    pass

i =0
while True :
    order = input("Order: ")
    if order == "n":
        Thread(target = north_r).start()
        Thread(target = north_l).start()
    
    elif order == "s":
        Thread(target = south_r).start()
        Thread(target = south_l).start()

    elif order == "w":
        Thread(target = west_r).start()
        Thread(target = west_l).start()
        
    elif order == "e":
        Thread(target = east_r).start()
        Thread(target = east_l).start()

GPIO.cleanup() # clear GPIO allocations after run