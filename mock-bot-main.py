import discord
import aiohttp
import time
import random
from discord.ext import commands

TOKEN = ''
userid = '670079293673570323'
version = 'v0.4'
invite = "https://discordapp.com/api/oauth2/authorize?client_id=670079293673570323&permissions=8&scope=bot"
client = discord.Client()
ts = time.gmtime()

@client.event
async def on_message(message):
    step = False
    channel = message.channel
    # We don't want the bot to reply to itself
    if message.author == client.user:
        return
    #or other bots
    if message.author.bot:
        return

    if message.content.startswith('!mock') or message.content.startswith(')'):
        if message.author.id == (670079293673570323):
            await message.channel.send("SIKE im not gonna mock myself loool")
        #if message.embed 
        messages = await channel.history(limit=2).flatten()
        grabbedMsg = (messages[1].content)
        mockedmsg = ""
        for i in grabbedMsg:
            step = not step
            if step == False:
                mockedmsg = mockedmsg + (i.upper())
            if step == True:
                mockedmsg = mockedmsg + (i.lower())
        await message.delete()
        await message.channel.send(mockedmsg)
        print("[",time.strftime("%Y-%m-%d %H:%M:%S",ts),"]",message.author," mocked.")
    
    if message.content.startswith('!mock-invite'):
        msg = invite
        await message.channel.send(msg)
        print("[",time.strftime("%Y-%m-%d %H:%M:%S",ts),"]",message.author," used about !invite.")

    if message.content.startswith('!mock-changelog'):
        msg = invite
        await message.channel.send("""
        ```asciidoc
        [Current] = v0.5 = Added ')' as a mock prefix
        = v0.4 = the bot now deletes your '!mock' command when you use it, making it look better
        = v0.3 = I forget lol
        = v0.2 = it actually works now
        = v0.1 = the birth of the bot
        """)
        print("[",time.strftime("%Y-%m-%d %H:%M:%S",ts),"]",message.author," used about !invite.")

    if message.content.startswith('!mock-help'):
            embed = discord.Embed(title="**List of commands**", description="List of commands to use.", colour=discord.Colour(0x7a19fd))
            embed.set_author(name="mock-bot")
            embed.set_footer(text=(version))
            embed.add_field(name="!mock", value="Mock the message above yours.", inline=False)
            embed.add_field(name="!mock-help", value="Show this embed.", inline=False)
            embed.add_field(name="!mock-invite", value="Get invite to the bot", inline=False)
            await message.channel.send(embed=embed)
            print("[",time.strftime("%Y-%m-%d %H:%M:%S",ts),"]",message.author," viewed the list of commands.")
 

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