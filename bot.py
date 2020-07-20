#!/usr/bin/env python3

# main.py
# import os
# from dotenv import load_dotenv

import discord

# load_dotenv()
# TOKEN = os.getenv('DISCORD_TOKEN')

TOKEN = '3_dZqTomzkhktDK0ECa8sTViZAUH9Rmr'

client = discord.Client()

@client.event
async def on_ready():
    print("The bot is ready!")
    await client.change_presence(game=discord.Game(name="Making a bot"))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == "Hello":
        await client.send_message(message.channel, "World")

client.run(TOKEN)
