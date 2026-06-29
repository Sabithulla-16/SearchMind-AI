import asyncio

from app.retriever.service import retriever_service
from app.rag.chunking.service import chunking_service


async def main():
    print("Retrieving document...\n")

    document = await retriever_service.retrieve(
        "https://www.python.org/"
    )

    if document is None:
        print("Failed to retrieve document.")
        return

    print(f"Title: {document.title}")
    print(f"URL: {document.url}")
    print(f"Content Length: {len(document.content)} characters")

    chunks = chunking_service.chunk_document(document)

    print(f"\nTotal Chunks: {len(chunks)}")
    print("=" * 80)

    for chunk in chunks:
        print(f"\nChunk {chunk.chunk_index}/{chunk.total_chunks}")
        print(f"Chunk ID    : {chunk.chunk_id}")
        print(f"Token Count : {chunk.token_count}")
        print(f"Text Length : {len(chunk.text)} characters")

        preview = chunk.text[:300].replace("\n", " ")
        print(f"Preview     : {preview}...")

        print("-" * 80)


if __name__ == "__main__":
    asyncio.run(main())