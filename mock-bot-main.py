import discord
import aiohttp
import time
import random
from discord.ext import commands

TOKEN = ''
userid = ''
version = 'v0.1'
invite = "https://discordapp.com/api/oauth2/authorize?client_id=670079293673570323&permissions=0&scope=bot"
client = discord.Client()
ts = time.gmtime()

@client.event
async def on_message(message):
    #msg_history = await channel.history(limit=100).flatten()
    # We don't want the bot to reply to itself
    if message.author == client.user:
        return
    #or other bots
    if message.author.bot:
        return

    if message.content.startswith('!mock'):
        msg = 'Currently unavaliable'
        await message.channel.send(msg)
        print("[",time.strftime("%Y-%m-%d %H:%M:%S",ts),"]",message.author," used about scp.")
    
    if message.content.startswith('!mock-invite'):
        msg = invite
        await message.channel.send(msg)
        print("[",time.strftime("%Y-%m-%d %H:%M:%S",ts),"]",message.author," used about scp.")
    
    if message.content.startswith('!mock-help'):
            embed = discord.Embed(title="**List of commands**", description="List of commands to use.", colour=discord.Colour(0x7a19fd))
            embed.set_author(name="mock-bot")
            embed.set_footer(text=(version))
            embed.add_field(name="!mock", value="Mock the message above yours.", inline=False)
            embed.add_field(name="!mock-help", value="Show this embed.", inline=False)
            embed.add_field(name="!mock-invite", value="Get invite to the bot", inline=False)
            await message.channel.send(embed=embed)
            print("[",time.strftime("%Y-%m-%d %H:%M:%S",ts),"]",message.author," viewed the list of commands.")

#def mocking():

@client.event
async def on_ready():
    print('------------------------------------------------')
    print('Logged in as:')
    print(client.user.name)
    print(client.user.id)
    print('------------------------------------------------')
    print("mock-bot", version,"is connected and running!")
    print('------------------------------------------------')

client.run(TOKEN)
