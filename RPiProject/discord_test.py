import os, re, discord, asyncio
from discord.ext import commands
import RPi.GPIO as GPIO
from RpiMotorLib import RpiMotorLib
import time

table = [1148506462704910386,1148505332809732127,1148506620054229042]
        #role channel id, table 1 channel id, table 2 channel id
        
TK = ''
menu = {'americano': 20
        ,'latte': 15
        ,'matcha': 50
        ,'croissant': 90
        ,'waffle': 40}
queue = []


#define GPIO pins
direction= 22 # Direction (DIR) GPIO Pin
step = 23 # Step GPIO Pin
EN_pin = 24 # enable pin (LOW to enable)

# Declare a instance of class pass GPIO pins numbers and the motor type
mymotortest = RpiMotorLib.A4988Nema(direction, step, (21,21,21), "DRV8825")
GPIO.setup(EN_pin,GPIO.OUT) # set enable pin as output

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    GPIO.output(EN_pin,GPIO.HIGH)

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    channel = message.channel
    
    # test channel
    GPIO.output(EN_pin,GPIO.HIGH)
    if channel.id == 1148509385912500234 and message.content.startswith('move'):
        await message.channel.send('OK!')
        home_table(1)

    # assing role
    if channel.id == table[0] and message.content.lower() == ('0001'): # id of role channel
        await message.delete()
        user_role = discord.utils.get(message.guild.roles, name = "Table-1")
        new_member = message.author
        await new_member.add_roles(user_role)
    elif channel.id == table[0] and message.content.lower() == ('0002'):
        await message.delete()
        user_role = discord.utils.get(message.guild.roles, name = "Table-2")
        new_member = message.author
        await new_member.add_roles(user_role)
    elif channel.id == table[0]:
        await message.delete()

    
    # table 1 channel
    if channel.id == table[1] and message.content.lower() == ('order'):
        await message.channel.send('What would you like?')
        # if channel.id == table[1] and message.content.lower() == ('matcha'):
        #     queue.append(message.lower()+channel.id)
        #     await message.channel.send('Order received please wait...')

        for content in menu:
            if message.content.lower() == content:
                await message.channel.send(f'{content} : {menu[content]} baht')
                msg = await client.wait_for('message', check=message, timeout=30)
                if 'paid' in msg:
                    queue.append(content+channel.id)
                    print(queue)
                    await message.channel.send('Order received please wait...')
                    return
                elif 'cancel' in msg:
                    await message.channel.send('Order canceled')
                    return

        # delete role
    elif channel.id == table[1] and message.content.lower() == ('leave'):
        await message.delete()
        user_role = discord.utils.get(message.guild.roles, name = "Table-1")
        new_member = message.author
        await new_member.remove_roles(user_role)
    
    # table 2 channel
    if channel.id == table[2] and message.content.lower() == ('menu'):
        # send message
        await message.delete()
        await channel.send('Menu\n1. Latte\n2. Americano\n3. Matcha\n4. Chocolate')
    elif channel.id == table[2] and message.content.lower() == ('order'):
        return

client.run(TK)

def home_table(num):
    if num == 1:
        GPIO.output(EN_pin,GPIO.LOW) # pull enable to low to enable motor
        mymotortest.motor_go(False, "Full", 200, .0005, False, .05)
