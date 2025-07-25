from google.adk.agents import Agent
import os

# Load student info from a text file
STUDENT_INFO_PATH = os.path.join(os.path.dirname(__file__), '..', 'student_info.txt')
try:
    with open(STUDENT_INFO_PATH, 'r') as f:
        student_info = f.read()
except FileNotFoundError:
    student_info = "Student information file not found."

root_agent = Agent(
    name="student_info_agent",
    model="gemini-2.0-flash-exp",
    description="Agent that answers questions about a student based on a text file.",
    instruction=f"""
    You are a helpful assistant. Answer questions and have conversations based ONLY on the following information about a student. If you do not know the answer from the information, say you don't know.

    ---
    STUDENT INFO:
    {student_info}
    ---
    """,
    tools=[],
)
