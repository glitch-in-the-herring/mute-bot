import os, argparse
import discord
from discord.ext import commands
description = "Mutes and unmutes everyone in a voice channel"

parser = argparse.ArgumentParser()
parser.add_argument("-t", "--token", metavar='TOKEN', help="Bot token. Keep this secret")
args = parser.parse_args()
token = args.token

bot = commands.Bot(command_prefix='$')

@bot.event()
async def on_ready():
	print("Bot has logged in")

@bot.command
async def load(ctx, extension):
	bot.load_extension(f"utils.{extension}")

@bot.command
async def unload(ctx, extension):
	bot.unload_extension(f"utils.{extension}")

for filename in os.listdir("./utils"):
	if filename.endswith(".py"):
		bot.load_extension(f"utils.{filename[:-3]}")

bot.run(token)