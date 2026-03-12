# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Flask-based web application that displays course information, using a simple MVC-style architecture.

## Commands

```bash
# Setup (Unix/Mac)
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Run application
python3 src/app.py
# Available at http://127.0.0.1:5000

# Run tests
python3 -m unittest discover -s tests          # all tests
python3 -m unittest tests.test_app             # single file
python3 -m unittest tests.test_app.AppTestCase.test_index  # single test
```

## Architecture

- **src/app.py**: Flask entry point. Routes are registered via `add_url_rule()` (not decorators) to keep views decoupled from Flask.
- **src/views.py**: Pure view functions — only imports `render_template` and `request` from Flask.
- **src/models.py**: In-memory `Course` objects in a list. No database — add courses by appending to the `courses` list.
- **src/templates/**: Jinja2 templates using `layout.html` as the base via `extends/block`.
- **tests/test_app.py**: Uses `sys.path.insert` to add `src/` — no `__init__.py` files needed.

## Key Details

- Course IDs in URLs are **1-based** — `course_id=1` maps to `courses[0]` via `int(course_id) - 1`
- `/contact` handles GET (render form) and POST (validate); validation errors are returned as an `errors` dict to the template
- `.env` contains `FLASK_APP` and `FLASK_ENV` configuration

## GitHub Actions

Two Claude-powered workflows in `.github/workflows/`:
- **claude.yml**: Responds to `@claude` mentions in issues, PRs, and comments
- **claude-code-review.yml**: Auto-reviews every PR using the `code-review` plugin

Both require `CLAUDE_CODE_OAUTH_TOKEN` set as a repository secret.

## Development Workflow

### Add Unit Tests
- Whenever you add any changed add unit tests and run to make sure the tests passes

### Verify Chnages with Playwright (MANDATORY)

**After implementing any feature, verify with Playwright (MANDATORY):**
   - Start the app: `python3 src/app.py`
   - Use the Playwright MCP tool to navigate to `http://127.0.0.1:5000`
   - Take a screenshot and save it to `test-output/` with a descriptive filename (e.g., `feature-name-verification-YYYY-MM-DD.png`)
   - Create a PR with details of the changes and share the link with me to review and merge
