import chromadb
from sentence_transformers import SentenceTransformer

# Step 1: Load the embedding model
print("Loading embedding model...")
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

# Step 2: Create a local, persistent vector database
client = chromadb.PersistentClient(path="./chroma_db")

# Step 3: Create a collection to store university FAQs
collection = client.get_or_create_collection(
    name="university_faqs",
    metadata={"hnsw:space": "cosine"}
)

# Step 4: Prepare 10 sample university FAQs
documents = [
    "Students can apply for admission through the university's online admission portal.",
    "The university offers undergraduate and postgraduate degree programs.",
    "Students can pay their semester fees through the designated bank or online payment methods.",
    "Scholarships are available for eligible students based on merit and financial need.",
    "Students can check their examination results through the university student portal.",
    "The university library provides books, research materials, and study spaces.",
    "Students can access online lectures and recorded lessons through the learning management system.",
    "The computer science department offers courses in programming, artificial intelligence, and data science.",
    "Students can contact the university support office for help with registration and student accounts.",
    "The university provides internship guidance and career support to help students prepare for employment."
]

# Step 5: Add useful metadata to each FAQ
metadatas = [
    {"title": "Admission Process", "category": "Admissions"},
    {"title": "Degree Programs", "category": "Academics"},
    {"title": "Fee Payment", "category": "Finance"},
    {"title": "Scholarships", "category": "Financial Aid"},
    {"title": "Examination Results", "category": "Examinations"},
    {"title": "Library Services", "category": "Student Services"},
    {"title": "Online Learning", "category": "E-Learning"},
    {"title": "Computer Science Courses", "category": "Academics"},
    {"title": "Student Support", "category": "Support"},
    {"title": "Internships and Careers", "category": "Careers"}
]

# Step 6: Generate embeddings for the FAQs
print("Generating embeddings...")
embeddings = model.encode(documents).tolist()

# Step 7: Store the documents, embeddings, and metadata
collection.upsert(
    ids=[f"faq_{i}" for i in range(1, 11)],
    documents=documents,
    embeddings=embeddings,
    metadatas=metadatas
)

print(f"\nSuccessfully stored {collection.count()} FAQs in ChromaDB!")

# Step 8: Create a function for semantic search
def search_faq(question):
    # Convert the user's question into an embedding
    query_embedding = model.encode([question]).tolist()

    # Find the three most similar stored records
    results = collection.query(
        query_embeddings=query_embedding,
        n_results=3,
        include=["documents", "metadatas", "distances"]
    )

    print(f"\nYour question: {question}")
    print("-" * 50)

    # Display the search results
    for i in range(len(results["ids"][0])):
        print(f"\nResult {i + 1}")
        print(f"Title: {results['metadatas'][0][i]['title']}")
        print(f"Category: {results['metadatas'][0][i]['category']}")
        print(f"Information: {results['documents'][0][i]}")
        print(f"Cosine distance: {results['distances'][0][i]:.4f}")

# Step 9: Test three different natural-language questions
test_questions = [
    "How can I get financial assistance for my studies?",
    "Where can I find programming and AI classes?",
    "How do I prepare for a job after university?"
]

for question in test_questions:
    search_faq(question)

# Step 10: Allow the user to ask additional questions
while True:
    user_question = input(
        "\nEnter your own question (or type 'exit' to stop): "
    ).strip()

    if user_question.lower() == "exit":
        print("Thank you for using University FAQ Semantic Search!")
        break

    if not user_question:
        print("Please enter a question.")
        continue

    search_faq(user_question)