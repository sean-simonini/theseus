from LLM.key import OPENAI_API_KEY
import openai

openai.api_key = OPENAI_API_KEY

import yaml

# Update the file path to the new location
with open("/Users/seanfurbush/Documents/GitHub/theseus/.venv/config.yaml", "r") as file:
    config = yaml.safe_load(file)
    print(config)  # Ensure this prints a valid dictionary