import os, re, discord, asyncio, time
from discord.ext import commands

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
    elif channel.id == 1148509385912500234 and message.content.startswith('queue'):
        for i in range(len(orders)):
            await message.channel.send(f'{orders[i].order} Table: {str(orders[i].table)}')
            # print(orders)
            # print(orders[i].order, orders[i].table)
        return
    elif channel.id == 1148509385912500234 and message.content.startswith('send'):
        channel = client.get_channel(table[int(orders[0].table)]) ######
        await channel.send('Order being delivered...\nIf order receive please type "send"') #####
        orders.pop(0)
        for i in range(len(orders)):
            await message.channel.send(f'{orders[i].order} Table: {str(orders[i].table)}')
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

        # delete role
    elif channel.id == table[5] and message.content.lower() == ('leave'):
        await message.delete()
        user_role = discord.utils.get(message.guild.roles, name = "meeting-room")
        new_member = message.author
        await new_member.remove_roles(user_role)

        async for msg in message.channel.history():
            await msg.delete()
    
   

client.run(TK)
