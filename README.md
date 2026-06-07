# Rushikesh Raut — Django Portfolio

A professional dark-themed portfolio website built with Django, featuring:
- 🏠 **Home** — Hero section, floating skill badges, featured projects teaser, tech strip
- 👤 **About** — Bio, education timeline, internship experience, certifications
- ⚡ **Skills** — Animated skill bars with icons, grouped by category (Full Stack / Networking / Tools)
- 📁 **Projects** — Detailed project cards with tech tags and descriptions

## Setup & Run

```bash
# 1. Create a virtual environment
python -m venv venv
source venv/bin/activate       # Windows: venv\Scripts\activate

# 2. Install Django
pip install django

# 3. Run migrations (no DB needed — no models used)
python manage.py migrate

# 4. Start server
python manage.py runserver

# 5. Open in browser
# http://127.0.0.1:8000
```

## Project Structure

```
portfolio/          ← Django settings & URLs
main/
  templates/main/
    base.html       ← Shared nav + footer
    home.html       ← Landing page
    about.html      ← About + timeline
    skills.html     ← Skill cards with bars
    projects.html   ← Project showcase
  static/main/
    css/style.css   ← All styles
    js/main.js      ← Scroll animations, nav
  views.py          ← All page views + data
manage.py
```

## Customisation

- Edit `main/views.py` to update skills, projects, or certifications
- Replace the avatar URL in `home.html` / `about.html` with a real photo
- Update contact links (email, LinkedIn) in `base.html` and `about.html`
- Add `ALLOWED_HOSTS` in `portfolio/settings.py` when deploying

## Deployment (e.g. Railway / Render)

```bash
pip install gunicorn whitenoise
# Add to MIDDLEWARE: 'whitenoise.middleware.WhiteNoiseMiddleware'
# Set DEBUG=False, ALLOWED_HOSTS=['yourdomain.com']
gunicorn portfolio.wsgi
```
