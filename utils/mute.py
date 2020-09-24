import discord
from discord.ext import commands

class Mute(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def mute(self, ctx):
		voice_channel = ctx.author.voice.channel
		if voice_channel != None:
			for user in voice_channel.members:
				if not user.voice.mute:
					await user.edit(mute=True)
			await ctx.send(f"Muted all users in {voice_channel.name}")
		else:
			await ctx.send("You are not in a voice channel!")

	@commands.command()
	async def unmute(self, ctx):
		voice_channel = ctx.author.voice.channel
		if voice_channel != None:
			for user in voice_channel.members:
				if user.voice.mute:
					await user.edit(mute=False)
			await ctx.send(f"Unmuted all users in {voice_channel.name}")
		else:
			await ctx.send("You are not in a voice channel!")	

def setup(bot):
    bot.add_cog(Mute(bot))