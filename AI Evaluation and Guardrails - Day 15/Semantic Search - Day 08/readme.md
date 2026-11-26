# Semantic Search Using Embeddings

## Project Overview
This project demonstrates how semantic search works using text embeddings and cosine similarity. It finds information based on the meaning of a user's question rather than relying only on exact keyword matches.

This project was created as part of the Big Brains Generative AI Internship.

## Objectives
- Understand text embeddings and vector representations.
- Generate embeddings for a collection of text documents.
- Calculate cosine similarity between a query and documents.
- Rank documents based on similarity scores.
- Test semantic search with predefined and custom questions.

## Technologies Used
- Python
- Sentence Transformers
- NumPy
- Pre-trained model: `sentence-transformers/all-MiniLM-L6-v2`

## How It Works
1. Load a pre-trained sentence embedding model.
2. Store 10 sample documents about an online learning platform.
3. Convert the documents into numerical vectors called embeddings.
4. Convert each user query into an embedding.
5. Calculate cosine similarity between the query and document embeddings.
6. Display the top three most similar documents.

## Installation

Make sure Python is installed on your computer.

Install the required libraries by running:

```bash
python -m pip install sentence-transformers numpy
```

## How to Run

1. Open the project folder in VS Code.
2. Open the terminal.
3. Run the following command:

```bash
python semantic_search.py
```

4. Wait for the model to load.
5. Review the search results for the test questions.
6. Enter your own question when prompted.
7. Type `exit` to stop the program.

The first run may take some time because the pre-trained model needs to download.

## Sample Questions
- How can I start learning to code?
- Can I watch my lessons whenever I want?
- How do I get proof that I finished a course?
- Where can I get help if I cannot access my account?

## Key Learning Outcomes
- Learned how text is represented using embeddings.
- Practiced generating embeddings with Sentence Transformers.
- Used cosine similarity to compare vectors.
- Implemented a basic semantic search system in Python.

## Limitations
- The search uses a small collection of 10 sample documents.
- Results depend on the embedding model and the available documents.
- The system retrieves similar text but does not generate answers like a conversational AI model.

## Author
Created as part of the Big Brains Generative AI Internship.