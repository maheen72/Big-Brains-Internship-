
import os
import mimetypes
from pathlib import Path

from dotenv import load_dotenv
from google import genai
from google.genai import types


# Load environment variables
load_dotenv()

# Get Gemini API key
API_KEY = os.getenv("GENAI_API_KEY")

# Check API key
if not API_KEY:
    raise ValueError("Gemini API key not found. Check your .env file.")

# Create Gemini client
client = genai.Client(api_key=API_KEY)

# Select Gemini model
MODEL_NAME = "gemini-3.5-flash"


def analyze_image(image_path, question):

    # Convert the image path into a Path object
    image_file = Path(image_path)

    if not image_file.is_absolute():
       image_file = Path(__file__).resolve().parent / image_file

    # Check whether the image exists
    if not image_file.is_file():
        print("Error: Image file not found.")
        return

    # Check the image file type
    mime_type, _ = mimetypes.guess_type(str(image_file))

    if mime_type not in ["image/jpeg", "image/png", "image/webp"]:
        print("Error: Please use a JPG, PNG, or WEBP image.")
        return

    # Read image as binary data
    with open(image_file, "rb") as file:
        image_bytes = file.read()

    # Create image input for Gemini
    image_part = types.Part.from_bytes(
        data=image_bytes,
        mime_type=mime_type
    )

    # Prepare instructions for the AI
    prompt = f"""
    Analyze the provided image and answer this question:

    {question}

    Only use information visible in the image.
    If the answer cannot be determined from the image,
    clearly say that the information is not visible.
    Do not invent information.
    Give a clear and simple answer.
    """

    try:
        # Send image and text to Gemini
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=[prompt, image_part]
        )

        # Display AI response
        print("\n========== AI RESPONSE ==========")
        print(response.text)
        print("=================================")

    except Exception as error:
        print("Something went wrong:", error)


# Main program
print("\n====================================")
print("  MULTIMODAL AI IMAGE ASSISTANT")
print("====================================")

# Get image path from user
image_path = input("\nEnter image path: ")

# Get question from user
question = input("Ask a question about the image: ")

# Analyze image
analyze_image(image_path, question)
