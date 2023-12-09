#import required dependencies
from discord.ext import commands
from functions import *
#from ../llm import *

intents = discord.Intents.all()
intents.members = True
intents.messages = True

#! is the command prefix to run commands.
client = commands.Bot(command_prefix = '!', intents=intents)

# Print when the bot is online.
@client.event
async def on_ready():
    print("{0.user} IS ONLINE." .format(client))
    # await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="!commands"))

@client.event
async def on_message(message):

    # check if message is from bot
    if (message.author != client.user):
        print(f"{message.channel} -> {message.author} said: {message.content}")
        await message.channel.send(f"{message.channel} -> {message.author} said: {message.content}")

    await client.process_commands(message)

@client.command()
async def llm(ctx):

    # check if message is from bot
    if (ctx.message.author != client.user):
        print(f"Helping")
        await ctx.message.channel.send(f"What do you need assistance with {ctx.message.author}?")
        
    #await client.process_commands(ctx)

client.run(TOKEN)
