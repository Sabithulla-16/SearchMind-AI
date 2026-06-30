from pathlib import Path


SUPPORTED_EXTENSIONS = {

    ".py",
    ".js",
    ".ts",
    ".tsx",
    ".jsx",

    ".md",

    ".txt",

    ".json",

    ".yaml",
    ".yml",

    ".html",
    ".css",

}


IGNORED_DIRECTORIES = {

    ".git",

    "__pycache__",

    "node_modules",

    ".next",

    ".venv",

    "venv",

    "dist",

    "build",

    "outputs",

    ".idea",

    ".vscode",

    ".pytest_cache",

    ".mypy_cache",

    ".ruff_cache",

    ".cache",

    ".DS_Store",

}


class FileFilter:

    def is_supported(
        self,
        path: Path,
    ):

        return (
            path.suffix.lower()
            in SUPPORTED_EXTENSIONS
        )

    def should_skip(
        self,
        path: Path,
    ):

        return any(

            part in IGNORED_DIRECTORIES

            for part in path.parts

        )


file_filter = FileFilter()