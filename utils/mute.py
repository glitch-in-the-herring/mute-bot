import discord
from discord.ext import commands

class Mute(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def mute(self, ctx):
		try:
			voice_channel = ctx.author.voice.channel
			for user in voice_channel.members:
			if not user.voice.mute:
				await user.edit(mute=True)
			await ctx.send(f"Muted all users in {voice_channel.name}")
		except AttributeError:
			await ctx.send("You are not in a voice channel!")

	@commands.command()
	async def unmute(self, ctx):
		try:
			voice_channel = ctx.author.voice.channel
			for user in voice_channel.members:
			if user.voice.mute:
				await user.edit(mute=False)
			await ctx.send(f"Unmuted all users in {voice_channel.name}")
		except AttributeError:
			await ctx.send("You are not in a voice channel!")

def setup(bot):
    bot.add_cog(Mute(bot))