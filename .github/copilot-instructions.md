# Project Guidelines

## Code Style
Follow Black formatting (100-char lines), pylint and flake8 linting standards. Use mandatory type hints and Google-style docstrings for all functions. Reference [ASSESSMENT_RUBRIC.md](ASSESSMENT_RUBRIC.md) for quality verification commands.

## Architecture
This is an educational repository with two Python curriculums: foundational 16-week course ([PYTHON_COURSE_PLAN.md](PYTHON_COURSE_PLAN.md)) and advanced 14-week library design ([PYTHON_LIBRARY_DESIGN_COURSE_PLAN.md](PYTHON_LIBRARY_DESIGN_COURSE_PLAN.md)). Structure includes curriculum docs, Jupyter notebooks for hands-on learning, CSV datasets, and practice utilities like the Automated File Organizer.

## Build and Test
No automated build system. Run quality checks manually:
- `black --check .` for formatting
- `pylint src/` and `flake8 src/` for linting
- `mypy src/` for type validation
- `pytest tests/` with `pytest --cov=src tests/` for testing and coverage (≥90% required)

Setup: `python3 -m venv venv && source venv/bin/activate && pip install -r requirements.txt`

## Conventions
Always activate virtual environment before running Python. Use pre-commit hooks for Black and pylint. Reference [WEEK_BY_WEEK_GUIDE.md](WEEK_BY_WEEK_GUIDE.md) for weekly tasks and setup patterns. Link to existing documentation instead of duplicating content.