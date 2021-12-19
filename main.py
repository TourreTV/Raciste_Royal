# bot.py
import os
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('Nzc4NjEzOTcyMzY1NjA2OTU0.X7UixA.4m1b6RupgdiBo5LJHjEEOaE17K8')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

client.run(TOKEN)