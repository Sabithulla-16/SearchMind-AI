import uuid

from app.rag.chunking.models import RetrievedChunk

from app.rag.chunking.splitter import splitter

from app.rag.chunking.tokenizer import tokenizer

from app.retriever.models import RetrievedDocument


class ChunkingService:

    def chunk_document(
        self,
        document: RetrievedDocument,
    ):

        texts = splitter.split(
            document.content
        )

        total = len(texts)

        chunks = []

        for index, text in enumerate(texts):

            chunks.append(

                RetrievedChunk(

                    chunk_id=str(uuid.uuid4()),

                    url=document.url,

                    title=document.title,

                    text=text,

                    chunk_index=index + 1,

                    total_chunks=total,

                    token_count=tokenizer.count_tokens(
                        text
                    ),

                )

            )

        return chunks

    def chunk_documents(
        self,
        documents: list[RetrievedDocument],
    ):

        all_chunks = []

        for document in documents:

            all_chunks.extend(

                self.chunk_document(
                    document
                )

            )

        return all_chunks


chunking_service = ChunkingService()