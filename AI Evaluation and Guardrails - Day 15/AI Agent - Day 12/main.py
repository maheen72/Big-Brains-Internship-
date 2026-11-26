import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

# Step 1 - load api key from .env file
load_dotenv()
API_KEY = os.getenv("GENAI_API_KEY")

# Checking if API key exists
try:
    
 if not API_KEY:
    raise ValueError("API key not found. Please set GENAI_API_KEY in your .env file.")

except ValueError as e:
    print(e)
    exit(1)
    
# Step 2 - Connect to Gemini
client = genai.Client(api_key=API_KEY)
MODEL = "gemini-3.5-flash"

# Step 3 - Create a Fictional product database
Products = {
    "laptop":{
        "name" : "laptop",
        "price" : 1000,
        "stock" : 10,
    },
    "wireless mouse":{
        "name" : "wireless mouse",
        "price" : 50,
        "stock" : 100,
    },
    "headphones":{
        "name" : "headphones",
        "price" : 150,
        "stock" : 50,
    }
}

# Step 4 - Get product information function
def get_product_info(product_name:str) -> dict:
    """ Find the product name and price in its stored database.
    Args:
        product_name = Name of the product """
    print( f"\n[TOOL EXECUTED] Searching for {product_name}...")
    
    product = Products.get(product_name.lower().strip())
    
    if product is None:
        return{
            "found" : False,
            "message" : f"No product found in the database with name {product_name}."
        }
        
    return{
            "found" : True,
            "product_name" : product["name"],
            "price" : product["price"],
            "currency" : "PKR"
        }
# Step 5 - Check product Stock
def check_stock(product_name:str) -> dict:
    """ Check the stock of the product in its stored database.
    Args:
        product_name = Name of the product """
    print( f"\n[TOOL EXECUTED] Checking stock for {product_name}...")
    
    product = Products.get(product_name.lower().strip())
    
    if product is None:
        return{
            "found" : False,
            "message" : f"No product found in the database with name {product_name}."
        }
        
    return{
            "found" : True,
            "product_name" : product["name"],
            "available" : product["stock"] > 0,
            "stock_quantity" : product["stock"]
    }
    
# Step 6 - Calculate total price
def calculate_total(price: float, quantity: int) -> dict:
    """ Calculate the total price of the product in its stored database.
    Args:
        price = Price of the product
        quantity = Quantity of the product """
    print( f"\n[TOOL EXECUTED] Calculating total price for {price}...")
    
    if price < 0 or quantity <= 0:
        return{
            "found" : False,
            "message" : f"Price and quantity must be non-negative."
        }
    
    total_price = price * quantity
    return{
            "found" : True,
            "price" : price,
            "quantity" : quantity,
            "total_price" : total_price,
            "currency" : "PKR"
        }
    
# Step 7 - Give instructions to AI Agent
agent_instructions = """
You are a helpful assistant that can provide information about products in a store.

your job is to answer questions about products, their prices, and stock availability using available tools

Available tools:
- `get_product_info`: Retrieve information about a specific product.
- `check_stock`: Check the stock availability of a specific product.
- `calculate_total`: Calculate the total price of a product based on its price and quantity.

Rules:
- Use tools whenever the user asks for product information or stock availability.
- Only use the `calculate_total` tool when the user asks for the total price of a product based on its price and quantity.
- Always provide clear and concise answers to the user.
- Never invent product information. If a product is not found, clearly explain that the product does not exist in the database.
- Keep your answers clear, friendly, and easy to understand.
- Give clear and friendly instructions to the user on how to use the tools when necessary.
"""

# Step 8 - Create Ai Agent

def run_agent(user_request: str):
    print("\n===================================")
    print("     PRODUCT INFORMATION AI")
    print("===================================")

    chat = client.chats.create(
        model=MODEL,
        config=types.GenerateContentConfig(
            system_instruction=agent_instructions,
            tools=[
                get_product_info,
                check_stock,
                calculate_total
            ],
            automatic_function_calling=types.AutomaticFunctionCallingConfig(
                maximum_remote_calls=10
            )
        )
    )

    response = chat.send_message(user_request)

    print("\nAI Agent Response:")
    print(response.text)

# Step 9 - Start the agent
print("Welcome to the Product Information AI Agent!")
print("You can ask me about products, their prices, and stock availability.")
print("Type exit to exit the assistant")

while True:
    
    user_input = input("\nYou: ").strip()
    if  user_input.lower() == "exit":
            print("Exiting the assistant. Goodbye!")
            break
    if not user_input:
            print("Please enter a valid question or type 'exit' to quit.")
            continue
    try:
        run_agent(user_input)
    except Exception as e:
        print(f"An error occurred: {e}")
        print("Please try again or type 'exit' to quit.")