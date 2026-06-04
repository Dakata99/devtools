# devtools

Centralised formatting, linting, and type-checking tooling for all projects.
Install once, get consistent code quality everywhere.

## Install

```bash
# latest from main
uv add --dev "git+https://github.com/yourorg/devtools.git"

# pin to a tag / commit for reproducibility (recommended)
uv add --dev "git+https://github.com/yourorg/devtools.git@v0.1.0"
```

## Commands

After installing, three commands are available in your project's virtualenv:

| Command | What it does |
|---|---|
| `dev-lint [paths]` | Run **ruff linter** with shared config |
| `dev-fmt [paths]` | Run **ruff formatter** with shared config |
| `dev-check [paths]` | Run **mypy** type checker with shared config |

```bash
uv run dev-lint src/
uv run dev-fmt src/
uv run dev-check src/
```

All three commands accept file/directory paths as arguments. Default is `.`.

## Pre-commit hooks

Copy (or symlink) the bundled config to your repo root:

```bash
cp "$(python -c 'from devtools import get_config_path; print(get_config_path(".pre-commit-config.yaml"))')" .pre-commit-config.yaml
uv run pre-commit install
```

## Extend configs (optional)

If you need to override rules for a specific repo, extend the shared config
rather than replacing it:

```toml
# your-repo/pyproject.toml
[tool.ruff]
extend = "src/devtools/configs/ruff.toml"

[tool.ruff.lint]
ignore = ["B008"]  # add repo-specific ignores on top
```

## Versioning & updates

Pin to a tag in consuming repos so a tooling update doesn't silently change
CI behaviour:

```bash
# bump to a new release
uv add --dev "git+https://github.com/yourorg/devtools.git@v0.2.0"
```

Use tags (`git tag v0.1.0 && git push --tags`) to mark stable releases.

## Releasing a new version

1. Bump `version` in `pyproject.toml`
2. Commit and push
3. `git tag vX.Y.Z && git push --tags`
