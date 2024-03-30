# pip install discord.py

import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
TOKEN = open("TOKEN", "r").read()

@client.event
async def on_connect():
    print("Connected!")

@client.event
async def on_message(message):
    if message.content.startswitch("$neuralbot "):
        await message.channel.send("hello! you said: " + message.content[11:])

client.run(TOKEN)

