import asyncio
import discord
import cv2
import numpy as np


Parts = {
    "head": "./assets/cat/cathead.png",
    "body": "./assets/cat/catbody.png",
    "foot": "./assets/cat/catfoot.png",
}


class Cat(object):
    def __init__(self, message):
        self.message = message

    async def Processing(self):
        await self.message.channel.send("にゃーん")

        Message = self.message.content.split("_")

        Num = Message[1]
        catHead = cv2.imread(Parts["head"])
        catBody = cv2.imread(Parts["body"])
        catfoot = cv2.imread(Parts["foot"])

        catBodyLoop = np.tile(catBody, (int(Num), 1, 1))
        catImg = cv2.vconcat([catHead, catBodyLoop, catfoot])
        cv2.imwrite("./assets/cat/catlink.png", catImg)

        await self.message.channel.send(file=discord.File("./assets/cat/catlink.png"))
