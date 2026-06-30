from app.retriever.models import RetrievedDocument


class DocumentValidator:

    MIN_CONTENT_LENGTH = 250

    def validate(
        self,
        document: RetrievedDocument,
    ) -> bool:

        if not document.title:
            return False

        if not document.content:
            return False

        if len(document.content.strip()) < self.MIN_CONTENT_LENGTH:
            return False

        return True


document_validator = DocumentValidator()