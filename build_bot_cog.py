from discord.ext import commands
from constants import LLM_MODEL, DIFFUSER_MODEL

from llm_cog import llm_cog
from diffuser_cog import diffuser_cog

class build_bot_cog(commands.Cog):

    def __init__(self, bot):
        print("build_bot_cog initalizing")
        self.bot = bot
    
    @commands.command()
    async def q(self, ctx):
        print("exiting bot")
        exit(0)

    @commands.command()
    async def DEBUG(self, ctx):
        print("DEBUG")
        await ctx.message.channel.send("ECHO: " + ctx.message.content[7:])

    @commands.command()
    async def activate_llm(self, ctx):
        await self.bot.add_cog(llm_cog(self.bot))
        print(LLM_MODEL + " has been activated.")
    
    @commands.command()
    async def deactivate_llm(self, ctx):
        await self.bot.remove_cog("llm_cog")
        print(LLM_MODEL + " has been deactivated.")

    @commands.command()
    async def activate_diffuser(self, ctx):
        await self.bot.add_cog(diffuser_cog(self.bot))
        print(DIFFUSER_MODEL + " has been activated.")
    
    @commands.command()
    async def deactivate_diffuser(self, ctx):
        await self.bot.remove_cog("diffuser_cog")
        print(DIFFUSER_MODEL + " has been deactivated.")
    

    