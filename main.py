import os
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot online como {bot.user} ({bot.user.id})")

@bot.command(name="ping")
async def ping(ctx):
    await ctx.send("Pong! 🏓")

@bot.command(name="hello")
async def hello(ctx):
    await ctx.send(f"Olá, {ctx.author.mention}! 👋")

@bot.command(name="status")
async def status(ctx):
    await ctx.send("Bot funcionando corretamente! ✅")

TOKEN = os.getenv("DISCORD_TOKEN")
if not TOKEN:
    raise ValueError("A variável de ambiente DISCORD_TOKEN não foi definida.")

bot.run(TOKEN)
