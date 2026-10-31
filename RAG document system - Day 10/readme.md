# Day 10 – RAG Document Q&A System

## Project Overview

This project is a simple Retrieval-Augmented Generation (RAG) application that answers user questions based on information stored in a university knowledge base.

It combines ChromaDB for document storage and retrieval with Google's Gemini API to generate clear and relevant answers.

Instead of answering from general knowledge, the system retrieves relevant information from stored documents and uses that information as context for generating responses.

## Technologies Used

- Python
- Google Gemini API
- ChromaDB
- Python-dotenv

## How It Works

1. **Document Storage:** University information is stored as text documents in a ChromaDB collection.
2. **Embedding Generation:** ChromaDB automatically generates embeddings for the stored documents using its default embedding function.
3. **Similarity Search:** When a user asks a question, ChromaDB retrieves the three most relevant document chunks.
4. **Context Creation:** The retrieved documents are combined into a context.
5. **Answer Generation:** The context and user's question are sent to the Gemini API.
6. **Response:** Gemini generates an answer based only on the retrieved university information.

## Features

- Stores university information in ChromaDB.
- Retrieves relevant documents using semantic search.
- Uses Gemini API to generate answers.
- Provides answers based on the stored knowledge base.
- Handles questions with no available information.
- Supports multiple questions through an interactive terminal interface.

## Project Structure

```text
RAG document system - Day 10/
│
├── main.py
├── README.md
├── requirements.txt
├── .env
└── chroma_db/
```

**Note:** The `.env` file and `chroma_db/` folder should not be uploaded to GitHub.

## Installation and Setup

### 1. Clone the Repository

```bash
github repo : https://github.com/maheen72/Big-Brains-Internship-/tree/main/RAG%20document%20system%20-%20Day%2010
```

### 2. Install Dependencies

```bash
pip install chromadb python-dotenv google-genai
```

### 3. Configure the API Key

Create a `.env` file in the project folder:

Replace the placeholders with your actual API key and supported model name.

### 4. Run the Application

```bash
python main.py
```

## Example Questions

- What is the minimum attendance requirement?
- How much is the undergraduate tuition fee?
- What are the university library opening hours?
- What GPA is required for a merit scholarship?
- Are electronic devices allowed during examinations?

## Learning Outcomes

Through this project, I learned:

- The basic concept of Retrieval-Augmented Generation (RAG).
- How to store and retrieve documents using ChromaDB.
- How semantic search helps find relevant information.
- How to connect a Python application with the Gemini API.
- How retrieved context can help an LLM generate more relevant answers.

## Internship

**Big Brains Generative AI Internship – Day 10**

*Learning and implementing a basic RAG-based document question-answering system.*