import discord
from os.path import join, dirname
from dotenv import load_dotenv
import os
import asyncio

from . import commands

# envの読み込み
load_dotenv(verbose=True)
dotenv_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path)

client = discord.Client()

# 起動時のconfig
@client.event
async def on_ready():
    print("---")
    print(client.user.id)
    print(client.user.name)
    print("---")


class Router(object):
    @client.event
    async def on_message(message):
        if message.author.id != client.user.id:
            if message.content.startswith("cat"):
                commands.Cat()


class BotInit(object):
    def __init__(self):
        self.token = os.environ.get("DISCORD_TOKEN")
        Router()

    def run(self):
        client.run(self.token)
