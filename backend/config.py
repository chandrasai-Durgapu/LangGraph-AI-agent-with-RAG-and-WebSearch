import os
from dotenv import load_dotenv
from pathlib import Path

# This attempts to load the variables
# load_dotenv()

dotenv_path = Path(__file__).parent / '.env'
print("Looking for .env at:", dotenv_path)
load_dotenv(dotenv_path=dotenv_path)

# Try to get the variable and check its value
test_value = os.getenv("API_KEY")

if test_value:
    print("✅ Success! The environment variable was loaded correctly.")
else:
    print(f"❌ Failure! The Environment variable was not loaded. Value found: {test_value}")
# Pinecone
PINECONE_API_KEY=os.getenv("PINECONE_API_KEY")

PINECONE_ENVIRONMENT=os.getenv("PINECONE_ENVIRONMENT") 
PINECONE_INDEX_NAME=os.getenv("PINECONE_INDEX_NAME") 

# Groq
GROQ_API_KEY=os.getenv("GROQ_API_KEY")

# Tavily
TAVILY_API_KEY=os.getenv("TAVILY_API_KEY")

# Embedding Model
EMBED_MODEL=os.getenv("EMBED_MODEL","sentence-transformers/all-MiniLM-L6-v2")

# Paths (adjust as needed)
DOC_SOURCE_DIR=os.getenv("DOC_SOURCE_DIR","data")

