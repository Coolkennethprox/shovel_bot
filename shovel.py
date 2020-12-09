import discord
from discord.ext import commands

client = commands.Bot(commands_prefix = 'sh?')

@client.event
async def on_ready():
    print('bot is ready')

@client.event
async def on_member_join(member):
    print(f*'{member} has joined a server.')

@client.event
async de on_member_remove(member):
print(f*'{member} has left the server')


    client.run('NzY4NDkxODkyNzU2NzA5Mzk2.X5BP2Q._wuV1LsuCVJUBsqPCMFNUw3jNHc')
