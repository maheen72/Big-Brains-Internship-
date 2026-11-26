
# Multimodal AI Image Understanding Assistant

## Big Brains Generative AI Internship – Day 14

## Project Overview

The Multimodal AI Image Understanding Assistant is a Python-based application that uses the Google Gemini API to understand images and answer questions about them.

The application accepts an image path and a text-based question from the user. It sends both inputs to the Gemini model and generates a response based on the visual information in the image.

This project demonstrates how Multimodal Generative AI can combine image and text inputs to understand and explain visual information.

## Objectives

- Understand the concept of Multimodal Generative AI.
- Integrate the Google Gemini API with Python.
- Process images and text together.
- Explore image understanding using different prompts.
- Learn practical applications of multimodal AI.

## Technologies Used

- Python
- Google Gemini API
- Google Gen AI SDK
- python-dotenv
- Pathlib
- Mimetypes
- Visual Studio Code

## Project Structure

```text
Multimodel Project - Day 14/
│
├── main.py
├── .env
├── .gitignore
├── requirements.txt
├── README.md
│
└── images/
    ├── Headphone.jpg
    ├── Plant-Cell.png
    └── recip.jpg
```

## Installation and Setup

### 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Open the Project Folder

```bash
cd YOUR_PROJECT_FOLDER
```

### 3. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Configure the Gemini API Key

Create a `.env` file in the project directory and add your Gemini API key:

```env
GEMINI_API_KEY=your_api_key_here
```

Replace `your_api_key_here` with your own API key.

**Important:** Never share or upload your actual API key to GitHub.

### 5. Run the Application

```bash
python main.py
```

Enter the image path when prompted, followed by your question about the image.

## Practical Experiments

### Experiment 1: Product Image Understanding

**Image:** Headphone.jpg

The application analyzes a headphone image and describes its visible features, color, design, and components.

### Experiment 2: Document Understanding

**Image:** recip.jpg

The application analyzes a shopping receipt and extracts visible information such as item names, quantities, prices, and total amount.

### Experiment 3: Educational Diagram Understanding

**Image:** Plant-Cell.png

The application analyzes a plant cell diagram, identifies visible components, and explains their functions.

## Key Learning Outcomes

- Understanding Multimodal Generative AI.
- Working with the Google Gemini API.
- Processing image files using Python.
- Combining image and text inputs.
- Writing effective prompts.
- Handling API keys using environment variables.
- Debugging file paths and API errors.

## Real-World Applications

- Educational diagram analysis.
- Product image descriptions.
- Receipt and document information extraction.
- Image accessibility.
- Visual information processing.

## Internship Information

**Program:** Big Brains Generative AI Internship

**Task:** Day 14 – Explore Multimodal Generative AI

**Project:** Multimodal AI Image Understanding Assistant

**Developed By:** Maheen Nasir
