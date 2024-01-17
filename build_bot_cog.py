from discord.ext import commands
from constants import LLM_MODEL, DIFFUSER_MODEL

from llm_cog import llm_cog
from diffuser_cog import diffuser_cog

class build_bot_cog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        print("build_bot_cog initalized")
    
    @commands.command()
    async def q(self, ctx):
        print("Bot shutting down")
        exit(0)

    @commands.command()
    async def DEBUG(self, ctx):
        print("DEBUG")
        await ctx.message.channel.send("ECHO: " + ctx.message.content[7:])

    @commands.command()
    async def activate_llm(self, ctx):
        print("Building LLM cog")
        await self.bot.add_cog(llm_cog(self.bot))
        await ctx.send(LLM_MODEL + " has been activated.")
    
    @commands.command()
    async def deactivate_llm(self, ctx):
        print("Deactivating LLM cog")
        await self.bot.remove_cog("llm_cog")
        await ctx.send(LLM_MODEL + " has been deactivated.")

    @commands.command()
    async def activate_diffuser(self, ctx):
        print("Building diffuser cog")
        await self.bot.add_cog(diffuser_cog(self.bot))
        await ctx.send(DIFFUSER_MODEL + " has been activated.")
    
    @commands.command()
    async def deactivate_diffuser(self, ctx):
        print("Deactivating diffuser cog")
        await self.bot.remove_cog("diffuser_cog")
        await ctx.send(DIFFUSER_MODEL + " has been deactivated.")
    

    