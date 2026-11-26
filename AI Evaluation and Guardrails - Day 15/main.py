
import os

from dotenv import load_dotenv
from google import genai
from google.genai import types


# Load API key
load_dotenv()

API_KEY = os.getenv("GENAI_API_KEY")

if not API_KEY:
    raise ValueError("Gemini API key not found. Check .env file.")

# Connect to Gemini
client = genai.Client(api_key=API_KEY)

MODEL = "gemini-3.8-flash"


# Student Knowledge Base
STUDENTS = {

    "STU-101": {
        "name": "Ali",
        "marks": 85,
        "attendance": 92,
        "department": "AI"
    },

    "STU-102": {
        "name": "Sara",
        "marks": 90,
        "attendance": 96,
        "department": "CS"
    },

    "STU-103": {
        "name": "Ahmed",
        "marks": 72,
        "attendance": 80,
        "department": "SE"
    }

}


# Convert database into text for Gemini
KNOWLEDGE_BASE = str(STUDENTS)


# Ask Gemini without guardrail
def ask_ai(question):

    instruction = """
    You are a helpful Student Information Assistant.
    Answer using the provided student records.
    """

    try:

        response = client.models.generate_content(
            model=MODEL,
            contents=f"""
            Student Records:
            {KNOWLEDGE_BASE}

            Question: {question}
            """,
            config=types.GenerateContentConfig(
                system_instruction=instruction
            )
        )

        return response.text or "No response received."

    except Exception as error:

        print("\nGemini API temporarily unavailable:", error)

        return "API_ERROR: Gemini is temporarily unavailable."


# Local Guardrail Function
def guarded_answer(question):

    question = question.lower()

    student_id = None

    # Find student ID in the question
    for sid in STUDENTS:

        if sid.lower() in question:
            student_id = sid
            break

    # Find student by name if ID is not provided
    if student_id is None:

        for sid, details in STUDENTS.items():

            if details["name"].lower() in question:
                student_id = sid
                break

    # Refuse if student does not exist
    if student_id is None:

        return "I don't have enough information to answer that."

    student = STUDENTS[student_id]

    # Answer only supported questions
    if "name" in question:

        return f"The name of {student_id} is {student['name']}."

    elif "marks" in question:

        return f"The marks of {student_id} are {student['marks']}."

    elif "attendance" in question:

        return f"The attendance of {student_id} is {student['attendance']}%."

    elif "department" in question:

        return f"The department of {student_id} is {student['department']}."

    else:

        return "I don't have enough information to answer that."


# Test Before Guardrail
print("\n===== BEFORE GUARDRAIL =====")

test_question = "What is the name of student STU-999?"

before_answer = ask_ai(test_question)

print("Question:", test_question)
print("AI Answer:", before_answer)


# Test After Guardrail
print("\n===== AFTER GUARDRAIL =====")

after_answer = guarded_answer(test_question)

print("Question:", test_question)
print("AI Answer:", after_answer)


# Evaluation Dataset
test_cases = [

    {
        "question": "What is the name of STU-101?",
        "expected": "The name of STU-101 is Ali."
    },

    {
        "question": "What are the marks of STU-102?",
        "expected": "The marks of STU-102 are 90."
    },

    {
        "question": "What is the department of STU-103?",
        "expected": "The department of STU-103 is SE."
    },

    {
        "question": "What is the name of STU-999?",
        "expected": "I don't have enough information to answer that."
    },

    {
        "question": "Which university does Ali attend?",
        "expected": "I don't have enough information to answer that."
    }

]


# Evaluate AI Responses
def evaluate_response(actual, expected):

    return actual.strip().lower() == expected.strip().lower()


# Run Evaluation Tests
print("\n===== AI EVALUATION RESULTS =====")

correct = 0
total = len(test_cases)

for number, test in enumerate(test_cases, start=1):

    print("\nTest Number:", number)

    # Get answer using guardrail
    actual_answer = guarded_answer(test["question"])

    # Compare expected and actual answers
    result = evaluate_response(
        actual_answer,
        test["expected"]
    )

    if result:

        status = "PASS"
        correct += 1

    else:

        status = "FAIL"

    print("Question:", test["question"])

    print("Expected Answer:", test["expected"])

    print("Actual AI Answer:", actual_answer)

    print("Result:", status)


# Calculate Evaluation Score
accuracy = (correct / total) * 100

print("\n===== FINAL EVALUATION =====")

print("Total Questions:", total)

print("Correct Responses:", correct)

print("Incorrect Responses:", total - correct)

print("Evaluation Score:", accuracy, "%")

print("\nAI Evaluation and Guardrail Testing Completed!")
