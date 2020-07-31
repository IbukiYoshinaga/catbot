import discord
from os.path import join, dirname
from dotenv import load_dotenv
import os
import asyncio
from wordcloud import WordCloud
from os import path

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
                CatClass = commands.Cat(message)
                await CatClass.Processing()

            if message.content.startswith("mention"):
                MentionClass = commands.Mention(message)
                await MentionClass.Processing()

            if message.content.startswith("cloud"):
                channel = message.channel
                channel_messages = await channel.history(limit=200).flatten()
                message_list = []
                for channel_message in channel_messages:
                    message_list.append(channel_message.content)
                message_list_str = " ".join(message_list)
                word_cloud = WordCloud(
                    font_path="/System/Library/Fonts/ヒラギノ明朝 ProN.ttc",
                    background_color="white",
                    width=900,
                    height=500,
                ).generate(message_list_str)
                word_cloud.to_file(path.join(path.dirname(__file__), "sample.png"))
                await channel.send(file=discord.File("./bot/sample.png"))


class BotInit(object):
    def __init__(self):
        self.token = os.environ.get("DISCORD_TOKEN")
        Router()

    def run(self):
        client.run(self.token)
