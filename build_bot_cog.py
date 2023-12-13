import discord
from discord.ext import commands

class build_bot_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print("build_bot_cog initalized")