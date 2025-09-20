# 

import os
import time
from pinecone import Pinecone as PineconeClient, ServerlessSpec  # official Pinecone client
#lang chain integrations
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_pinecone import PineconeVectorStore  # LangChain's Pinecone integration
from .config import PINECONE_API_KEY

# Initialize Pinecone client (no .init())
pc = PineconeClient(api_key=PINECONE_API_KEY)

# Define embedding model
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Set your index name
INDEX_NAME = "rag-index"


def get_retriever():
    """
    Initializes and returns a Pinecone-based LangChain retriever.
    Checks for existing index or creates one using ServerlessSpec.
    """
    try:
        # Check if index exists
        if INDEX_NAME not in pc.list_indexes().names():
            print(f"Index '{INDEX_NAME}' not found. Creating a new index...")

            pc.create_index(
                name=INDEX_NAME,
                dimension=384,
                metric="cosine",
                spec=ServerlessSpec(cloud="aws", region="us-east-1")
            )

            # Wait for the index to be ready
            while not pc.describe_index(INDEX_NAME).status['ready']:
                print("Waiting for index to be ready...")
                time.sleep(1)

            print(f"New index '{INDEX_NAME}' is ready.")
        else:
            print(f"Index '{INDEX_NAME}' already exists.")

        # Initialize vectorstore
        vectorstore = PineconeVectorStore(
            index_name=INDEX_NAME,
            embedding=embeddings,
            # client=pc
        )

        return vectorstore.as_retriever()

    except Exception as e:
        print(f"An error occurred in get_retriever(): {e}")
        return None


def add_documents(text_content: str):
    """
    Splits text content and adds chunks to Pinecone vectorstore.
    """
    if not text_content:
        print("Document cannot be empty.")
        raise ValueError("Document cannot be empty")

    try:
        start_time = time.perf_counter()

        # Split the text
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=500,
            chunk_overlap=50
        )
        documents = text_splitter.create_documents([text_content])

        end_time = time.perf_counter()
        print(f"Time taken for splitting: {end_time - start_time:.4f} seconds")
        print("Document split into chunks. Proceeding to index...")

    except Exception as e:
        print(f"Error while splitting document: {e}")
        return

    try:
        # Initialize vectorstore again
        vectorstore = PineconeVectorStore(
            index_name=INDEX_NAME,
            embedding=embeddings
        )

        vectorstore.add_documents(documents)
        print("✅ Successfully added document chunks to Pinecone.")

    except Exception as e:
        print(f"Error while adding documents to Pinecone: {e}")
