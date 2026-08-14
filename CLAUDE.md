# CLAUDE.md — template-python-tool

Map, not manual. Change this file in the same PR that changes the convention.

## Stack

- Python 3.12+ · uv (packaging, venv, runner) · hatchling build backend · src layout
- pytest · ruff (lint **and** format, config in `pyproject.toml`)

## Commands (exact)

```bash
uv sync                     # install deps into .venv (uv.lock is committed)
uv run pytest               # tests (CI gate; zero-test repos fail psd-ci)
uv run ruff check           # lint
uv run ruff check --fix     # lint with autofix
uv run ruff format          # format
uv run ruff format --check  # CI format gate
```

## Map

- `src/psd_tool/` — the package (rename it). `text.py` is the example module; `py.typed` marks it typed.
- `tests/` — pytest tests, one file per module, exact-value assertions.
- `pyproject.toml` — single source of truth: project metadata, dev deps (`[dependency-groups]`), ruff, pytest.

## Conventions

- **`uv run` everything** — bare `python`/`pip` is never correct here. Single-file scripts use PEP 723 inline metadata.
- Every public function fully typed with a docstring covering args, returns, raises.
- Test-first for non-trivial logic; watch the test fail before making it pass.
- Tests assert exact values and cover edge cases (empty, unicode, boundaries) and error paths (`pytest.raises` with `match=`).
- Existing tests are contracts: weakening or deleting an assertion must be declared in the PR body.
- Dependencies: add with `uv add` (runtime) / `uv add --dev` (dev) so `uv.lock` stays in sync; state why in the PR body.

## Anti-patterns (will fail review)

- `pip install`, `python script.py`, requirements.txt, or a hand-edited `uv.lock`.
- Deleting or skipping a failing test to get green; assertion-free tests.
- Untyped public functions, or `# type: ignore` without an explanatory comment.
- Broad `except Exception` that swallows errors instead of handling specific ones.
- Committing `.venv/` or leaving `uv.lock` out of a dependency-changing PR.

## PR evidence bar

pytest + ruff check + ruff format --check output pasted in the PR; bug fixes include a failing-then-passing test.
