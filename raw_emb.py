import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

# Initialize OpenAI client (no need to pass API key explicitly)
client = OpenAI()

# Generate embeddings
response = client.embeddings.create(
    input="Your text string goes here",
    model="text-embedding-3-small"
)

# Print the first embedding result
print(response.data[0].embedding)
