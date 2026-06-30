from pathlib import Path

from app.sources.models import SourceDocument


class FilesystemParser:

    def parse(
        self,
        path: Path,
    ):

        try:

            text = path.read_text(
                encoding="utf-8",
            )

        except Exception:

            return None

        return SourceDocument(

            title=path.name,

            url=str(path),

            text=text,

            source="filesystem",

            metadata={

                "extension": path.suffix,

                "directory": str(path.parent),

            },

        )


filesystem_parser = FilesystemParser()