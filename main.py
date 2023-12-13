import discord
from discord.ext import commands
from constants import *
import json, asyncio

from llm_cog import llm_cog
from build_bot_cog import build_bot_cog

with open(CONFIG_PATH) as json_file:
    json_decoded = json.load(json_file)

token = json_decoded.get('token')
user_id = json_decoded.get('user_id')
model = json_decoded.get('model')

intents = discord.Intents.all()
intents.members = True
intents.messages = True

bot = commands.Bot(command_prefix="!", intents=intents)

async def main():
    async with bot:
        await bot.add_cog(build_bot_cog(bot))
        await bot.add_cog(llm_cog(bot, model))
        await bot.start(token)

asyncio.run(main())

