from discord.ext import commands
from transformers import AutoModelForCausalLM, AutoTokenizer

class llm_cog(commands.Cog):
    def __init__(self, bot, model):
        self.bot = bot
        self.tokenizer = AutoTokenizer.from_pretrained(model)
        self.model = AutoModelForCausalLM.from_pretrained(model, trust_remote_code=True, device_map="auto")
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
        print("llm activated, prompt = " + ctx.message.content)
        await ctx.message.channel.send(self.llm_prompt(ctx.message.content[4:]))
        print("llm done")
    
    @commands.command()
    async def DEBUG(self, ctx):
        print("DEBUG")
        await ctx.message.channel.send("ECHO " + ctx.message.content)
