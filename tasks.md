# Tasks

Punch list for `course-explainer-app` (branch `starter-template-jt`). Check items off as they're completed.

## Bugs / Robustness

- [ ] `course_id` in `/course/<course_id>` is not validated — a non-numeric or out-of-range value raises an unhandled exception instead of a 404 (`src/views.py`).
- [ ] Decide on and document indexing convention for courses — URLs are 1-based (`courses[int(course_id) - 1]`) while `index.html` links are effectively 0-indexed into the list. This is easy to get wrong when adding courses.

## Features

- [ ] Add a way to persist course data (currently a hardcoded in-memory list in `src/models.py`) — e.g. JSON file, SQLite, or a real database.
- [ ] Add a course creation/edit form (currently read-only).
- [ ] Add search/filter to the course listing page.
- [ ] Wire up `python-dotenv` (`.env` support) — it's a dependency but not currently read anywhere in `src/`.

## Testing

- [ ] Add a test for `/course/<course_id>` with an invalid `course_id` (non-numeric, zero, negative, out-of-range) once bounds checking is added.
- [ ] Add test coverage for `src/models.py`.

## Housekeeping

- [ ] Confirm `venv/` and `.venv/` are both gitignored (two virtualenv directories currently exist side by side).
- [ ] Revisit whether `gunicorn` is needed yet, or defer until deployment is actually set up.
