<h1> **swg_discord_bot** </h1>

launch a localized llm & diffuser models into discord using bots

<h1> Installation </h1>

1. Clone the repository: `git clone 'https://github.com/Nathanrowe32/swg_discord_bot.git'`
2. Create a virtual environment: `python -m venv .venv`
3. Activate the virtual environment: `.venv/Scripts/Activate` for windows
4. Install dependencies: `pip install -r requirements.txt`
5. Configure 'config.json' by adding discord bot token, and changing to preferred model.
  -  Discord Developer Portal (https://discord.com/login?redirect_to=%2Fdevelopers/)
  -  Hugging Face (https://huggingface.co/)

<h1> Usage </h1>

Discord commands to run on discord server bot is deployed on.

1. Run `python main.py`
2. After ensuring the bot is online, the llm and/or diffuser must be turned on.
   `!activate_llm` // turn on llm model
   `!deactivate_llm` // turn off llm model
   `!activate_diffuser` // turn on diffuser model
   `!deactivate_diffuser` // turn off diffuser model
3. Run llm model with `!llm PROMPT`
4. Run diffuser model with `!diffuser PROMPT`

<h2> Notes </h2>
Chose to turn on/off models for efficiency; when both on it slows down compute time significantly.
LLM model is 3B parameters, found OK results.
Diffuser model is stabilityai/sdxl-turbo, found POOR results. (Did not do too much tuning/testing in this area however)
