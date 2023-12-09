from transformers import AutoModelForCausalLM, AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained('stabilityai/stablelm-zephyr-3b')
model = AutoModelForCausalLM.from_pretrained(
    'stabilityai/stablelm-zephyr-3b',
    trust_remote_code=True,
    device_map="auto"
)

user_input = ""
while (user_input != "X"):

    user_input = str(input("say something to clyde or 'X' to exit.").upper())

    if (user_input != "X"):
        prompt = [{'role': 'user', 'content': user_input}]
        inputs = tokenizer.apply_chat_template(
            prompt,
            add_generation_prompt=True,
            return_tensors='pt'
        )

        tokens = model.generate(
            inputs.to(model.device),
            max_new_tokens=1024,
            temperature=0.8,
            do_sample=True
        )

        print(tokenizer.decode(tokens[0], skip_special_tokens=True))
