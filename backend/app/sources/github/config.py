import tempfile
from pathlib import Path


TEMP_REPOSITORY_DIR = (
    Path(tempfile.gettempdir())
    / "searchmind_repositories"
)