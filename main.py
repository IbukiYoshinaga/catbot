import discord
import asyncio
import sys
import cv2
import numpy as np
import os
from bot.bot_init import BotInit


def init():
    BotInit()


if __name__ == "__main__":
    bot_init = BotInit()
    bot_init.run()

Parts = {
    "head": "./assets/cat/cathead.png",
    "body": "./assets/cat/catbody.png",
    "foot": "./assets/cat/catfoot.png",
}


@client.event
async def on_ready():
    print("---")
    print(client.user.id)
    print(client.user.name)
    print("---")


@client.event
async def on_message(message):
    if message.author.id != client.user.id:
        if message.content.startswith("cat"):
            await message.channel.send("にゃーん")

            Message = message.content.split("_")

            Num = Message[1]
            catHead = cv2.imread(Parts["head"])
            catBody = cv2.imread(Parts["body"])
            catfoot = cv2.imread(Parts["foot"])

            catBodyLoop = np.tile(catBody, (int(Num), 1, 1))
            catImg = cv2.vconcat([catHead, catBodyLoop, catfoot])
            cv2.imwrite("./assets/cat/catlink.png", catImg)

            await message.channel.send(file=discord.File("./assets/cat/catlink.png"))

        if message.content == "bye":
            sys.exit()
