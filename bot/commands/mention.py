import asyncio
import discord


class Mention(object):
    def __init__(self, message):
        self.message = message

    async def Processing(self):
        mention_count = int(self.message.content.split(" ")[1])
        for count in range(mention_count):
            await self.message.channel.send(self.message.mentions[0].mention)

        await self.message.channel.send(self.message.author.mention + "メンション完了")
