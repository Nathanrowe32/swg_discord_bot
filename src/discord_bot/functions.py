import discord
from constants import *

#disconnects bot from voice channel.
async def disconnectBot(client):
    voice = discord.utils.get(client.voice_clients)
    #checks to see if the bot was in a channel, if not do nothing.
    if voice:
        await voice.disconnect()
