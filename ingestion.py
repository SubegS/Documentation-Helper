import asyncio
import os 
import ssl
from typing import Any, Dict, List
import certifi
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings

load_dotenv()


# Configure SSL context to use certifi certificates
ssl_context = ssl.create_default_context(cafile=certifi.where())
os.environ["SSL_CERT_FILE"] = certifi.where()
os.environ["REQUESTS_CA_BUNDLE"] = certifi.where()

embeddings = OpenAIEmbeddings(
    model="text-embedding-3-small",
    show_progress_bar=False,
    chunk_size=50,
    retry_min_seconds=10,
)


async def main():
    """Main async function to orchestrate the entire process."""

if __name__ == "__main__":
    asyncio.run(main())