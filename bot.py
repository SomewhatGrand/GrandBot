import discord
from discord.ext import commands
import os

# Bot setup
TOKEN = os.getenv("DISCORD_TOKEN")  # This fetches the token from the environment variable
intents = discord.Intents.default()
intents.messages = True

bot = commands.Bot(command_prefix="!", intents=intents)

# When bot is ready
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

# Simple command
@bot.command()
async def hello(ctx):
    await ctx.send("Hello! I'm alive! 🚀")

# Run the bot
bot.run(TOKEN)
