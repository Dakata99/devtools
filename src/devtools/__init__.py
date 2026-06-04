"""devtools: centralised dev tooling for all projects."""

from importlib.resources import files
from pathlib import Path


def get_config_path(filename: str) -> Path:
    """Return the absolute path to a bundled config file.

    Usage in consuming repos (if not using the CLI wrappers):
        from devtools import get_config_path
        config = get_config_path("ruff.toml")  # -> Path inside installed package
    """
    config_file = files("devtools") / "configs" / filename
    # `files()` returns a Traversable; resolve to a real Path for CLI use
    return Path(str(config_file))
