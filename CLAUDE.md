# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Flask-based web application that displays course information. The application uses a simple MVC-style architecture with Flask handling routing, view functions rendering templates, and a Course model managing course data.

## Development Environment

### Setup

```bash
# Windows
python3 -m venv venv
venv\Scripts\activate

# Unix/Mac
pytho3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Running the Application

```bash
python3 src/app.py
```

The application will be available at `http://127.0.0.1:5000`

### Running Tests

```bash
# Run all tests
python3 -m unittest discover -s tests

# Run a specific test file
python3 -m unittest tests.test_app

# Run a specific test case
python3 -m unittest tests.test_app.AppTestCase.test_index
```

## Architecture

### Application Structure

The application follows a modular Flask design:

- **src/app.py**: Application entry point and Flask configuration. Routes are registered using `add_url_rule()` rather than decorators, which allows views to remain decoupled from Flask.
- **src/views.py**: View functions that handle HTTP requests and return rendered templates. Views are pure functions that don't depend on Flask decorators.
- **src/models.py**: Data models (currently in-memory Course objects stored in a list). No database backend - all course data is hardcoded.
- **src/templates/**: Jinja2 HTML templates with inheritance structure (layout.html as base)
- **src/static/css/**: CSS stylesheets for the application

### Key Design Patterns

1. **Separation of concerns**: Routes (app.py), view logic (views.py), and data (models.py) are separated into distinct modules.
2. **Template inheritance**: Templates use Jinja2's extends/block pattern with layout.html as the base template.
3. **Manual route registration**: Routes are registered with `add_url_rule()` instead of `@app.route()` decorators, allowing view functions to be imported and registered separately.

### Data Model

- Course data is stored in-memory as a list of Course objects in models.py
- No database or persistence layer exists
- To add new courses, modify the `courses` list in models.py

## Important Notes

- `views.py` imports only `render_template` and `request` from Flask, maintaining loose coupling
- Course IDs in URLs are **1-based integers** — `course_id=1` maps to `courses[0]` via `int(course_id) - 1`
- The contact view at `/contact` handles both GET (render form) and POST (validate + process); validation errors are passed back to the template as an `errors` dict
- The `.env` file contains Flask configuration (`FLASK_APP`, `FLASK_ENV`)
- Tests add `src/` to `sys.path` directly — no package `__init__.py` files are used

## Development Workflow

### Add Unit Tests

- Whenever you add any changes add unit tests and run and make sure the tests passes.

### Verify Changes with Playwright (MANDATORY)

**After implementing any new feature, you MUST:**

1. Start the Flask application (if not already running - `python src/app.py`)
2. Use the Playwright MCP tool to connect to the application at `http://127.0.0.1:5000`
3. Navigate to and interact with the new feature to verify it works correctly
4. Take a screenshot of the working feature
5. Save the screenshot in the `test-output/` folder with a descriptive filename (e.g., `feature-name-verification-YYYY-MM-DD.png`)

This step ensures that all features are visually verified and provides documentation of the working state of the application.
