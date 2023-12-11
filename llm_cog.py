#import required dependencies
from discord.ext import commands
import asyncio

class llm_cog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        print("created worker")
    

    # Print when the bot is online.
    @commands.Cog.listener()
    async def on_ready(self):
        print("{0.user} IS ONLINE." .format(self.bot.client))
        # await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="!commands"))

    @commands.command(name="copyme", help="Change bot prefix")
    async def on_message(self, message):

        # check if message is from bot
        if (message.author != self.bot.client.user):
            print(f"{message.channel} -> {message.author} said: {message.content}")
            await message.channel.send(f"{message.channel} -> {message.author} said: {message.content}")

        await self.bot.client.process_commands(message)

    @commands.command()
    async def llm(self, ctx):

        # check if message is from bot
        if (ctx.message.author != self.bot.client.user):
            print(f"Helping")
            await ctx.message.channel.send(f"What do you need assistance with {ctx.message.author}?")
            