import os, re, discord, asyncio, time
from discord.ext import commands
import RPi.GPIO as GPIO
from RpiMotorLib import RpiMotorLib
from threading import Thread

D1, S1, E1= 22, 23, 24
D2, S2, E2 = 12, 5, 6

Forward = 20
Backward = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(Forward, GPIO.OUT)
GPIO.setup(Backward, GPIO.OUT)

def forward(x):
    GPIO.output(Forward, GPIO.HIGH)
    print("Moving Forward")
    time.sleep(x)
    GPIO.output(Forward, GPIO.LOW)
def reverse(x):
    GPIO.output(Backward, GPIO.HIGH)
    print("Moving Backward")
    time.sleep(x)
    GPIO.output(Backward, GPIO.LOW)

mymotortest1 = RpiMotorLib.A4988Nema(D1, S1, (21,21,21), "DRV8825")
GPIO.setup(E1,GPIO.OUT) # set enable pin as output

mymotortest2 = RpiMotorLib.A4988Nema(D2, S2, (21,21,21), "DRV8825")
GPIO.setup(E2,GPIO.OUT) # set enable pin as output

table = [1148506462704910386,1148505332809732127,1148506620054229042,1148507024091521084,1148507121281945643,1148506972954562680]
        #role channel id, table 1 channel id, table 2 channel id, private room 1 channel id, private room 2 channel id, meeting room channel id
        
TK = ''
class order:
    def __init__(self, table, order):
        self.table = table
        self.order = order
        
orders = []


menu = ['latte','americano','matcha','chocolate','waffle']
cancel=False
null=False

#-----------------steppermotor-----------------
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
    GPIO.output(E1,GPIO.LOW)
    mymotortest1.motor_go(False,"Full" ,1000,.0005,False,.05)
    GPIO.output(E1,GPIO.HIGH)
def t():
    GPIO.output(E2,GPIO.LOW)
    mymotortest2.motor_go(False,"Full" ,1000,.0005,False,.05)
    GPIO.output(E2,GPIO.HIGH)

def qq():
    GPIO.output(E1,GPIO.LOW)
    mymotortest1.motor_go(True,"Full" ,1000,.0005,False,.05)
    GPIO.output(E1,GPIO.HIGH)
def rr():
    GPIO.output(E2,GPIO.LOW)
    mymotortest2.motor_go(True,"Full" ,1000,.0005,False,.05)
    GPIO.output(E2,GPIO.HIGH)
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
    GPIO.output(E1,GPIO.LOW)
    mymotortest1.motor_go(False,"Full" ,1000,.0005,False,.05)
    GPIO.output(E1,GPIO.HIGH)
def x():
    GPIO.output(E2,GPIO.LOW)
    mymotortest2.motor_go(False,"Full" ,1000,.0005,False,.05)
    GPIO.output(E2,GPIO.HIGH)

def uu():
    GPIO.output(E1,GPIO.LOW)
    mymotortest1.motor_go(True,"Full" ,1000,.0005,False,.05)
    GPIO.output(E1,GPIO.HIGH)
def vv():
    GPIO.output(E2,GPIO.LOW)
    mymotortest2.motor_go(True,"Full" ,1000,.0005,False,.05)
    GPIO.output(E2,GPIO.HIGH)
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
    time.sleep(1.2)
    Thread(target = e).start()
    Thread(target = f).start()
    time.sleep(1.2)
    forward(.6)
def back5():
    reverse(.6)
    Thread(target = gg).start()
    Thread(target = hh).start()
    time.sleep(2)
    Thread(target = ee).start()
    Thread(target = ff).start()
    

def go1():
    
    Thread(target = i).start()
    Thread(target = j).start()
    time.sleep(1.2)
    Thread(target = k).start()
    Thread(target = l).start()
    time.sleep(1.2)
    forward(.6)

def back1():
    reverse(.6)
    Thread(target = ii).start()
    Thread(target = jj).start()
    time.sleep(1.2)
    Thread(target = kk).start()
    Thread(target = ll).start()
    

def go2():
    Thread(target = m).start()
    Thread(target = n).start()
    time.sleep(1.2)
    Thread(target = o).start()
    Thread(target = p).start()
    time.sleep(1.2)
    forward(.6)
def back2():
    reverse(.6)
    Thread(target = mm).start()
    Thread(target = nn).start()
    time.sleep(2)
    Thread(target = oo).start()
    Thread(target = pp).start()
    

def go3():
    Thread(target = q).start()
    Thread(target = r).start()
    time.sleep(1.2)
    Thread(target = s).start()
    Thread(target = t).start()
    time.sleep(1.2)
    forward(.6)
def back3():
    reverse(.6)
    Thread(target = qq).start()
    Thread(target = rr).start()
    time.sleep(2)
    Thread(target = ss).start()
    Thread(target = tt).start()
    

def go4():
    Thread(target = u).start()
    Thread(target = v).start()
    time.sleep(2)
    Thread(target = w).start()
    Thread(target = x).start()
    time.sleep(2)
    forward(.6)
def back4():
    reverse(.6)
    Thread(target = uu).start()
    Thread(target = vv).start()
    time.sleep(2)
    Thread(target = ww).start()
    Thread(target = xx).start()
    
#-----------------steppermotor-----------------
options = [start,go1,go2,go3,go4,go5]


intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
@client.event
async def on_message(message: discord.Message):
    global cancel,null
    if message.author == client.user:
        return
    channel = message.channel
    
    # test channel
    if channel.id == 1148509385912500234 and message.content.startswith('queue'):
        for i in range(len(orders)):
            await message.channel.send(f'{orders[i].order} Table: {str(orders[i].table)}')
            # print(orders)
            # print(orders[i].order, orders[i].table)
        return
    elif channel.id == 1148509385912500234 and message.content.startswith('start'):
        options[0]()
    elif channel.id == 1148509385912500234 and message.content.startswith('send'):
        options[int(orders[0].table)]() # calls the function go(table)
        channel = client.get_channel(table[int(orders[0].table)]) # set channel to sending table
        await channel.send('Order being delivered...')
        orders.pop(0)
        for i in range(len(orders)):
            await message.channel.send(f'{orders[i].order} Table: {str(orders[i].table)}')
        channel = message.channel
    
    elif channel.id == 1148509385912500234 and message.content.startswith('leave'):    
        async for msg in message.channel.history():
            await msg.delete()


    # assing role
    if channel.id == table[0] and message.content.lower() == ('1111'): # id of role channel
        await message.delete()
        user_role = discord.utils.get(message.guild.roles, name = "Table-1")
        new_member = message.author
        await new_member.add_roles(user_role)
    elif channel.id == table[0] and message.content.lower() == ('2222'):
        await message.delete()
        user_role = discord.utils.get(message.guild.roles, name = "Table-2")
        new_member = message.author
        await new_member.add_roles(user_role)
    elif channel.id == table[0] and message.content.lower() == ('3333'):
        await message.delete()
        user_role = discord.utils.get(message.guild.roles, name = "private-room-1")
        new_member = message.author
        await new_member.add_roles(user_role)
    elif channel.id == table[0] and message.content.lower() == ('4444'):
        await message.delete()
        user_role = discord.utils.get(message.guild.roles, name = "private-room-2")
        new_member = message.author
        await new_member.add_roles(user_role)
    elif channel.id == table[0] and message.content.lower() == ('5555'):
        await message.delete()
        user_role = discord.utils.get(message.guild.roles, name = "meeting-room")
        new_member = message.author
        await new_member.add_roles(user_role)
    elif channel.id == table[0]:
        await message.delete()

# table 1 channel
    if channel.id == table[1] and message.content.lower() == ('order'):
        
        await message.channel.send('What do you want?\nMenu :\n1. Latte\n2. Americano\n3. Matcha\n4. Chocolate\n5. Waffle')
        def check(m):
            global cancel,null
            null = False
            cancel = False
            for content in menu:
                if m.content.lower() == content and m.channel == channel:
                    var = content
                    orders.append(order(1,var)) # add order to queue
                    return m.content.lower() == content and m.channel == channel, orders, cancel, null
            if m.content.lower() == ('cancel') and m.channel == channel:
                    cancel=True
                    return m.content.lower() == ('cancel') and m.channel == channel, orders, cancel, null
            else:
                    null = True
                    return m.content.lower() == ('null') and m.channel ==  channel, orders, cancel, null
                
        msg = await client.wait_for('message', check=check)
        print(msg)
        # check if cancel
        print(null)
        if cancel == True:
            await message.channel.send('Canceled')
            cancel=False
        # check if valid command
        elif null == True:
            await message.channel.send('Please enter valid menu')
            null=False

        elif cancel == False and null == False:
            await message.channel.send(f'{orders[-1].order} Table1'.format(msg)) # print queue
            cancel=False
        return

    elif channel.id == table[1] and message.content.lower() == ('queue'):
        for i in range(len(orders)):
            await message.channel.send(f'{orders[i].order} Table: {str(orders[i].table)}')

    elif channel.id == table[1] and message.content.lower() == ('send'):
        back1()
        time.sleep(1)
        await message.channel.send('Getting back...')

        # delete role
    elif channel.id == table[1] and message.content.lower() == ('leave'):
        await message.delete()
        user_role = discord.utils.get(message.guild.roles, name = "Table-1")
        new_member = message.author
        await new_member.remove_roles(user_role)

        async for msg in message.channel.history():
            await msg.delete()
    

# table 2 channel
    if channel.id == table[2] and message.content.lower() == ('order'):
        
        await message.channel.send('What do you want?\nMenu :\n1. Latte\n2. Americano\n3. Matcha\n4. Chocolate\n5. Waffle')
        def check(m):
            global cancel,null
            null = False
            cancel = False
            for content in menu:
                if m.content.lower() == content and m.channel == channel:
                    var = content
                    orders.append(order(2,var)) # add order to queue
                    return m.content.lower() == content and m.channel == channel, orders, cancel, null
            if m.content.lower() == ('cancel') and m.channel == channel:
                    cancel=True
                    return m.content.lower() == ('cancel') and m.channel == channel, orders, cancel, null
            else:
                    null = True
                    return m.content.lower() == ('null') and m.channel ==  channel, orders, cancel, null
                
        msg = await client.wait_for('message', check=check)
        print(msg)
        # check if cancel
        print(null)
        if cancel == True:
            await message.channel.send('Canceled')
            cancel=False
        # check if valid command
        elif null == True:
            await message.channel.send('Please enter valid menu')
            null=False

        elif cancel == False and null == False:
            await message.channel.send(f'{orders[-1].order} Table2'.format(msg)) # print queue
            cancel=False
        return

    elif channel.id == table[2] and message.content.lower() == ('queue'):
        for i in range(len(orders)):
            await message.channel.send(f'{orders[i].order} Table: {str(orders[i].table)}')

    elif channel.id == table[2] and message.content.lower() == ('send'):
        back2()
        time.sleep(1)
        await message.channel.send('Getting back...')

    # delete role
    elif channel.id == table[2] and message.content.lower() == ('leave'):
        await message.delete()
        user_role = discord.utils.get(message.guild.roles, name = "Table-2")
        new_member = message.author
        await new_member.remove_roles(user_role)

        async for msg in message.channel.history():
            await msg.delete()

# table 3 channel
    if channel.id == table[3] and message.content.lower() == ('order'):
        
        await message.channel.send('What do you want?\nMenu :\n1. Latte\n2. Americano\n3. Matcha\n4. Chocolate\n5. Waffle')
        def check(m):
            global cancel,null
            null = False
            cancel = False
            for content in menu:
                if m.content.lower() == content and m.channel == channel:
                    var = content
                    orders.append(order(3,var)) # add order to queue
                    return m.content.lower() == content and m.channel == channel, orders, cancel, null
            if m.content.lower() == ('cancel') and m.channel == channel:
                    cancel=True
                    return m.content.lower() == ('cancel') and m.channel == channel, orders, cancel, null
            else:
                    null = True
                    return m.content.lower() == ('null') and m.channel ==  channel, orders, cancel, null
                
        msg = await client.wait_for('message', check=check)
        print(msg)
        # check if cancel
        print(null)
        if cancel == True:
            await message.channel.send('Canceled')
            cancel=False
        # check if valid command
        elif null == True:
            await message.channel.send('Please enter valid menu')
            null=False

        elif cancel == False and null == False:
            await message.channel.send(f'{orders[-1].order} pvRoom1'.format(msg)) # print queue
            cancel=False
        return

    elif channel.id == table[3] and message.content.lower() == ('queue'):
        for i in range(len(orders)):
            await message.channel.send(f'{orders[i].order} Table: {str(orders[i].table)}')
    
    elif channel.id == table[3] and message.content.lower() == ('send'):
        back3()
        time.sleep(1)
        await message.channel.send('Getting back...')

    # delete role
    elif channel.id == table[3] and message.content.lower() == ('leave'):
        await message.delete()
        user_role = discord.utils.get(message.guild.roles, name = "private-room-1")
        new_member = message.author
        await new_member.remove_roles(user_role)

        async for msg in message.channel.history():
            await msg.delete()

# table 4 channel
    if channel.id == table[4] and message.content.lower() == ('order'):
        
        await message.channel.send('What do you want?\nMenu :\n1. Latte\n2. Americano\n3. Matcha\n4. Chocolate\n5. Waffle')
        def check(m):
            global cancel,null
            null = False
            cancel = False
            for content in menu:
                if m.content.lower() == content and m.channel == channel:
                    var = content
                    orders.append(order(4,var)) # add order to queue
                    return m.content.lower() == content and m.channel == channel, orders, cancel, null
            if m.content.lower() == ('cancel') and m.channel == channel:
                    cancel=True
                    return m.content.lower() == ('cancel') and m.channel == channel, orders, cancel, null
            else:
                    null = True
                    return m.content.lower() == ('null') and m.channel ==  channel, orders, cancel, null
                
        msg = await client.wait_for('message', check=check)
        print(msg)
        # check if cancel
        print(null)
        if cancel == True:
            await message.channel.send('Canceled')
            cancel=False
        # check if valid command
        elif null == True:
            await message.channel.send('Please enter valid menu')
            null=False

        elif cancel == False and null == False:
            await message.channel.send(f'{orders[-1].order} pvRoom2'.format(msg)) # print queue
            cancel=False
        return

    elif channel.id == table[4] and message.content.lower() == ('queue'):
        for i in range(len(orders)):
            await message.channel.send(f'{orders[i].order} Table: {str(orders[i].table)}')

    elif channel.id == table[4] and message.content.lower() == ('send'):
        back4()
        time.sleep(1)
        await message.channel.send('Getting back...')

        # delete role
    elif channel.id == table[4] and message.content.lower() == ('leave'):
        await message.delete()
        user_role = discord.utils.get(message.guild.roles, name = "private-room-2")
        new_member = message.author
        await new_member.remove_roles(user_role)

        async for msg in message.channel.history():
            await msg.delete()

# table 5 channel
    if channel.id == table[5] and message.content.lower() == ('order'):
        
        await message.channel.send('What do you want?\nMenu :\n1. Latte\n2. Americano\n3. Matcha\n4. Chocolate\n5. Waffle')
        def check(m):
            global cancel,null
            null = False
            cancel = False
            for content in menu:
                if m.content.lower() == content and m.channel == channel:
                    var = content
                    orders.append(order(5,var)) # add order to queue
                    return m.content.lower() == content and m.channel == channel, orders, cancel, null
            if m.content.lower() == ('cancel') and m.channel == channel:
                    cancel=True
                    return m.content.lower() == ('cancel') and m.channel == channel, orders, cancel, null
            else:
                    null = True
                    return m.content.lower() == ('null') and m.channel ==  channel, orders, cancel, null
                
        msg = await client.wait_for('message', check=check)
        print(msg)
        # check if cancel
        print(null)
        if cancel == True:
            await message.channel.send('Canceled')
            cancel=False
        # check if valid command
        elif null == True:
            await message.channel.send('Please enter valid menu')
            null=False

        elif cancel == False and null == False:
            await message.channel.send(f'{orders[-1].order} meetingRoom'.format(msg)) # print queue
            cancel=False
        return

    elif channel.id == table[5] and message.content.lower() == ('queue'):
        for i in range(len(orders)):
            await message.channel.send(f'{orders[i].order} Table: {str(orders[i].table)}')

    elif channel.id == table[5] and message.content.lower() == ('send'):
        back5()
        time.sleep(1)
        await message.channel.send('Getting back...')

        # delete role
    elif channel.id == table[5] and message.content.lower() == ('leave'):
        await message.delete()
        user_role = discord.utils.get(message.guild.roles, name = "meeting-room")
        new_member = message.author
        await new_member.remove_roles(user_role)

        async for msg in message.channel.history():
            await msg.delete()
    
   

client.run(TK)
