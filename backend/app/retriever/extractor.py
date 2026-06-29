import trafilatura

from app.retriever.models import RetrievedDocument


class Extractor:

    def extract(
        self,
        url: str,
        html: str,
    ):

        metadata = trafilatura.extract_metadata(html)

        content = trafilatura.extract(
            html,
            include_links=False,
            include_images=False,
            include_formatting=False,
            include_tables=True,
            favor_precision=True,
            with_metadata=False,   # <-- IMPORTANT
        )

        if not content:
            return None

        title = ""

        if metadata and metadata.title:
            title = metadata.title

        return RetrievedDocument(
            title=title,
            url=url,
            content=content.strip(),
        )


extractor = Extractor()