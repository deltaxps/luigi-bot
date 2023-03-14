import discord
from discord.ext import commands
import random
import os
import pathlib
import json

bot = commands.Bot(
    command_prefix="l.",  # unused for now, given he only replies to you when you talk
    intents=discord.Intents.all(),
    case_insensitive=True,
)

with open(f"{os.path.realpath(os.path.dirname(__file__))}/backend/config.json") as file:
    config = json.load(file)


@bot.event
async def on_ready():
    os.system("cls" if os.name == "nt" else "clear")
    print("logged in")
    await bot.change_presence(status=discord.Status.dnd, activity=discord.Activity(type=discord.ActivityType.watching, name="super mario"))

@bot.event
async def on_message(msg):
    if msg.author.bot:
        return
    
    p = random.randint(1, 100)

    if "luigi" in msg.content.lower().replace(" ", ""):
        if p <= 1:  # ryan requested this response
            await msg.reply("go fuck yourself", mention_author=False)
            return

        if p <= 1:
            path = str(pathlib.Path(__file__).parent.absolute()) + "/data/secrets"
            img = os.path.join(path, "help.jpg")
            await msg.reply(file=discord.File(img), mention_author=False)
            return

        replies = []
        replies.clear()
        with open("data/data", "rt") as file:
            for line in file:
                replies.append(line)

        reply = replies[random.randrange(0, len(replies))]
        await msg.reply(reply, mention_author=False)


bot.run(config["token"])