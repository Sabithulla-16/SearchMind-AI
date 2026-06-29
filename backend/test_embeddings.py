import asyncio

from app.retriever.service import retriever_service

from app.rag.chunking.service import chunking_service

from app.rag.embeddings.service import embedding_service


async def main():

    document = await retriever_service.retrieve(
        "https://www.python.org/"
    )

    chunks = chunking_service.chunk_document(
        document
    )

    embedded = embedding_service.embed_chunks(
        chunks
    )

    print(f"Chunks: {len(embedded)}")

    print()

    print(f"Embedding Length: {len(embedded[0].embedding)}")

    print()

    print(embedded[0].embedding[:10])


asyncio.run(main())