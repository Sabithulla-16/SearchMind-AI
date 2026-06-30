from pathlib import Path

from app.sources.filesystem.filters import (
    file_filter,
)


class FilesystemLoader:

    def load(
        self,
        folder: str,
    ):

        folder = Path(folder)

        files = []

        for path in folder.rglob("*"):

            if not path.is_file():
                continue

            if file_filter.should_skip(path):
                continue

            if not file_filter.is_supported(path):
                continue

            files.append(path)

        return files


filesystem_loader = FilesystemLoader()