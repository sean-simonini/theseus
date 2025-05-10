import os
import litellm
from litellm import completion

# Option 2: Environment variable (recommended)
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")


OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY is not set in the environment.")
print (OPENAI_API_KEY)
