from diffusers import AutoPipelineForText2Image
import torch
from discord.ext import commands
from constants import DIFFUSER_MODEL, DIFFUSSER_COMMAND_WORD
import discord
import random
import string

class diffuser_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.pipe = AutoPipelineForText2Image.from_pretrained(DIFFUSER_MODEL, torch_dtype=torch.float16, variant="fp16")
        self.pipe.to("cuda")
        print("diffusers_cog initalized")

    def diffuser_pipe(self, user_prompt):
        random_tag = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(10))
        file_path = f"images/{random_tag}.png"
        # if using torch < 2.0
        self.pipe.enable_xformers_memory_efficient_attention()
        image = self.pipe(prompt=user_prompt).images[0]
        image.save(file_path)

        return file_path
    
    @commands.command()
    async def diffuser(self, ctx):
        prompt = ctx.message.content[len(DIFFUSSER_COMMAND_WORD) + 1:]
        generating_message = await ctx.send("Generating...")
        
        print("diffuser activated, prompt = " + prompt)
        await ctx.send(prompt, file=discord.File(self.diffuser_pipe(prompt)))
        print("diffuser done")
        
        await generating_message.delete()

    @commands.command()
    async def diffuser_DEBUG(self, ctx):
        print("DEBUG")
        await ctx.message.channel.send("ECHO " + ctx.message.content)
