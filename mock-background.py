import discord
import asyncio

client = discord.Client()

async def my_background_task():
    await client.wait_until_ready()
    #await client.change_presence(status=discord.Status.dnd)  # Online, idle, invisible, dnd
    while True:
        await client.change_presence(activity=discord.Game(name="mocking you lol"))

@client.event
async def on_ready():
    print('-----------------------------------------------------')
    print('Logged in as:')
    print(client.user.name)
    print(client.user.id)
    print('-----------------------------------------------------')
    print("mock-bot is connected and running!")
    print("This feed is the background task one, not the main.")
    print('-----------------------------------------------------')

client.loop.create_task(my_background_task())
client.run('')