# pip install discord.py
# pip install neuralintents
# pip install dotenv
# pip install python-dotenv

import discord
import os
from dotenv import load_dotenv
from neuralintents import GenericAssistant

chatbot = GenericAssistant('intents.json')
chatbot.train_model()
chatbot.save_model()

print("Bot running...")

client = discord.Client()

load_dotenv()
TOKEN = os.getenv('TOKEN')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith("$aibot"):
        response = chatbot.request(message.content[7:])
        await message.channel.send(response)

client.run(TOKEN)