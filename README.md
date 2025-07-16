# Hello SAT Math Practice App

This Django project provides a simple practice interface for SAT math questions. It includes an admin console for managing topics, skillsets and questions, as well as a minimal Vue.js frontend for practicing.

## Initial setup

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Apply database migrations:

```bash
python manage.py migrate
```

This creates the `practice_topic`, `practice_skillset` and related tables required for the admin.

3. Create a superuser to access the admin:

```bash
python manage.py createsuperuser
```

4. Run the development server:

```bash
python manage.py runserver
```

Then open `http://localhost:8000/` in a browser.
