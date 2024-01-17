from discord.ext import commands
from transformers import AutoModelForCausalLM, AutoTokenizer
from constants import LLM_MODEL, LLM_COMMAND_WORD

class llm_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.tokenizer = AutoTokenizer.from_pretrained(LLM_MODEL)
        self.model = AutoModelForCausalLM.from_pretrained(LLM_MODEL, trust_remote_code=True, device_map="auto")
        print("llm_cog initalized")


    def clean_response(self, llm_response, indicator):
        index = llm_response.rindex(indicator) + len(indicator)
        llm_response = llm_response[index:]
        return llm_response
    
    def llm_prompt(self, user_prompt):
        prompt = [{'role': 'user', 'content': user_prompt}]
        inputs = self.tokenizer.apply_chat_template(
            prompt,
            add_generation_prompt=True,
            return_tensors='pt'
        )

        tokens = self.model.generate(
            inputs.to(self.model.device),
            max_new_tokens=1024,
            temperature=0.8,
            do_sample=True
        )

        print(self.tokenizer.decode(tokens[0], skip_special_tokens=True))
        clean_response = self.clean_response(self.tokenizer.decode(tokens[0], skip_special_tokens=True), "<|assistant|>")
        return clean_response

    @commands.command()
    async def llm(self, ctx):
        prompt = ctx.message.content[len(LLM_COMMAND_WORD) + 1:]

        print("llm activated, prompt = " + prompt)
        await ctx.message.channel.send(self.llm_prompt(prompt))
        print("llm done")
