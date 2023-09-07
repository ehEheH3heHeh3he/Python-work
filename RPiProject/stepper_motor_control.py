import RPi.GPIO as GPIO
from RpiMotorLib import RpiMotorLib
import time

################################
# RPi and Motor Pre-allocations
################################
#
#define GPIO pins
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

###########################
# Actual motor control
###########################

from threading import Thread

def left_r():
    print('left1')
    GPIO.output(E1,GPIO.LOW) # pull enable to low to enable motor
    mymotortest1.motor_go(False, # True=Clockwise, False=Counter-Clockwise
                            "Full" , # Step type (Full,Half,1/4,1/8,1/16,1/32)
                            200, # number of steps
                            .0005, # step delay [sec]
                            False, # True = print verbose output 
                            .05) # initial delay [sec]
    GPIO.output(E1,GPIO.HIGH)

def left_l():
    print("left2")
    GPIO.output(E2,GPIO.LOW)
    mymotortest2.motor_go(False, # True=Clockwise, False=Counter-Clockwise
                        "Full" , # Step type (Full,Half,1/4,1/8,1/16,1/32)
                        200, # number of steps
                        .0005, # step delay [sec]
                        False, # True = print verbose output 
                        .05) # initial delay [sec]
    GPIO.output(E2,GPIO.HIGH)
def right_r():
    print("right1")
    GPIO.output(E1,GPIO.LOW) # pull enable to low to enable motor
    mymotortest1.motor_go(True, # True=Clockwise, False=Counter-Clockwise
                            "Full" , # Step type (Full,Half,1/4,1/8,1/16,1/32)
                            200, # number of steps
                            .0005, # step delay [sec]
                            False, # True = print verbose output 
                            .05) # initial delay [sec]
    GPIO.output(E1,GPIO.HIGH)

def right_l():
    print("right2")
    GPIO.output(E2,GPIO.LOW)
    mymotortest2.motor_go(True, # True=Clockwise, False=Counter-Clockwise
                        "Full" , # Step type (Full,Half,1/4,1/8,1/16,1/32)
                        200, # number of steps
                        .0005, # step delay [sec]
                        False, # True = print verbose output 
                        .05) # initial delay [sec]
    GPIO.output(E2,GPIO.HIGH)
i =0
while True :
    order = input("Order: ")
    if order == "1":
        Thread(target = left_r).start()
        Thread(target = left_l).start()
        
    elif order == "2":
        Thread(target = right_r).start()
        Thread(target = right_l).start()

GPIO.cleanup() # clear GPIO allocations after run