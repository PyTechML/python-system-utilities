# Duplicate File Finder — hashing utilities
# Provides content hashing helpers used across the folder.

from pathlib import Path
import hashlib


def file_hash(path: Path, chunk_size: int = 8192) -> str:
    hasher = hashlib.sha256()

    with path.open("rb") as f:
        while chunk := f.read(chunk_size):
            hasher.update(chunk)

    return hasher.hexdigest()


