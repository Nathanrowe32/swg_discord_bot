from os import path
import json

CONFIG_PATH =  str(path.abspath(path.join(__file__ ,".."))).replace('\\', '/') + "/config.json"

with open(CONFIG_PATH) as json_file:
    json_decoded = json.load(json_file)

TOKEN = json_decoded.get('token')
USER_ID = json_decoded.get('user_id')
LLM_MODEL = json_decoded.get('llm_model')
DIFFUSER_MODEL = json_decoded.get('diffuser_model')

AUDIO_SOURCE_FILE = ""
LLM_COMMAND_WORD = "!llm"
DIFFUSSER_COMMAND_WORD = "!diffuser"