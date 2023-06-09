import os, json, discord
from discord.ext import commands

from dotenv import load_dotenv
load_dotenv()

client = commands.Bot()

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")

client.run(os.environ["TOKEN"])