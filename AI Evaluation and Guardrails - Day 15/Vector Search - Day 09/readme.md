
# University FAQ Semantic Search  


## 1. Project Overview

This project demonstrates how vector databases can store text embeddings and retrieve relevant information using semantic similarity.

I developed a University FAQ Semantic Search system using Python, ChromaDB, and Sentence Transformers. The system stores 10 fictional university FAQs in a persistent local vector database and allows users to search for relevant information using natural-language questions.

## 2. Objective

The objectives of this project are to:

- Understand the concept of vector databases.
- Learn how text is converted into numerical embeddings.
- Store embeddings, documents, and metadata in ChromaDB.
- Perform similarity searches using natural-language questions.
- Understand how vector databases support semantic search applications.

## 3. Technologies Used

- **Python:** Used to develop the application and implement the search functionality.
- **ChromaDB:** Used to store and retrieve document embeddings, text, and metadata.
- **Sentence Transformers:** Used to generate numerical embeddings from text.
- **all-MiniLM-L6-v2:** A pretrained sentence-embedding model used to represent the meaning of documents and search queries.

## 4. Sample Data

The project contains 10 fictional university FAQs covering the following topics:

1. Admission procedures
2. Degree programs
3. Semester fee payments
4. Scholarships and financial aid
5. Examination results
6. Library services
7. Online learning
8. Computer science, artificial intelligence, and data science courses
9. Student support
10. Internships and career guidance

Each FAQ has a unique ID, document text, numerical embedding, and metadata containing a title and category.

## 5. How the Project Works

The system follows these steps:

1. Load the pretrained Sentence Transformers embedding model.
2. Create a persistent ChromaDB client.
3. Create or retrieve a collection named `university_faqs`.
4. Prepare 10 university FAQs and their metadata.
5. Generate embeddings for all FAQ documents.
6. Store the document IDs, text, embeddings, and metadata using ChromaDB's `upsert()` method.
7. Convert each search question into an embedding.
8. Retrieve the three most similar records using ChromaDB's similarity search.
9. Display the title, category, document text, and cosine distance for each result.
10. Allow users to enter additional questions interactively.

The collection uses cosine distance to compare vectors. A smaller distance generally indicates greater similarity between the query and a stored document.

## 6. Traditional Database vs. Vector Database

A traditional database is commonly used to retrieve structured information, such as student IDs, prices, and dates.

A vector database stores and searches numerical vector representations based on similarity.

For example, a user might ask, "How can I get financial assistance for my studies?" The system may retrieve a scholarship FAQ even though the stored document uses different wording.

This demonstrates how semantic search can retrieve related information based on meaning rather than relying only on exact keyword matches.

## 7. Search Queries and Results

The program automatically tests three natural-language questions.

### Query 1: Financial Assistance

**Question:** How can I get financial assistance for my studies?

**Relevant topic:** Scholarships and financial aid.

**Returned results:** The program displays the three closest matching records, including their titles, categories, document text, and cosine distances.

### Query 2: Programming and AI Courses

**Question:** Where can I find programming and AI classes?

**Relevant topic:** Computer science courses and academic programs.

**Returned results:** The program displays the three closest matching records returned by ChromaDB.

### Query 3: Career Preparation

**Question:** How do I prepare for a job after university?

**Relevant topic:** Internships and career guidance.

**Returned results:** The program displays the three closest matching records returned by ChromaDB.

The actual ranking and cosine distances depend on the generated embeddings and search results. The program also allows users to enter additional questions and view their results.

## 8. Results and Learning Outcomes

Through this project, I learned:

- What a vector database is and why it is useful.
- How text embeddings represent semantic meaning numerically.
- How to generate embeddings using Sentence Transformers.
- How to store documents, embeddings, and metadata in ChromaDB.
- How to perform similarity searches using natural-language queries.
- How persistent storage allows a local vector database to be reused.
- Why similarity search results should be evaluated for relevance and correctness.

## 9. Real-World Applications

Vector databases are commonly used in:

- Semantic search systems
- AI-powered knowledge bases
- Recommendation systems
- Document retrieval
- Retrieval-Augmented Generation (RAG) applications

For example, a university could store academic documents and FAQs in a vector database. Students could then ask questions in natural language and retrieve relevant information without needing to use the exact wording of the stored documents.

## 10. Conclusion

This project provided practical experience with embeddings, vector databases, metadata, and similarity search.

Using Python, ChromaDB, and Sentence Transformers, I developed a small semantic search system that stores university FAQs and retrieves relevant records based on the meaning of a user's question.

This project helped me understand the basic workflow of vector search and how vector databases can be used as a building block for Generative AI and RAG applications.

## 11. Project Structure

```text
Day 09/
├── vector_search.py
├── README.md
└── chroma_db/
```

- `vector_search.py`: Contains the Python implementation.
- `README.md`: Documents the project, technologies, workflow, and results.
- `chroma_db/`: Stores the local ChromaDB database files and is created automatically when the program runs.

## 12. How to Run the Project

### Step 1: Install the required libraries

```bash
python -m pip install chromadb sentence-transformers
```

### Step 2: Run the Python program

```bash
python vector_search.py
```

### Step 3: Wait for the model to load

The program loads the embedding model, generates embeddings, and stores the 10 FAQs in ChromaDB. The first run may download the model files.

### Step 4: Test the search functionality

The program automatically searches three sample questions and displays the returned results.

### Step 5: Enter your own questions

Type a natural-language question when prompted. Enter `exit` to stop the program.
