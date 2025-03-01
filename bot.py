import discord
from discord.ext import commands

TOKEN = "MTI5MDA1MjEwNjk5MjA5MTI0Nw.GcOnfG.jeyc4xQm7828NEKTNQoMf6iQ02cnPFmO4vDFlo"
intents = discord.Intents.default()
intents.messages = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.command()
async def hello(ctx):
    await ctx.send("Hello! I'm alive! 🚀")

bot.run(TOKEN)
