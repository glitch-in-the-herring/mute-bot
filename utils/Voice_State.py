import discord
from discord.ext import commands

class Voice_State(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.Cog.listener()
	async def on_ready(self):
		print("Bot has logged in")

	@commands.command()
	async def mute(self, ctx):
		"""Mutes everyone in the voice channel you are in right now."""
		try:
			voice_channel = ctx.author.voice.channel
			if ctx.author.permissions_in(voice_channel).mute_members:
				for user in voice_channel.members:
					if not user.voice.mute:
						await user.edit(mute=True)
				await ctx.send(f"Muted all users in {voice_channel.name}")
			else:
				await ctx.send("You do not have the permission to mute members!")
		except AttributeError:
			await ctx.send("You are not in a voice channel!")

	@commands.command()
	async def unmute(self, ctx):
		"""Unmutes everyone in the voice channel you are in right now."""
		try:
			voice_channel = ctx.author.voice.channel
			if ctx.author.permissions_in(voice_channel).mute_members:	
				for user in voice_channel.members:
					if user.voice.mute:
						await user.edit(mute=False)
				await ctx.send(f"Unmuted all users in {voice_channel.name}")
			else:
				await ctx.send("You do not have the permission to mute members!")					
		except AttributeError:
			await ctx.send("You are not in a voice channel!")

	@commands.command()
	async def deafen(self, ctx):
		"""Deafens everyone in the voice channel you are in right now."""
		try:
			voice_channel = ctx.author.voice.channel
			if ctx.author.permissions_in(voice_channel).deafen_members:
				for user in voice_channel.members:
					if not user.voice.deaf:
						await user.edit(deafen=True)
				await ctx.send(f"Deafened all users in {voice_channel.name}")
			else:
				await ctx.send("You do not have the permission to deafen members!")						
		except AttributeError:
			await ctx.send("You are not in a voice channel!")

	@commands.command()
	async def undeafen(self, ctx):
		"""Undeafens everyone in the voice channel you are in right now."""
		try:
			voice_channel = ctx.author.voice.channel
			if ctx.author.permissions_in(voice_channel).deafen_members:
				for user in voice_channel.members:
					if user.voice.deaf:
						await user.edit(deafen=False)
				await ctx.send(f"Undeafened all users in {voice_channel.name}")
			else:
				await ctx.send("You do not have the permission to deafen members!")	
		except AttributeError:
			await ctx.send("You are not in a voice channel!")

def setup(bot):
    bot.add_cog(Voice_State(bot))