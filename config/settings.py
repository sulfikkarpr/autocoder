import os

# --- Hugging Face API Configuration ---
HF_API_TOKEN = "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"  # Replace with your actual token

# --- Code Generation Settings ---
DEFAULT_CODE_MODEL = "bigcode/starcoder2-15b-instruct-v0.1"
MAX_TOKENS = 1024
CODE_GENERATION_TEMPERATURE = 0.5

# --- File Management Settings ---
DEFAULT_SAVE_DIRECTORY = "generated_code"
DEFAULT_FILE_EXTENSION = ".py"

# --- Other Configuration ---
UI_TITLE = "AutoCoder Prototype"
EXECUTE_CODE = True

# Set environment variable for Hugging Face API
os.environ["HF_API_TOKEN"] = HF_API_TOKEN

# ... rest of your code to utilize the configuration ...