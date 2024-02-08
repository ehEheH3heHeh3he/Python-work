import os
import nextcord
from nextcord.ext import commands
import random
from dotenv.main import load_dotenv


client = commands.Bot(command_prefix='.//')
load_dotenv()

@client.event
async def on_ready():
    print(f'Successfully logged in as {client.user}')   
    
    
@client.command()
async def randomize(ctx):
    
    '''randomize sauce'''
    
    url = f'https://nhentai.net/g/{random.randint(1, 300000)}'
    await ctx.respond(f'Here\'s your sauce: {url}')
    
    
@client.command()
async def find(ctx, sauce: int):
    
    '''find target sauce'''
    
    await ctx.channel.send(f'Here\'s your sauce: https://nhentai.net/g/{sauce}')


@client.command()
async def dm(ctx, member: nextcord.Member):

    '''send random sauce to the requester dm'''
    
    url = f'https://nhentai.net/g/{random.randint(1, 300000)}'
    
    channel = await member.create_dm()
    
    try:
        await channel.send(f'Here\'s your sauce: {url}')
        
    except nextcord.HTTPException:
        await ctx.send(':x: Member had their dm close, message not sent')
    

token = os.getenv('TOKEN')
client.run(token)