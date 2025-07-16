import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

def summarize_meeting(transcript):
    """
    Summarizes a meeting transcript using OpenAI's GPT-3.5 via the new SDK (>=1.0.0).

    Args:
        transcript (str): The full meeting transcript.

    Returns:
        str: A summary of the transcript.
    """

    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    prompt = f"""
    You are an AI meeting assistant. Summarize the following meeting transcript.
    Your summary should include:
    - Main discussion points
    - Key decisions
    - Action items with owners and deadlines if mentioned

    Transcript:
    {transcript}

    Summary:
    """

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3
        )
        return response.choices[0].message.content.strip()

    except Exception as e:
        print(f"❌ Error calling OpenAI API: {e}")
        return "Error generating summary."
