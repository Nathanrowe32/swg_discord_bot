import discord
from discord.ext import commands
from constants import TOKEN
import asyncio

from build_bot_cog import build_bot_cog

intents = discord.Intents.all()
intents.members = True
intents.messages = True

bot = commands.Bot(command_prefix="!", intents=intents)

async def main():
    async with bot:
        await bot.add_cog(build_bot_cog(bot))
        await bot.start(TOKEN)

asyncio.run(main())

