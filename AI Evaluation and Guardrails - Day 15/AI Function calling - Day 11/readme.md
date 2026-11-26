
# Student Information AI Assistant

## Project Overview
The Student Information AI Assistant is a Python-based AI application that uses Google's Gemini API and Function Calling to retrieve student information from a fictional database.

Users can ask questions in natural language, such as asking about a student's marks, attendance, or department. Gemini understands the question and decides when to call a custom Python function to retrieve the required information.

## Technologies Used
- Python
- Google Gemini API
- Google Gen AI SDK
- Python-dotenv
- VS Code

## Project Features
- Answers student-related questions.
- Retrieves student marks and attendance.
- Provides student department information.
- Uses custom Python function calling.
- Handles invalid student IDs.
- Answers general questions without accessing the student database.
- Uses fictional student records for testing.

## Student Database

The project contains the following fictional student records:

| Student ID | Name | Marks | Attendance | Department |
|---|---|---|---|---|
| STU-101 | Ali | 85 | 92% | Artificial Intelligence |
| STU-102 | Sara | 90 | 96% | Computer Science |
| STU-103 | Ahmed | 72 | 80% | Software Engineering |

## How Function Calling Works

1. The user enters a question.
2. Gemini analyzes the question.
3. If student information is required, Gemini calls the custom Python function `get_student_result()`.
4. The function searches the student database using the student ID.
5. The function returns the requested information to Gemini.
6. Gemini generates a final response for the user.

For general questions, Gemini can answer without calling the custom function.

## Installation

### Step 1: Install Python packages

```bash
pip install google-genai python-dotenv
```

### Step 2: Configure the API Key

Create a `.env` file in the project folder.

Add your Gemini API key:

```env
GENAI_API_KEY=your_actual_api_key
```

Do not upload your `.env` file or share your API key publicly.

### Step 3: Run the Project

Open the project folder in VS Code and run:

```bash
python main.py
```

## Test Cases

| Test | User Question | Expected Result |
|---|---|---|
| 1 | What are the marks of STU-101? | Ali's marks: 85 |
| 2 | What is the attendance of STU-102? | Sara's attendance: 96% |
| 3 | Which department does STU-103 belong to? | Software Engineering |
| 4 | Find STU-999. | Student record not found |
| 5 | What is Artificial Intelligence? | General AI-generated answer without database lookup |

## Project Structure

```text
AI Function calling - Day 11/
│
├── main.py
├── .env
└── README.md
```

## Learning Outcomes

Through this project, I learned:

- How to connect Python applications with the Gemini API.
- How to create custom Python functions.
- How AI models use function calling to interact with external tools.
- How to retrieve information from a local database.
- How to handle invalid inputs.
- How to distinguish between questions requiring tools and general questions.

## Author
AI Student | Big Brains Internship
