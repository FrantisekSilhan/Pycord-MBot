import discord
from discord.ext import commands
import nekos
import random

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

def setup(client):
  client.add_cog(FunCog(client))