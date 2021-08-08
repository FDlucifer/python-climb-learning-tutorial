# https://discord.com/developers/applications
# token: ODUwNjI0NzIzNzIxMjU2OTYw.YLscAQ.BxaT402X1unslGbZq_UL61bTFDY
# https://discord.com/api/oauth2/authorize?client_id=850624723721256960&permissions=2349067334&scope=bot
# pip install discord.py
# pip install -U python-dotenv
# pip install pandas-datareader

import discord
import os
from discord import channel
from dotenv import load_dotenv
import pandas_datareader as web

client = discord.Client()

load_dotenv()
TOKEN = "ODUwNjI0NzIzNzIxMjU2OTYw.YLscAQ.BxaT402X1unslGbZq_UL61bTFDY"

def get_stock_price(ticker):
    data = web.DataReader(ticker, "yahoo")
    return data['Close'].iloc[-1]

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send("hello fuck you and go away, bitch!")

    if message.content == '$private':
        await message.author.send("hello in private brother!")

    if message.content.startswith("$stockprice"):
        if len(message.content.split(" ")) == 2:
            ticker = message.content.split(" ")[1]
            price = get_stock_price(ticker)
            await message.channel.send(f"stock price of {ticker} is {price}")


@client.event
async def on_connect():
    print("bot connected to the server!")
    # channel = client.get_channel(703610564424761426)
    # await channel.send("just connected to vulhub-walkthrough!")

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(f"welcome to the server {member}!")


client.run(TOKEN)