"""CLI entry points — thin wrappers that inject shared configs automatically."""

import sys
from pathlib import Path

from plumbum import FG, local
from plumbum.commands.processes import ProcessExecutionError

from devtools import get_config_path


def _run(cmd: list[str]) -> None:
    """Run a command, streaming output, and exit with its return code."""
    command = local[cmd[0]]
    try:
        command[cmd[1:]] & FG
    except ProcessExecutionError as exc:
        sys.exit(exc.retcode)


def lint() -> None:
    """dev-lint [paths...]  — run ruff linter with shared config."""
    paths = sys.argv[1:] or ["."]
    _run([
        "ruff", "check",
        "--config", str(get_config_path("ruff.toml")),
        *paths,
    ])


def format() -> None:  # noqa: A001
    """dev-fmt [paths...]  — run ruff formatter with shared config."""
    paths = sys.argv[1:] or ["."]
    _run([
        "ruff", "format",
        "--config", str(get_config_path("ruff.toml")),
        *paths,
    ])


def check() -> None:
    """dev-check [paths...]  — run mypy with shared config."""
    paths = sys.argv[1:] or ["."]
    _run([
        "mypy",
        "--config-file", str(get_config_path("mypy.ini")),
        *paths,
    ])
