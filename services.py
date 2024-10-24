import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

REPLICATE_API_URL = "https://api.replicate.com/v1/predictions"
REPLICATE_API_TOKEN = os.getenv("REPLICATE_API_TOKEN")

headers = {
    "Authorization": f"Token {REPLICATE_API_TOKEN}",
    "Content-Type": "application/json",
}

def generate_image(prompt: str, model: str, version: str, num_outputs: int, width: int, height: int):
    """
    This function interacts with Replicate's API to generate an image based on the given prompt.
    """
    data = {
        "version": version,
        "input": {
            "prompt": prompt,
            "num_outputs": num_outputs,
            "width": width,
            "height": height,
        }
    }

    response = requests.post(f"{REPLICATE_API_URL}", headers=headers, json=data)
    
    if response.status_code != 200:
        raise Exception(f"Error: {response.status_code}, {response.text}")
    
    return response.json()
