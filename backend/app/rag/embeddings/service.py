from app.rag.chunking.models import RetrievedChunk

from app.rag.embeddings.client import embedding_client

from app.rag.embeddings.models import EmbeddedChunk


class EmbeddingService:

    def embed_chunk(
        self,
        chunk: RetrievedChunk,
    ):

        embedding = embedding_client.embed(
            chunk.text
        )

        return EmbeddedChunk(

            chunk_id=chunk.chunk_id,

            url=chunk.url,

            title=chunk.title,

            text=chunk.text,

            embedding=embedding,

            chunk_index=chunk.chunk_index,

            total_chunks=chunk.total_chunks,

        )

    def embed_chunks(
        self,
        chunks: list[RetrievedChunk],
    ):

        return [

            self.embed_chunk(chunk)

            for chunk in chunks

        ]


embedding_service = EmbeddingService()