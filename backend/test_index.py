import asyncio

from app.retriever.service import retriever_service

from app.rag.chunking.service import chunking_service

from app.rag.embeddings.service import embedding_service

from app.rag.indexing.service import indexing_service


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

    indexing_service.index(
        embedded
    )

    results = indexing_service.search(
        "Python programming language"
    )

    print()

    print(results)


asyncio.run(main())