import os, re, discord, asyncio
from discord.ext import commands
import RPi.GPIO as GPIO
from RpiMotorLib import RpiMotorLib
import time

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


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    channel = message.channel
    # test channel
    GPIO.output(EN_pin,GPIO.HIGH)
    if channel.id == 1148509385912500234 and message.content.startswith('move'):
        await message.channel.send('OK!')
        GPIO.output(EN_pin,GPIO.LOW) # pull enable to low to enable motor
        mymotortest.motor_go(False, # True=Clockwise, False=Counter-Clockwise
                             "Full" , # Step type (Full,Half,1/4,1/8,1/16,1/32)
                             200, # number of steps
                             .0005, # step delay [sec]
                             False, # True = print verbose output 
                             .05) # initial delay [sec]

    if message.content.startswith('hello,'):
        await message.channel.send('Hello!')
        
    # assing role
    if channel.id == 1148506462704910386 and message.content.lower() == ('0001'): # id of role channel
        await message.delete()
        user_role = discord.utils.get(message.guild.roles, name = "Table-1")
        new_member = message.author
        await new_member.add_roles(user_role)
    elif channel.id == 1148506462704910386 and message.content.lower() == ('0002'):
        await message.delete()
        user_role = discord.utils.get(message.guild.roles, name = "Table-2")
        new_member = message.author
        await new_member.add_roles(user_role)
    elif channel.id == 1148506462704910386:
        await message.delete()

    # table 1 channel
    if channel.id == 1148505332809732127 and message.content.lower() == ('menu'):
        # send message
        await message.delete()
        await channel.send('Menu\n1. Latte\n2. Americano\n3. Matcha\n4. Chocolate')
    elif channel.id == 1148505332809732127 and message.content.lower() == ('order'):
        return
    
    # delete role
    elif channel.id == 1148505332809732127 and message.content.lower() == ('leave'):
        await message.delete()
        user_role = discord.utils.get(message.guild.roles, name = "Table-1")
        new_member = message.author
        await new_member.remove_roles(user_role)


client.run('ODU2NDY4MTc2NTU1NjA2MDE2.GLNq0k.I_18Gt2Y8_BrPwdPFH-6wOSp7duWPraxnTy0wE')
