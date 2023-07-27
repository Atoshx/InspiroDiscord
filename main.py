import discord
from discord.ext import commands
import requests
import shutil
import io
import uuid
import os

intents = discord.Intents.all()

bot = commands.Bot(command_prefix = '$', intents=intents)

def getImgReq():
    link = "http://inspirobot.me/api?generate=true"
    f = requests.get(link)
    imgurl = f.text

    response = requests.get(imgurl, stream=True)
    file = io.BytesIO(response.content)

    filename = str(uuid.uuid4()) + '.jpg'  # generates a random unique filename
    with open(filename, 'wb') as out_file:
        shutil.copyfileobj(file, out_file)

    return filename
    del filename

@bot.event
async def ready():
    print(f"LOGGED IN AS {bot.user.name}")

@bot.command()
async def inspire(ctx):
    inspQuote = getImgReq()
    await ctx.send("Your newly created **MOTIVATIONAL QUOTE**", file=discord.File(inspQuote))
    os.remove(inspQuote)


bot.run(INSERT_TOKEN_HERE)




