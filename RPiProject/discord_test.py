import os, re, discord, asyncio, time
from discord.ext import commands

table = [1148506462704910386,1148505332809732127,1148506620054229042]
        #role channel id, table 1 channel id, table 2 channel id
        
TK = ''
queue = []
menu = ['waffle','latte','americano','matcha','chocolate']
cancel=False
null=False

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
    if channel.id == 1148509385912500234 and message.content.startswith('move'):
        await message.channel.send('OK!')
        return
    elif channel.id == 1148509385912500234 and message.content.startswith('check'):
        await message.channel.send(queue)
        return

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
        
        await message.channel.send('What do you want?\nMenu :\n1. Latte\n2. Americano\n3. Matcha\n4. Chocolate')
        def check(m):
            global cancel,null
            null = False
            cancel = False
            for content in menu:
                if m.content.lower() == content and m.channel == channel:
                    var = content
                    queue.append(var) # add order to queue
                    return m.content.lower() == content and m.channel == channel, queue, cancel, null
            if m.content.lower() == ('cancel') and m.channel == channel:
                    cancel=True
                    return m.content.lower() == ('cancel') and m.channel == channel, queue, cancel, null
            else:
                    null = True
                    return m.content.lower() == ('null') and m.channel ==  channel, queue, cancel, null
                
        msg = await client.wait_for('message', check=check)
        print(msg)
        # check if cancel
        print(null)
        if cancel == True:
            await message.channel.send('Canceled')
            cancel=False
        elif null == True:
            await message.channel.send('Please enter valid menu')
            null=False

        elif cancel == False and null == False:
            await message.channel.send(f'{queue}'.format(msg)) # print queue
            cancel=False
        return

        # delete role
    elif channel.id == table[1] and message.content.lower() == ('leave'):
        await message.delete()
        user_role = discord.utils.get(message.guild.roles, name = "Table-1")
        new_member = message.author
        await new_member.remove_roles(user_role)

        async for msg in message.channel.history():
            await msg.delete()
    
    # table 2 channel
    if channel.id == table[2] and message.content.lower() == ('menu'):
        # send message
        await message.delete()
        await channel.send('Menu\n1. Latte\n2. Americano\n3. Matcha\n4. Chocolate')
    elif channel.id == table[2] and message.content.lower() == ('order'):
        return

client.run(TK)
