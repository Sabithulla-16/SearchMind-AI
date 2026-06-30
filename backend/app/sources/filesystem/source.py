from app.sources.base import BaseSource

from app.sources.filesystem.loader import (
    filesystem_loader,
)

from app.sources.filesystem.parser import (
    filesystem_parser,
)

from app.sources.models import SourceResult


class FilesystemSource(BaseSource):

    name = "filesystem"

    async def retrieve(
        self,
        folder: str,
    ):

        files = filesystem_loader.load(
            folder
        )

        documents = []

        for file in files:

            document = filesystem_parser.parse(
                file
            )

            if document is None:
                continue

            documents.append(
                document
            )

        return SourceResult(

            source="filesystem",

            documents=documents,

            statistics={

                "indexed_files": len(documents),

            },

        )


filesystem_source = FilesystemSource()