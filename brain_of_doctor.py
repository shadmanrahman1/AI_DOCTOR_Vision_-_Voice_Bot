# step 1:  api key for Groq
import os
import base64
from dotenv import load_dotenv
from groq import Groq

# Load environment variables from .env file
load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")
if not groq_api_key:
    raise ValueError("GROQ_API_KEY environment variable is not set.")

# Step 2: convert image to required format


# image_path = "acne.jpg"
def encode_image(image_path):
    image_file = open(image_path, "rb")
    encoded_image = base64.b64encode(image_file.read()).decode("utf-8")
    image_file.close()
    return encoded_image


# Step 3: Setup MultiModal LLM

query = "is there something wrong with this skin?"
model = "meta-llama/llama-4-scout-17b-16e-instruct"


def analyze_image_with_query(query, model, encoded_image):
    client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
    completion = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": query},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{encoded_image}",
                        },
                    },
                ],
            }
        ],
        temperature=1,
        max_completion_tokens=1024,
        top_p=1,
        stream=False,
        stop=None,
    )
    return completion.choices[0].message.content
