from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path

from devtools import get_config_path

BASE_CONFIG_TARGET = Path(".mkdocs.base.yml")


def sync() -> None:
    """Copy the packaged shared MkDocs config into the consuming repo."""
    source = get_config_path("mkdocs.base.yml")
    shutil.copyfile(source, BASE_CONFIG_TARGET)
    print(f"Synced {source} -> {BASE_CONFIG_TARGET}")


def build() -> None:
    """Build docs using the shared base config plus local mkdocs.yml."""
    sync()
    subprocess.run(
        ["mkdocs", "build", "--strict", "-f", "mkdocs.yml"],
        check=True,
    )


def serve() -> None:
    """Serve docs locally using the shared base config plus local mkdocs.yml."""
    sync()
    subprocess.run(
        ["mkdocs", "serve", "-f", "mkdocs.yml"],
        check=True,
    )


if __name__ == "__main__":
    command = sys.argv[1] if len(sys.argv) > 1 else "build"

    if command == "sync":
        sync()
    elif command == "build":
        build()
    elif command == "serve":
        serve()
    else:
        raise SystemExit(f"Unknown docs command: {command}")
