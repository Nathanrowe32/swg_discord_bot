from discord.ext import commands
from constants import LLM_COMMAND_WORD
from ollama import ChatResponse, chat 

class llm_cog(commands.Cog):
    def __init__(self, bot):
        print("llm_cog initalizing")
        self.bot = bot

    # fix clean_response to remove thinking
    def clean_response(self, llm_response, indicator):
        index = llm_response.rindex(indicator) + len(indicator)
        llm_response = llm_response[index:]
        return llm_response
    
    def llm_prompt(self, user_prompt):
        response: ChatResponse = chat(model='deepseek-r1', messages=[
            {
                'role': 'user',
                'content': user_prompt,
            },
        ])
        response = response['message']['content']
        return response

    @commands.command()
    async def llm(self, ctx):
        prompt = ctx.message.content[len(LLM_COMMAND_WORD) + 1:]

        print("llm activated, prompt = " + prompt)
        await ctx.message.channel.send(self.llm_prompt(prompt))
        print("llm done")
