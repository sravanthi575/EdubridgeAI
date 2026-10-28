# 🎓 EduBridge AI — Free Education for Everyone

*Learn for Free. Grow with AI. Build Your Future.*

A Flask web application with free courses, quizzes, an optional AI study assistant,
learning paths, a career hub, a scholarship directory, a student community and an admin panel.

## Features
| Module | What it does |
|---|---|
| Home | Landing page, course search, popular courses |
| Accounts | Register, login/logout, profile, change password (hashed passwords, CSRF protection) |
| Dashboard | Enrolled courses, progress %, quiz scores chart, streak, recommendations, activity |
| Courses | 12 courses / 31 original lessons (Python, HTML, CSS, SQL are the most complete) |
| Practice tests | Multiple choice, difficulty filter, server-side scoring, explanations, history |
| AI Tutor | Optional. Works with an API key; otherwise suggests matching lessons |
| Learning paths | Rule-based paths for 5 goals with manual and automatic progress |
| Career Hub | Resume builder (printable), interview questions, mock interview, projects, skill assessment |
| Scholarships | Directory of **official** links; shows "last verified" date (empty until an admin verifies) |
| Community | Forum (questions, project ideas, study groups), reporting, mentor requests |
| Admin | Courses, lessons, quiz questions, scholarships, mentors, reports, student accounts |

## UI / UX design
| Area | What you get |
|---|---|
| Look | "Chalk and ink" palette (ink, teal, highlighter yellow), Bricolage Grotesque headings, Atkinson Hyperlegible body text, system-font fallbacks (also cover Telugu and Hindi) |
| Themes | Light and dark mode, remembered per device, follows the system setting on first visit |
| Home page | Animated bridge illustration, course search, popular courses, "How it works" steps, AI tutor example, resume call-to-action |
| Navigation | Sticky bar with current-page highlight, "More" menu, account menu, mobile menu, and a bottom tab bar on phones |
| Dashboard | Stat cards, "continue where you left off", quick actions and three charts (quiz scores, course progress, weekly activity) |
| Icons and images | A 30+ icon SVG sprite (`templates/base.html`), inline SVG illustrations (`templates/_macros.html`), subject badges, SVG favicon. No external image files needed |
| Forms | Labelled fields, inline error messages, error summary, show/hide password, strength meter, double-submit protection |
| Feedback | Toast messages with icons (successes fade, errors stay until dismissed), top loading bar, button spinners, chart skeletons, typing indicator in the AI chat |
| Learning UX | Lesson sidebar with progress ticks, reading-progress bar, copy buttons on code, quiz answered counter and score ring |
| Accessibility | Skip link, visible focus rings, ARIA labels and live regions, 44px touch targets, colour never the only signal, reduced-motion support |
| Responsive | Designed for phones first up to wide desktops; tables scroll, grids reflow |

All colours and fonts are CSS variables at the top of `static/css/style.css`, so re-theming takes minutes.
Chart.js is bundled in `static/js/` (MIT licence), so the dashboard charts work offline.

## Run it (Windows)
```
C:\Users\Sindhe Sravanthi\Downloads\EduBridgeAI1\EduBridgeAI>

```
dir

```
py -m venv venv

```
venv\Scripts\activate
```
python -m pip install --upgrade pip
```
python -m pip install -r requirements.txt
```
if not exist .env copy .env.example .env
``
python app.py`
```
 * Running on http://127.0.0.1:5000
```
```
#Open Chrome or another browser and enter:
http://127.0.0.1:5000?utm_source=chatgpt.com
```
```
```
## Create an admin account
Admin rights can **only** be granted from the server (never from a web form):
```bash
flask --app app create-admin
```
or set `ADMIN_EMAIL` and `ADMIN_PASSWORD` in `.env` before starting the app.

## Enable the AI Study Assistant (optional)
Put your key in `.env` (never commit this file):
```
AI_API_KEY=your-key
AI_MODEL=claude-sonnet-5-5
```
The key stays on the server. AI calls cost money, so the rest of the site works without it.

## Run the tests
```bash
python -m pytest -q
```

## Project structure
```
app.py            app factory, CLI commands (seed, create-admin)
config.py         settings from environment variables
extensions.py     db, login manager, CSRF
models/           User, Course/Lesson, Question/QuizAttempt, progress, community, scholarship
routes/           auth, main, courses, quizzes, ai_tutor, paths, career, scholarships, community, admin
services/         ai_service, recommendation_service, progress_service
data/             starter lessons, questions, interview bank, project ideas
templates/        Jinja2 pages (templates/admin for the admin panel)
static/           CSS and JavaScript
tests/            pytest suite
```

## Deploy (e.g. Render)
1. Push to GitHub (`.env` is git-ignored).
2. Create a Web Service. Build: `pip install -r requirements.txt psycopg2-binary`. Start: `gunicorn app:app`.
3. Set environment variables: `SECRET_KEY` (long random value), `DATABASE_URL` (PostgreSQL), `SESSION_COOKIE_SECURE=1`, optional `AI_API_KEY`, `ADMIN_EMAIL`, `ADMIN_PASSWORD`.

## Security notes
- Passwords hashed with Werkzeug; CSRF tokens on every form and AJAX call.
- Quiz scores are computed on the server from the database.
- User text is HTML-escaped; only admin-written lesson HTML is rendered raw.
- Login throttling and AI rate limits are in-memory (per process); use Redis/Flask-Limiter for multi-server production.
- Scholarship details change often. Always verify on the official site before marking a listing "verified".

## Resume points
- Built a full-stack Flask + SQLAlchemy education platform with authentication, role-based admin, quizzes, progress analytics and an optional LLM-powered tutor.
- Implemented CSRF protection, password hashing, server-side validation and an automated pytest suite.
