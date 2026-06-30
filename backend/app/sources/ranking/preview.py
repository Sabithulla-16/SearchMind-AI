from pathlib import Path


MAX_PREVIEW_CHARS = 1500


class PreviewReader:

    def read(
        self,
        path: Path,
    ) -> str:

        try:

            return path.read_text(

                encoding="utf-8",

                errors="ignore",

            )[:MAX_PREVIEW_CHARS]

        except Exception:

            return ""


preview_reader = PreviewReader()