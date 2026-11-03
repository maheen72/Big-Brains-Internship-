
import os
from dotenv import load_dotenv
from google import genai
from google.genai import types


# STEP 1: Create fictional student data
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


# STEP 2: Create our custom Python function
def get_student_result(student_id: str) -> dict:
    """
    Retrieve student information using a student ID.
    """

    print("\n[TOOL EXECUTED] Gemini requested student information.")

    student_id = student_id.strip().upper()

    if student_id in students:
        print("[DATABASE] Student record found.")

        return {
            "found": True,
            "student_id": student_id,
            **students[student_id]
        }

    print("[DATABASE] Student record not found.")

    return {
        "found": False,
        "message": "No student record exists for this ID."
    }


# STEP 3: Connect Python to Gemini
load_dotenv()  # Load environment variables from .env file
api_key = os.getenv("GENAI_API_KEY")

if not api_key:
    raise SystemExit(
        "API key missing. Please set GENAI_API_KEY first."
    )

client = genai.Client(api_key=api_key)


# STEP 4: Create the AI assistant
def run_assistant():

    print("================================")
    print("   STUDENT INFORMATION AI")
    print("================================")

    question = input("\nAsk your question: ")

    print("\n[AI] Processing your question...")

    try:
        response = client.models.generate_content(
            model="gemini-3.5-flash",

            contents=question,

            config=types.GenerateContentConfig(
                tools=[get_student_result],

                system_instruction=(
                    "You are a helpful university student assistant. "
                    "Use get_student_result whenever the user asks "
                    "for student records, marks, attendance or department. "
                    "Never invent student information. "
                    "If the tool reports that a student was not found, "
                    "clearly tell the user. "
                    "For general questions that do not require student "
                    "records, answer normally without using the tool."
                )
            )
        )

        print("\n========== FINAL AI RESPONSE ==========")
        print(response.text)
        print("=======================================")

    except Exception as error:
        print("\nAn error occurred:", error)


# STEP 5: Run the application
if __name__ == "__main__":
    run_assistant()
