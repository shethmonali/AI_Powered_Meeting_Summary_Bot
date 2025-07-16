📋 AI-Powered Meeting Summarizer Bot


Overview
This project is an AI-powered meeting summarizer that uses OpenAI's GPT-3.5-turbo to generate concise summaries from raw meeting transcripts. Summaries are then automatically posted to a Microsoft Teams channel using a simple webhook integration.

Built in Python, this project helps reduce meeting fatigue and increases visibility into team decisions and action items — with no LangChain dependencies.

✨ Features ✨ 
✅ Generate summaries of meeting transcripts using GPT-3.5-turbo
✅ Extracts discussion points, decisions, and action items
✅ Sends summaries directly to a Microsoft Teams channel
✅ Simple and fast — built with pure OpenAI API (v1.0+)
✅ Designed to run locally or in production as a scheduled script

🛠 Tech Stack 🛠
Python 3.8+
OpenAI API (v1.0+)
Microsoft Teams Incoming Webhook
dotenv for secure config management


📁 Project Structure 📁 

meeting_summarizer/
│
├── data/
│   └── sample_meeting_transcript.txt       # Example input
│
├── src/
│   ├── summarizer.py                       # OpenAI summarization logic
│   ├── teams_integration.py                # Sends summary to Teams
│   └── utils.py                            # Helper for file loading
│
├── .env                                    # Environment variables (not committed)
├── main.py                                 # Run this to summarize & post to Teams
├── requirements.txt                        # Python dependencies
└── README.md


🔧 Setup Instructions 🔧

1. Clone the Repository
git clone https://github.com/yourusername/meeting-summarizer.git
cd meeting-summarizer

2. Install Dependencies
pip install -r requirements.txt

3. Create .env File
Create a .env file in the root directory:
		OPENAI_API_KEY=your_openai_api_key
		TEAMS_WEBHOOK_URL=https://outlook.office.com/webhook/your-webhook-url
		🔐 Note: Do not commit this file.

4. Add Your Transcript
Put your transcript in data/sample_meeting_transcript.txt or update the filename in main.py.

🚀 Run the Bot 🚀 
python main.py

This will:
		Read the transcript

		Summarize it using GPT-3.5-turbo

		Print it to the terminal

		Post it to your Microsoft Teams channel via webhook

💬 Example Output
Input Transcript:
Alice: Let's finalize the roadmap. Dev estimates needed by Monday.
Bob: I’ll handle that by Friday.
Carol: Marketing copy due Wednesday.
Teams Summary:
📋 Meeting Summary:

- Roadmap finalization discussed
- Bob to provide development estimates by Friday
- Carol to deliver marketing copy by Wednesday
- Follow-up actions noted for Monday review

📦 Requirements 📦 
openai>=1.0.0
python-dotenv
requests

Install with:
pip install -r requirements.txt


🚀 Future Enhancements 🚀 
Speech-to-text support using OpenAI Whisper
Streamlit UI for uploading and reviewing transcripts
Slack integration or email summaries
Multi-meeting batch summarization


🤝 Contributions 🤝 
PRs, issues, and ideas are welcome! Please open an issue to propose enhancements.
