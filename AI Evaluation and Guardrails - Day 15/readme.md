
# AI Evaluation and Guardrails – Day 15

## Project Overview

This project demonstrates AI evaluation, hallucinations, and guardrails using Python and the Gemini API.

The project uses a small student knowledge base to test whether an AI system provides accurate answers or refuses to answer when the required information is unavailable.

## Objectives

- Understand AI hallucinations.
- Learn why AI models generate incorrect or unsupported information.
- Create a small knowledge base.
- Test AI responses using evaluation questions.
- Implement a guardrail to prevent unsupported answers.
- Compare AI responses before and after applying a guardrail.

## Technologies Used

- Python
- Google Gemini API
- Google GenAI SDK
- python-dotenv
- VS Code

## Knowledge Base

The project uses the following fictional student records:

| Student ID | Name | Marks | Attendance | Department |
|---|---|---:|---:|---|
| STU-101 | Ali | 85 | 92% | AI |
| STU-102 | Sara | 90 | 96% | CS |
| STU-103 | Ahmed | 72 | 80% | SE |

## Project Structure

```text
AI Evaluation and Guardrails - Day 15/
│
├── main.py
├── .env
├── .gitignore
└── README.md
```

## How It Works

### 1. Before Guardrail

The Gemini model receives a question and the available student records. It generates an answer based on the provided information.

### 2. After Guardrail

A Python-based guardrail checks the available student information before providing an answer.

If the requested information is unavailable, the system responds:

"I don't have enough information to answer that."

### 3. AI Evaluation

The project evaluates five test questions by comparing expected answers with actual answers.

## Test Cases

| Test | Question | Expected Result |
|---|---|---|
| 1 | What is the name of STU-101? | Ali |
| 2 | What are the marks of STU-102? | 90 |
| 3 | What is the department of STU-103? | SE |
| 4 | What is the name of STU-999? | Refuse to guess |
| 5 | Which university does Ali attend? | Refuse to guess |

## Evaluation Results

- Total test questions: 5
- Correct responses: 5
- Incorrect responses: 0
- Evaluation score: 100%

All five defined test cases passed successfully.

## Installation

Install the required libraries:

```bash
pip install google-genai python-dotenv
```

## API Key Setup

Create a `.env` file in the project folder and add:

```env
GENAI_API_KEY=your_api_key_here
```

Replace `your_api_key_here` with your own Gemini API key.

**Important:** Never upload your actual API key to GitHub.

## Run the Project

```bash
python main.py
```

## Key Learning Outcomes

- Learned how AI hallucinations can occur.
- Understood the importance of grounding AI answers in reliable information.
- Implemented a basic rule-based guardrail.
- Tested supported and unsupported questions.
- Evaluated system responses using expected answers.
- Learned why evaluation is important for building reliable AI applications.

## Future Improvements

- Add tests for partially supported questions.
- Improve handling of multiple requested facts.
- Expand the knowledge base.
- Add more evaluation metrics.
- Improve error handling for temporary API failures.

## Author

AI Student | Big Brains Internship  
Day 15 – AI Evaluation and Guardrails
