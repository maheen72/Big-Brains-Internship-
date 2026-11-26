import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

# Creating Student Database

students = {
    "STU-101": {
        "name": "Ali",
        "marks": 85,
        "attendance": 92,
        "department": "Artificial Intelligence"
    },
    "STU-102": {
        "name": "Sara",
        "marks": 90,
        "attendance": 96,
        "department": "Computer Science"
    },
    "STU-103": {
        "name": "Ahmed",
        "marks": 72,
        "attendance": 80,
        "department": "Software Engineering"
    }
}

# Student Information Retrieval Tool

def get_student_result(student_id: str) -> dict:
    """
    Retrieves student information using their ID.
    """

    student_id = student_id.strip().upper()

    print(f"\n[TOOL EXECUTED] Searching for {student_id}...")

    if not student_id:
        return {
            "found": False,
            "message": "Student ID cannot be empty."
        }

    student = students.get(student_id)

    if student:
        return {
            "found": True,
            "student_id": student_id,
            "student": student
        }

    return {
        "found": False,
        "student_id": student_id,
        "message": f"No student found with ID {student_id}."
    }

# Load Environment Variables

load_dotenv()

api_key = os.getenv("GENAI_API_KEY")

if not api_key:
    raise ValueError(
        "GENAI_API_KEY is missing. Please check your .env file."
    )

# Connect to Gemini
client = genai.Client(api_key=api_key)
MODEL_NAME = "gemini-3.5-flash"

# AI Assistant
def run_assistant():

    print("\n===================================")
    print("     STUDENT INFORMATION AI")
    print("===================================")
    print("Ask questions about student records.")
    print("Type 'exit' to close the assistant.\n")

    while True:

        question = input("You: ").strip()

        # Check for empty input
        if not question:
            print("Please enter a question.\n")
            continue

        # Exit the assistant
        if question.lower() in ["exit", "quit", "bye"]:
            print("Assistant: Goodbye! Have a great day.")
            break

        try:

            response = client.models.generate_content(
                model=MODEL_NAME,
                contents=question,

                config=types.GenerateContentConfig(

                    tools=[get_student_result],

                    system_instruction="""
                    You are a helpful Student Information Assistant.

                    Your responsibilities:

                    1. Use get_student_result whenever the user
                       asks about a student's marks, attendance,
                       department, or personal academic record.

                    2. Never invent student information.

                    3. If a student ID is not found, clearly
                       explain that the record does not exist.

                    4. Only provide information returned by
                       the student database.

                    5. Answer general questions without using
                       the student database.

                    6. Keep your answers clear, friendly,
                       and easy to understand.
                    """,

                    temperature=0.2
                )
            )

            # Display the AI response
            if response.text:
                print(f"\nAssistant: {response.text}\n")
            else:
                print("\nAssistant: I couldn't generate a response. Please try again.\n")

        except Exception as error:

            print("\nSomething went wrong.")
            print(f"Error: {error}\n")

# Run the Program

if __name__ == "__main__":
    run_assistant()
