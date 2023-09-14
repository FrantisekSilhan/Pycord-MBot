import discord
from discord.ext import commands
import nekos
import random
import time
import requests

class FunCog(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.slash_command(name="cuddle", description="[Action] Cuddles a user")
  async def cuddle(self, ctx, member: discord.Member):
    url = nekos.img(random.choice(["cuddle", "hug"]))
    embed = discord.Embed()
    embed.set_author(name=f"{ctx.author} cuddles {member}", icon_url=ctx.author.avatar, url=url)
    embed.set_image(url=url)
    await ctx.respond(member.mention, embed=embed)

  @commands.slash_command(name="feed", description="[Action] Feeds a user")
  async def feed(self, ctx, member: discord.Member):
    url = nekos.img("feed")
    embed = discord.Embed()
    embed.set_author(name=f"{ctx.author} feeds {member}", icon_url=ctx.author.avatar, url=url)
    embed.set_image(url=url)
    await ctx.respond(member.mention, embed=embed)

  @commands.slash_command(name="kiss", description="[Action] Kisses a user")
  async def kiss(self, ctx, member: discord.Member):
    url = nekos.img("kiss")
    embed = discord.Embed()
    embed.set_author(name=f"{ctx.author} kisses {member}", icon_url=ctx.author.avatar, url=url)
    embed.set_image(url=url)
    await ctx.respond(member.mention, embed=embed)

  @commands.slash_command(name="pat", description="[Action] Pats a user")
  async def pat(self, ctx, member: discord.Member):
    url = nekos.img("pat")
    embed = discord.Embed()
    embed.set_author(name=f"{ctx.author} pats {member}", icon_url=ctx.author.avatar, url=url)
    embed.set_image(url=url)
    await ctx.respond(member.mention, embed=embed)

  @commands.slash_command(name="slap", description="[Action] Slaps a user")
  async def slap(self, ctx, member: discord.Member):
    url = nekos.img("slap")
    embed = discord.Embed()
    embed.set_author(name=f"{ctx.author} slaps {member}", icon_url=ctx.author.avatar, url=url)
    embed.set_image(url=url)
    await ctx.respond(member.mention, embed=embed)

  @commands.slash_command(name="spank", description="[Action] Spanks a user")
  async def spank(self, ctx, member: discord.Member):
    url = nekos.img("spank")
    embed = discord.Embed()
    embed.set_author(name=f"{ctx.author} spanks {member}", icon_url=ctx.author.avatar, url=url)
    embed.set_image(url=url)
    await ctx.respond(member.mention, embed=embed)

  @commands.slash_command(name="tickle", description="[Action] Tickles a user")
  async def tickle(self, ctx, member: discord.Member):
    url = nekos.img("tickle")
    embed = discord.Embed()
    embed.set_author(name=f"{ctx.author} tickles {member}", icon_url=ctx.author.avatar, url=url)
    embed.set_image(url=url)
    await ctx.respond(member.mention, embed=embed)

  @commands.slash_command(name="dollar", description="[Image] Sends 'every dollar spent on' pic")
  async def dollar(self, ctx):
    url = nekos.img("gecg")
    embed = discord.Embed()
    embed.set_author(name=f"{ctx.author}", icon_url=ctx.author.avatar, url=url)
    embed.set_image(url=url)
    await ctx.respond(embed=embed)

  @commands.slash_command(name="fox", description="[Image] Sends foxgirl pic")
  async def fox(self, ctx):
    url = nekos.img("fox_girl")
    embed = discord.Embed()
    embed.set_author(name=f"{ctx.author}", icon_url=ctx.author.avatar, url=url)
    embed.set_image(url=url)
    await ctx.respond(embed=embed)

  @commands.slash_command(name="gasm", description="[Image] Sends gasm pic")
  async def gasm(self, ctx):
    url = nekos.img("gasm")
    embed = discord.Embed()
    embed.set_author(name=f"{ctx.author}", icon_url=ctx.author.avatar, url=url)
    embed.set_image(url=url)
    await ctx.respond(embed=embed)

  @commands.slash_command(name="neko", description="[Image] Sends neko pic")
  async def neko(self, ctx):
    url = nekos.img("neko")
    embed = discord.Embed()
    embed.set_author(name=f"{ctx.author}", icon_url=ctx.author.avatar, url=url)
    embed.set_image(url=url)
    await ctx.respond(embed=embed)

  @commands.slash_command(name="ngif", description="[Image] Sends neko gif")
  async def ngif(self, ctx):
    url = nekos.img("ngif")
    embed = discord.Embed()
    embed.set_author(name=f"{ctx.author}", icon_url=ctx.author.avatar, url=url)
    embed.set_image(url=url)
    await ctx.respond(embed=embed)

  @commands.slash_command(name="smug", description="[Image] Sends smug gif")
  async def smug(self, ctx):
    url = nekos.img("smug")
    embed = discord.Embed()
    embed.set_author(name=f"{ctx.author}", icon_url=ctx.author.avatar, url=url)
    embed.set_image(url=url)
    await ctx.respond(embed=embed)

  @commands.slash_command(name="waifu", description="[Image] Sends waifu pic")
  async def waifu(self, ctx):
    url = nekos.img("waifu")
    embed = discord.Embed()
    embed.set_author(name=f"{ctx.author}", icon_url=ctx.author.avatar, url=url)
    embed.set_image(url=url)
    await ctx.respond(embed=embed)

  @commands.slash_command(name="lolitka", description="[Image] Sends lolitka pic")
  async def lolitka(self, ctx):
    url = "https://chino.is-a.dev/chino?timestamp=" + str(time.time())

    embed = discord.Embed()
    embed.set_author(name=f"{ctx.author}", icon_url=ctx.author.avatar, url=url)
    embed.set_image(url=url)
    await ctx.respond(embed=embed)

  @commands.slash_command(name="joke", description="Get a random ChatGPT joke")
  async def joke(self, ctx):
    url = "https://www.xdd.moe/joke"

    res = requests.get(url)

    if res.status_code == 200:
      joke_data = res.json()
      joke_id = joke_data.get("id")
      joke_text = joke_data.get("joke", "No joke available")
      joke_url = f"https://www.xdd.moe/joke?id={joke_id}"

      embed = discord.Embed()
      embed.set_author(name=f"{ctx.author}", icon_url=ctx.author.avatar, url=url)
      embed.add_field(name=f"Joke #{joke_id}", value=joke_text, inline=False)
      embed.add_field(name="Joke Link", value=f"[Click Here]({joke_url})")
      await ctx.respond(embed=embed)
    
    else:
      await ctx.respond("Mthia has skill issue (API error)")

def setup(client):
  client.add_cog(FunCog(client))
