import os
from dotenv import load_dotenv

def load_api_key():
    load_dotenv()
    return os.getenv("OPENAI_API_KEY")

def load_meeting_transcript(file_path):
    with open(file_path, 'r') as file:
        return file.read()
