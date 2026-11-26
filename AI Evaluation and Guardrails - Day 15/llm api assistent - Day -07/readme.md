# LLM API Assistant

## Overview
This project is a command-line AI assistant built with Python and the Google Gemini API.

## Features
- Accepts questions from the user.
- Sends questions to an AI model through an API.
- Displays AI-generated responses.
- Supports multiple questions until the user types `exit`.
- Handles errors and missing API keys.

## Technologies Used
- Python
- Google Gemini API
- Google Gen AI SDK
- python-dotenv

## How to Run
1. Install the dependencies:
   `python -m pip install google-genai python-dotenv`
2. Add your Gemini API key to a local `.env` file.
3. Run `python llm-api-assistant.py`.

Keep your API key private. Never upload the `.env` file.
