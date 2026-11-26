from sentence_transformers import SentenceTransformer
import numpy as np

print("Loading model...")
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

document = [
      "Our platform offers beginner-friendly Python programming courses.",
    "Students can learn machine learning and artificial intelligence online.",
    "The platform provides certificates after completing eligible courses.",
    "Students can access recorded video lessons at any time.",
    "Our customer support team helps students with account problems.",
    "Course fees can be paid using supported online payment methods.",
    "Students can practice coding through hands-on programming projects.",
    "The platform offers courses about data science and data analysis.",
    "Students can study web development, including HTML, CSS, and JavaScript.",
    "New students can create an account using their email address."
]

document_embeddings = model.encode(document)

print("Number of embeddings:", len(document))
print("Shape of embeddings", document_embeddings.shape)

def semantic_search(query, top_k = 3):
    
    query_embeddings = model.encode([query])[0]
    document_norm = np.linalg.norm(document_embeddings, axis=1)
    query_norm = np.linalg.norm(query_embeddings)
    scores = np.dot(document_embeddings , query_embeddings) / (document_norm * query_norm)
    
    ranked_indices = np.argsort(scores)[::-1]
    
    print("\nQuestion:", query)
    print("-" * 60)
    
    for rank,index in enumerate(ranked_indices[:top_k], start=1):
        print(f"{rank}. Similarity score: {scores[index]:.4f}")
        print("   Information:", document[index])
        
test_questions = [
    "How can I start learning to code?",
    "Can I watch my lessons whenever I want?",
    "How do I get proof that I finished a course?",
    "Where can I get help if I cannot access my account?"
]
        
print("\nRunning semantic search for test questions...")

for question in test_questions:
    semantic_search(question)

while True:
    user_question = input("\nEnter your question (or type 'exit' to quit): ").strip()
    
    if user_question.lower() == "exit":
        print("Exiting the program. Goodbye!")
        break
    if user_question:
        semantic_search(user_question)