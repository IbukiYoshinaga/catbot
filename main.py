import discord
import asyncio
import sys
import os
from bot.bot_init import BotInit


def init():
    BotInit()


if __name__ == "__main__":
    bot_init = BotInit()
    bot_init.run()


@client.event
async def on_ready():
    print("---")
    print(client.user.id)
    print(client.user.name)
    print("---")
