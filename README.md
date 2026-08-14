# template-python-tool

PSD401 template for Python tools and libraries. uv-managed, src layout, Python 3.12+.

## What this template gives you

- **uv-managed project**: `pyproject.toml` + committed `uv.lock`, `requires-python >= 3.12`, hatchling build backend, src layout with a typed example module (`src/psd_tool/text.py`, `py.typed` marker).
- **pytest** with real, exact-value assertions covering unicode, truncation, empty input, and both error paths (`tests/test_slugify.py`). PSD CI fails zero-test repos by design.
- **ruff** as both linter and formatter — line length 100, `E W F I UP B SIM RUF` rule set, config lives in `pyproject.toml`.
- **PSD CI wiring** (org reusable workflows), Dependabot (github-actions + uv, weekly, minor/patch grouped), MIT LICENSE, CLAUDE.md.

## The PSD runtime rule

Everything runs through uv — never bare `python` or `pip`:

```bash
uv run pytest          # not: python -m pytest
uv run some_script.py  # not: python some_script.py
```

Single-file scripts declare inline dependencies with **PEP 723** metadata and run with `uv run script.py`:

```python
# /// script
# requires-python = ">=3.12"
# dependencies = ["httpx"]
# ///
```

## First 10 minutes

1. **Rename**: `name` in `pyproject.toml`, the `src/psd_tool/` package directory, the `[tool.hatch.build.targets.wheel]` packages entry, and imports in `tests/`. Naming: lowercase-kebab repo, snake_case package, `psd-` prefix for district-specific tools.
2. **Set repo custom properties**: `tier` (default `c-experiment`), `owner`, `lifecycle: active`; add topics (`python`, …).
3. **Review CLAUDE.md** and prune it to your tool.
4. **Verify green**: `uv sync && uv run pytest && uv run ruff check && uv run ruff format --check`.
5. Replace `text.py`/`test_slugify.py` with your real module and tests — never leave the repo with zero tests.

## Commands

| Task | Command |
|------|---------|
| Install/sync | `uv sync` |
| Test | `uv run pytest` |
| Lint | `uv run ruff check` |
| Format | `uv run ruff format` |
| Format check (CI) | `uv run ruff format --check` |

## Owner

Technology Services, Peninsula School District.
