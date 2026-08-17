# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Flask-based web application that displays course information. The application uses a simple MVC-style architecture with Flask handling routing, view functions rendering templates, and a Course model managing course data. This is currently a minimal starter template (branch `starter-template-jt`) — only an index page and a course detail page exist.

## Development Environment

### Setup

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Unix/Mac
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
# or, per README.md:
uv pip install -r requirements.txt
```

Dependencies (`requirements.txt`): Flask, gunicorn (production WSGI server, not used by `python src/app.py`), python-dotenv (for `.env`, not currently read anywhere in `src/`).

### Running the Application

```bash
python src/app.py
```

The application will be available at `http://127.0.0.1:5000`

### Running Tests

```bash
# Run all tests
python -m unittest discover -s tests

# Run a specific test file
python -m unittest tests.test_app

# Run a specific test case
python -m unittest tests.test_app.AppTestCase.test_index
```

## Architecture

### Application Structure

- **src/app.py**: Application entry point and Flask configuration. Routes are registered using `add_url_rule()` rather than `@app.route()` decorators, which keeps view functions decoupled from Flask and importable on their own.
- **src/views.py**: View functions that handle HTTP requests and return rendered templates. The `course` view looks up a `Course` by treating `course_id` as a 1-based index into `models.courses` (`courses[int(course_id) - 1]`) — there is no bounds/type checking, so a non-numeric or out-of-range `course_id` raises an unhandled exception rather than a 404.
- **src/models.py**: Data models — in-memory `Course` objects stored in a plain list (`courses`). No database backend; all course data is hardcoded.
- **src/templates/**: Jinja2 HTML templates with inheritance (`layout.html` is the base; `index.html` and `course.html` extend it via `{% block content %}`).
- **src/static/css/**: CSS stylesheets for the application.

### Routes

- `/` (`index`) — renders `index.html` (course listing).
- `/course/<course_id>` (`course`) — looks up `courses[int(course_id) - 1]` and renders `course.html` with that `Course` object. `course_id` is 1-based (matching the `Course 1`/`2`/`3` links in `index.html`, which are 0-indexed in the underlying list).

### Data Model

- `Course` (src/models.py): plain class with `title`, `description`, `instructor`, `duration`.
- `courses` is a hardcoded list of 3 `Course` instances. To add a course, append to this list — there is no persistence layer.

## Important Notes

- Virtual environment (`venv/`) should not be committed to version control.
- `src/app.py` imports `views` with a bare `from views import ...`, so the app must be run as `python src/app.py` (or with `src/` on `sys.path`) rather than as a package from the repo root — see how `tests/test_app.py` inserts `src/` into `sys.path` before importing `app`.

## CLAUDE.md Maintenance
This file drifts. When running /init on an existing CLAUDE.md, verify every claim against the actual source files and explicitly list any stale or inaccurate lines you removed rather than silently rewriting.

## Unrelated Repo Contents

The repository root also contains tooling unrelated to the Flask app itself — don't treat these as part of the application architecture:

- **docs/toolkit/**: Reference docs (AsciiDoc) for the phData Toolkit CLI (a separate Snowflake/data-platform tool), not documentation for this app.
- **log-analysis/**: Docker Compose setup for a local Elastic Stack (Elasticsearch, Kibana, Logstash), used for log analysis independent of this Flask app.
- **toolkit.conf** / **.toolkit-metadata**: Configuration for the phData Toolkit CLI.
