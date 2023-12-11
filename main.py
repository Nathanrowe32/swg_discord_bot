import discord
from discord.ext import commands
from constants import *
import json, os, asyncio

from llm_cog import llm_cog

with open(CONFIG_PATH) as json_file:
    json_decoded = json.load(json_file)
token = json_decoded.get('token')
user_id = json_decoded.get('user_id')

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

async def main():
    async with bot:
        await bot.add_cog(llm_cog(bot))
        await bot.start(token)

asyncio.run(main())

