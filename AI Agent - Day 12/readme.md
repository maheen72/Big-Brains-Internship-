
# Product Information AI Agent

## Overview

This project is a simple AI Agent built using Python and Google Gemini API as part of the Big Brains Generative AI Internship (Day 13).

The AI Agent can understand user requests, select appropriate tools, execute tasks, and provide responses based on the results.

Unlike a basic chatbot, this agent uses function calling to interact with a fictional product database and perform multiple operations.

## Features

- Retrieve product information and prices.
- Check product stock availability.
- Calculate the total price based on product price and quantity.
- Automatically select appropriate tools based on user requests.
- Handle unavailable products without inventing information.
- Support multi-step tasks using multiple tools.

## Technologies Used

- Python
- Google Gemini API
- Google Gen AI SDK
- Function Calling
- Python Dictionaries
- python-dotenv

## Available Tools

The agent uses three Python functions:

### 1. get_product_info()
Retrieves product information and prices from the product database.

### 2. check_stock()
Checks whether a product is available and returns its stock quantity.

### 3. calculate_total()
Calculates the total price using the product price and requested quantity.

## Project Structure

AI-Agent-Day-13/
│
├── main.py
├── README.md
└── .gitignore

## Installation and Setup

### 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Navigate to the Project Folder

```bash
cd AI-Agent-Day-13
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the API Key

Create a `.env` file in the project folder and add:

```env
GENAI_API_KEY=your_gemini_api_key
```

Replace `your_gemini_api_key` with your actual Gemini API key.

### 5. Run the Project

```bash
python main.py
```

## Example Test Cases

### Test 1: Product Information

**User:** What is the price of the wireless mouse?

**Expected Result:** The agent retrieves the wireless mouse price from the database.

### Test 2: Stock Availability

**User:** Is the laptop available in stock?

**Expected Result:** The agent checks the stock and reports the available quantity.

### Test 3: Multiple Tool Execution

**User:** What is the total price of 2 laptops, and are they available?

**Expected Result:** The agent retrieves the laptop price, checks stock availability, and calculates the total price.

### Test 4: Unavailable Product

**User:** Do you have an iPhone 20?

**Expected Result:** The agent explains that the product is not available in the database.

## Learning Outcomes

Through this project, I learned:

- What AI Agents are and how they work.
- The difference between AI chatbots and AI Agents.
- How LLMs make decisions and select tools.
- How to implement function calling in Python.
- How an AI Agent performs multi-step tasks.
- How to connect Python applications with the Google Gemini API.

## Internship

**Program:** Big Brains Generative AI Internship  
**Task:** Day 13 – Understand AI Agents and Build Your First AI Agent

---

**Author:** Maheen Nasir
