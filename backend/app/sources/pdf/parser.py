from app.sources.models import SourceDocument


class PDFParser:

    def parse(
        self,
        document,
        path: str,
    ):

        pages = []

        for page in document:

            pages.append(
                page.get_text()
            )

        text = "\n".join(pages)

        return SourceDocument(

            title=path.split("/")[-1],

            url=path,

            text=text,

            source="pdf",

            metadata={

                "pages": len(document),

            },

        )


pdf_parser = PDFParser()