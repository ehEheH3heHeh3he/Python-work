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


# def north_r(i):
#     GPIO.output(E1,GPIO.LOW) 
#     mymotortest1.motor_go(False,"Full" ,i,.0005,False,.05)
#     GPIO.output(E1,GPIO.HIGH)

# def north_l(i):
#     GPIO.output(E2,GPIO.LOW)
#     mymotortest2.motor_go(True,"Full" ,i,.0005,False,.05)
#     GPIO.output(E2,GPIO.HIGH)

# def south_r(i):
#     GPIO.output(E1,GPIO.LOW) 
#     mymotortest1.motor_go(True,"Full" ,i,.0005,False,.05)
#     GPIO.output(E1,GPIO.HIGH)

# def south_l(i):
#     GPIO.output(E2,GPIO.LOW)
#     mymotortest2.motor_go(False,"Full" ,i,.0005,False,.05)
#     GPIO.output(E2,GPIO.HIGH)

# def west_r(i):
#     GPIO.output(E1,GPIO.LOW) 
#     mymotortest1.motor_go(False,"Full" ,i,.0005,False,.05)
#     GPIO.output(E1,GPIO.HIGH)

# def west_l(i):
#     GPIO.output(E2,GPIO.LOW)
#     mymotortest2.motor_go(False,"Full" ,i,.0005,False,.05)
#     GPIO.output(E2,GPIO.HIGH)

# def east_r(i):
#     GPIO.output(E1,GPIO.LOW) 
#     mymotortest1.motor_go(True,"Full" ,i,.0005,False,.05)
#     GPIO.output(E1,GPIO.HIGH)

# def east_l(i):
#     GPIO.output(E2,GPIO.LOW)
#     mymotortest2.motor_go(True,"Full" ,i,.0005,False,.05)
#     GPIO.output(E2,GPIO.HIGH)

def a():
    GPIO.output(E1,GPIO.LOW) 
    mymotortest1.motor_go(False,"Full" ,75,.0005,False,.05)
    GPIO.output(E1,GPIO.HIGH)
def b():
    GPIO.output(E2,GPIO.LOW)
    mymotortest2.motor_go(True,"Full" ,75,.0005,False,.05)
    GPIO.output(E2,GPIO.HIGH)
def c():
    GPIO.output(E1,GPIO.LOW) 
    mymotortest1.motor_go(False,"Full" ,60,.0005,False,.05)
    GPIO.output(E1,GPIO.HIGH)
def d():
    GPIO.output(E2,GPIO.LOW)
    mymotortest2.motor_go(False,"Full" ,60,.0005,False,.05)
    GPIO.output(E2,GPIO.HIGH)

def e():
    GPIO.output(E1,GPIO.LOW) 
    mymotortest1.motor_go(False,"Full" ,650,.0005,False,.2)
    GPIO.output(E1,GPIO.HIGH)
def f():
    GPIO.output(E2,GPIO.LOW)
    mymotortest2.motor_go(False,"Full" ,650,.0005,False,.2)
    GPIO.output(E2,GPIO.HIGH)
def g():
    GPIO.output(E1,GPIO.LOW) 
    mymotortest1.motor_go(False,"Full" ,100,.0005,False,.05)
    GPIO.output(E1,GPIO.HIGH)
def h():
    GPIO.output(E2,GPIO.LOW)
    mymotortest2.motor_go(True,"Full" ,100,.0005,False,.05)
    GPIO.output(E2,GPIO.HIGH)

def ee():
    GPIO.output(E1,GPIO.LOW) 
    mymotortest1.motor_go(True,"Full" ,100,.0005,False,.05)
    GPIO.output(E1,GPIO.HIGH)
def ff():
    GPIO.output(E2,GPIO.LOW)
    mymotortest2.motor_go(False,"Full" ,100,.0005,False,.05)
    GPIO.output(E2,GPIO.HIGH)
def gg():
    GPIO.output(E1,GPIO.LOW) 
    mymotortest1.motor_go(True,"Full" ,650,.0005,False,.05)
    GPIO.output(E1,GPIO.HIGH)
def hh():
    GPIO.output(E2,GPIO.LOW)
    mymotortest2.motor_go(True,"Full" ,650,.0005,False,.05)
    GPIO.output(E2,GPIO.HIGH)

def i():
    GPIO.output(E1,GPIO.LOW) 
    mymotortest1.motor_go(False,"Full" ,350,.0005,False,.05)
    GPIO.output(E1,GPIO.HIGH)
def j():
    GPIO.output(E2,GPIO.LOW)
    mymotortest2.motor_go(False,"Full" ,350,.0005,False,.05)
    GPIO.output(E2,GPIO.HIGH)  
def k():
    GPIO.output(E1,GPIO.LOW) 
    mymotortest1.motor_go(False,"Full" ,500,.0005,False,.05)
    GPIO.output(E1,GPIO.HIGH)
def l():
    GPIO.output(E2,GPIO.LOW)
    mymotortest2.motor_go(True,"Full" ,500,.0005,False,.05)
    GPIO.output(E2,GPIO.HIGH)

def ii():
    GPIO.output(E1,GPIO.LOW) 
    mymotortest1.motor_go(True,"Full" ,500,.0005,False,.05)
    GPIO.output(E1,GPIO.HIGH)
def jj():
    GPIO.output(E2,GPIO.LOW)
    mymotortest2.motor_go(False,"Full" ,500,.0005,False,.05)
    GPIO.output(E2,GPIO.HIGH)
def kk():
    GPIO.output(E1,GPIO.LOW) 
    mymotortest1.motor_go(True,"Full" ,350,.0005,False,.05)
    GPIO.output(E1,GPIO.HIGH)
def ll():
    GPIO.output(E2,GPIO.LOW)
    mymotortest2.motor_go(True,"Full" ,350,.0005,False,.05)
    GPIO.output(E2,GPIO.HIGH)  

def m():
    GPIO.output(E1,GPIO.LOW) 
    mymotortest1.motor_go(False,"Full" ,350,.0005,False,.05)
    GPIO.output(E1,GPIO.HIGH)
def n():
    GPIO.output(E2,GPIO.LOW)
    mymotortest2.motor_go(False,"Full" ,350,.0005,False,.05)
    GPIO.output(E2,GPIO.HIGH) 
def o():
    GPIO.output(E1,GPIO.LOW) 
    mymotortest1.motor_go(False,"Full" ,1000,.0005,False,.05)
    GPIO.output(E1,GPIO.HIGH)
def p():
    GPIO.output(E2,GPIO.LOW)
    mymotortest2.motor_go(True,"Full" ,1000,.0005,False,.05)
    GPIO.output(E2,GPIO.HIGH)

def mm():
    GPIO.output(E1,GPIO.LOW) 
    mymotortest1.motor_go(True,"Full" ,1000,.0005,False,.05)
    GPIO.output(E1,GPIO.HIGH)
def nn():
    GPIO.output(E2,GPIO.LOW)
    mymotortest2.motor_go(False,"Full" ,1000,.0005,False,.05)
    GPIO.output(E2,GPIO.HIGH)
def oo():
    GPIO.output(E1,GPIO.LOW) 
    mymotortest1.motor_go(True,"Full" ,350,.0005,False,.05)
    GPIO.output(E1,GPIO.HIGH)
def pp():
    GPIO.output(E2,GPIO.LOW)
    mymotortest2.motor_go(True,"Full" ,350,.0005,False,.05)
    GPIO.output(E2,GPIO.HIGH)

def q():
    GPIO.output(E1,GPIO.LOW)
    mymotortest1.motor_go(False,"Full" ,450,.0005,False,.05)
    GPIO.output(E1,GPIO.HIGH)
def r():
    GPIO.output(E2,GPIO.LOW)
    mymotortest2.motor_go(True,"Full" ,450,.0005,False,.05)
    GPIO.output(E2,GPIO.HIGH)
def s():
    GPIO.output(E2,GPIO.LOW)
    mymotortest1.motor_go(False,"Full" ,1000,.0005,False,.05)
    GPIO.output(E2,GPIO.HIGH)
def t():
    GPIO.output(E1,GPIO.LOW)
    mymotortest2.motor_go(False,"Full" ,1000,.0005,False,.05)
    GPIO.output(E1,GPIO.HIGH)

def qq():
    GPIO.output(E2,GPIO.LOW)
    mymotortest1.motor_go(True,"Full" ,1000,.0005,False,.05)
    GPIO.output(E2,GPIO.HIGH)
def rr():
    GPIO.output(E1,GPIO.LOW)
    mymotortest2.motor_go(True,"Full" ,1000,.0005,False,.05)
    GPIO.output(E1,GPIO.HIGH)
def ss():
    GPIO.output(E1,GPIO.LOW)
    mymotortest1.motor_go(True,"Full" ,450,.0005,False,.05)
    GPIO.output(E1,GPIO.HIGH)
def tt():
    GPIO.output(E2,GPIO.LOW)
    mymotortest2.motor_go(False,"Full" ,450,.0005,False,.05)
    GPIO.output(E2,GPIO.HIGH)

def u():
    GPIO.output(E1,GPIO.LOW)
    mymotortest1.motor_go(False,"Full" ,1000,.0005,False,.05)
    GPIO.output(E1,GPIO.HIGH)
def v():
    GPIO.output(E2,GPIO.LOW)
    mymotortest2.motor_go(True,"Full" ,1000,.0005,False,.05)
    GPIO.output(E2,GPIO.HIGH)
def w():
    GPIO.output(E2,GPIO.LOW)
    mymotortest1.motor_go(False,"Full" ,1000,.0005,False,.05)
    GPIO.output(E2,GPIO.HIGH)
def x():
    GPIO.output(E1,GPIO.LOW)
    mymotortest2.motor_go(False,"Full" ,1000,.0005,False,.05)
    GPIO.output(E1,GPIO.HIGH)

def uu():
    GPIO.output(E2,GPIO.LOW)
    mymotortest1.motor_go(True,"Full" ,1000,.0005,False,.05)
    GPIO.output(E2,GPIO.HIGH)
def vv():
    GPIO.output(E1,GPIO.LOW)
    mymotortest2.motor_go(True,"Full" ,1000,.0005,False,.05)
    GPIO.output(E1,GPIO.HIGH)
def ww():
    GPIO.output(E1,GPIO.LOW)
    mymotortest1.motor_go(True,"Full" ,1000,.0005,False,.05)
    GPIO.output(E1,GPIO.HIGH)
def xx():
    GPIO.output(E2,GPIO.LOW)
    mymotortest2.motor_go(False,"Full" ,1000,.0005,False,.05)
    GPIO.output(E2,GPIO.HIGH)

# go start
def start():
    Thread(target = a).start()
    Thread(target = b).start()
    time.sleep(.3)
    Thread(target = c).start()
    Thread(target = d).start()

def go5():
    Thread(target = g).start()
    Thread(target = h).start()
    time.sleep(.7)
    Thread(target = e).start()
    Thread(target = f).start()
def back5():
    Thread(target = gg).start()
    Thread(target = hh).start()
    time.sleep(.7)
    Thread(target = ee).start()
    Thread(target = ff).start()

def go1():
    Thread(target = i).start()
    Thread(target = j).start()
    time.sleep(.7)
    Thread(target = k).start()
    Thread(target = l).start()
def back1():
    Thread(target = ii).start()
    Thread(target = jj).start()
    time.sleep(.7)
    Thread(target = kk).start()
    Thread(target = ll).start()

def go2():
    Thread(target = m).start()
    Thread(target = n).start()
    time.sleep(.8)
    Thread(target = o).start()
    Thread(target = p).start()
def back2():
    Thread(target = mm).start()
    Thread(target = nn).start()
    time.sleep(1.2)
    Thread(target = oo).start()
    Thread(target = pp).start()

def go3():
    Thread(target = q).start()
    Thread(target = r).start()
    time.sleep(.8)
    Thread(target = s).start()
    Thread(target = t).start()
def back3():
    Thread(target = qq).start()
    Thread(target = rr).start()
    time.sleep(1.2)
    Thread(target = ss).start()
    Thread(target = tt).start()

def go4():
    Thread(target = u).start()
    Thread(target = v).start()
    time.sleep(1.2)
    Thread(target = w).start()
    Thread(target = x).start()
def back4():
    Thread(target = uu).start()
    Thread(target = vv).start()
    time.sleep(1.2)
    Thread(target = ww).start()
    Thread(target = xx).start()

while True :
    order = input("Order: ")
    if order == "0":
        start()
    elif order == "1":
        go5()
    elif order == "-1":
        back5()
    elif order == "2":
        go1()
    elif order == "-2":
        back1()
    elif order == "3":
        go2()
    elif order == "-3":
        back2()
    elif order == "4":
        go3()
    elif order == "-4":
        back3()
    elif order == "5":
        go4()
    elif order == "-5":
        back4()
    elif order == "q":
        break

GPIO.cleanup() # clear GPIO allocations after run