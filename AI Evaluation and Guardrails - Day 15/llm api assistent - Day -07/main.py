import os
from dotenv import load_dotenv
from google import genai

# Load private settings from the .env file
load_dotenv()

# Check if the Gemini API key is available
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("Error: Gemini API key is not found.")
    print("Please set GEMINI_API_KEY in the .env file.")
    raise SystemExit(1)

# Connect to Gemini
client = genai.Client(api_key=api_key)

# Display the title
print("=" * 50)
print("      LLM API Assistant")
print("=" * 50)
print("Ask a question or type 'exit' to stop the program.")

# Keep asking questions
while True:
    question = input("\nEnter your question: ").strip()

    if question.lower() == "exit":
        print("Exiting the program. Goodbye!")
        break

    if not question:
        print("Please enter a valid question.")
        continue

    try:
        # Send the question to Gemini
        response = client.models.generate_content(
            model="gemini-3.8-flash",
            contents=question
        )

        # Display the AI-generated response
        print("\nAI response:")
        print(response.text)

    except Exception as error:
        print(f"Something went wrong: {error}")
        