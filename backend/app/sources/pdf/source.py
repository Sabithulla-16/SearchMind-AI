from app.sources.base import BaseSource

from app.sources.pdf.loader import pdf_loader

from app.sources.pdf.parser import pdf_parser

from app.sources.models import SourceResult


class PDFSource(BaseSource):

    name = "pdf"

    async def retrieve(
        self,
        path: str,
    ):

        document = pdf_loader.load(
            path
        )

        parsed = pdf_parser.parse(
            document,
            path,
        )

        return SourceResult(

            source="pdf",

            documents=[parsed],

            statistics={

                "pages": parsed.metadata.get(
                    "pages",
                    0,
                ),

            },

        )


pdf_source = PDFSource()