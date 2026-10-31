import os
import chromadb
from dotenv import load_dotenv
from google import genai

# Loading environmental variables from .env files
load_dotenv(
    dotenv_path=os.path.join(os.path.dirname(__file__), ".env")
)


# Loading API key and Model name  from .env file
GENAI_API_KEY = os.getenv("GENAI_API_KEY")
GEMINI_MODEL_NAME = os.getenv("GEMINI_MODEL_NAME", "gemini-3.5-flash")

print("Key length:", len(GENAI_API_KEY))
print("Starts with:", GENAI_API_KEY[:4])
print("Has spaces/quotes:", GENAI_API_KEY != GENAI_API_KEY.strip().strip('"').strip("'"))

# Checking if the API key available or not in .env file
if not GENAI_API_KEY:
  raise ValueError(
        "GENAI key is not found. Kindly set GEN AI key first in .env file"
        )
# Initializing the Gemini client with the API key and model name
gemini_client = genai.Client(api_key = GENAI_API_KEY)

# Initializing the ChromaDB client
chroma_client = chromadb.PersistentClient(path="./chroma_db")

# creating a collection in Chromadb to store the documents
try:
    collection = chroma_client.delete_collection(
        name = "university_knowledge"
        )
except Exception:
    pass

# creating a new collection
collection = chroma_client.create_collection(
    name = "university_knowledge"
    )

# creating documnents to store in the collection
documents = [
    (
        "Attendance Policy: Students at Bright Future University "
        "must maintain at least 75 percent attendance in each "
        "course to be eligible for final examinations."
    ),
    (
        "Tuition Fees: The undergraduate tuition fee is "
        "50000 Pakistani rupees per semester. Students must pay "
        "their semester fees before the published deadline."
    ),
    (
        "Library Hours: The university library is open from "
        "8 AM to 6 PM, Monday through Friday. It is closed on Sundays."
    ),
    (
        "Scholarships: Students with a semester GPA of 3.5 or higher "
        "may apply for a merit scholarship. Selection is subject to "
        "the university's scholarship review process."
    ),
    (
        "Computer Science Courses: The university offers introductory "
        "courses in Python programming, databases and artificial "
        "intelligence for eligible undergraduate students."
    ),
    (
        "Examination Rules: Students must bring their university "
        "identity card to examinations. Electronic devices are not "
        "permitted unless explicitly authorized."
    ),
    (
        "Student Support: The student support office helps students "
        "with enrollment questions, fee guidance and general "
        "academic information. Students can visit the office "
        "during regular university working hours."
    ),
]

# storing the documents in the database(chromadb) collection
collection.add(
    ids = [f"chunk{i}" for i in range(len(documents))],
    documents = documents
)

# prints the sucess message and give the numver of chunks stored in the collection
print("Documents stored sucessfully in the colection")
print(f"Number of chunks stored: {collection.count()}")

# Creating a function that answers questions based on documents
def answer_question(user_question):
    """Retrieve relevant information and generate an answer."""

    # Retrieving relevant information
    result = collection.query(
        query_texts=[user_question],
        n_results=3
    )

    # Extracting the retrieved documents
    retrieved_chunks = result["documents"][0]
    
    if not retrieved_chunks:
        print("No relevant information found in the university knowledge base.")
        return

    # Combining the retrieved chunks
    context = "\n\n".join(retrieved_chunks)
    
    
    # Creating a prompt for the Gemini model
    prompt = f"""
You are a university information assistant.

Answer the user's question using ONLY the context below.

Rules:
    - Do not invent facts or use outside knowledge.
    - If the context does not contain enough information,
      clearly say that the information is not available
      in the provided university knowledge base.
    - Keep your answer clear and concise.

Retrieved context:
    {context}

User question:
       
    {user_question}

Answer:
    """

    # Generating an answer using the Gemini model
    response = gemini_client.models.generate_content(
        model = GEMINI_MODEL_NAME,
        contents = prompt,
    )
    
    # Returning the generated answer
    print("\n" + "=" * 55)
    print("QUESTION:", user_question)
    print("\nRETRIEVED CONTEXT:")
    print(context)
    print("\nGENERATED ANSWER:")
    print(response.text or "No answer was returned.")
    print("=" * 55)
    
if __name__ == "__main__":
    print("Welcome to the University Knowledge Assistant!")
    print("Type 'exit' to close the application.\n")

    while True:
        user_question = input("Please enter your question:").strip()
        if user_question == "exit":
            print("Exiting the University Knowledge Assistant. Goodbye!")
            break
        if not user_question:
            print("Please enter a valid question.")
            continue
            
        try:
          answer_question(user_question)
        except Exception as error:
          print("Error:", error)