from utils import load_meeting_transcript
from summarizer import summarize_meeting
from teams_integration import send_summary_to_teams

def main():
    transcript = load_meeting_transcript('data/sample_meeting_transcript.txt')
    summary = summarize_meeting(transcript)

    print("\n📋 Meeting Summary:\n")
    print(summary)

    send_summary_to_teams(summary)

if __name__ == "__main__":
    main()
