# Student Info Voice Agent

This application is a real-time, streaming conversational agent (text and audio) that answers questions about a student based on the contents of a text file. It uses Google Gemini and ADK for the agent, and FastAPI for the backend.

## Features
- Real-time voice and text chat with an AI agent
- Agent answers questions using only the information in `app/student_info.txt`
- No calendar or external tool integration

## Usage
1. Place your student information in `app/student_info.txt` (created automatically if missing).
2. Start the FastAPI server (see below).
3. Open the web app in your browser.
4. Chat with the agent using text or voice. The agent will only answer based on the info in the text file.

## Setup
- Python 3.9+
- Install dependencies:
  ```
  pip install -r requirements.txt
  ```
- Set up your Gemini API key in a `.env` file:
  ```
  GEMINI_API_KEY=your-key-here
  ```
- Run the app:
  ```
  uvicorn app.main:app --reload
  ```

## Customization
- Edit the instruction prompt in `app/jarvis/agent.py` to change the agent's behavior.
- Update `app/student_info.txt` with the student's information.

## License
MIT
