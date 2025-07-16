# Django Todo List Application

A full-featured todo list application built with Django, featuring user authentication, task management, and due date tracking.

## Features

- ✅ User authentication (login/logout/signup)
- 🗒️ Create, read, update, and delete tasks
- ✔️ Mark tasks as complete/incomplete
- 📅 Due date tracking with calendar input
- 🔍 Search functionality
- 📱 Responsive design (works on mobile/desktop)

## Requirements

- Python 3.8+
- Django 4.0+
- PostgreSQL (recommended) or SQLite

## Installation

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/django-todo.git

cd todoproject
```

2. **Set up virtual environment**
```bash

python -m venv venv

source venv/bin/activate # Linux/Mac

venv\Scripts\activate # Windows
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Configure database**
- For SQLite (default): No setup needed
- For PostgreSQL: Create database and update `settings.py`

5. **Run migrations**
```bash
python manage.py migrate
```
6. **Create superuser (optional)**

```bash
python manage.py createsuperuser
```

7. **Run development server**

```bash
python manage.py runserver
```

## Project Structure
```
django-todo/

├── todo/ # Main app

│ ├── migrations/ # Database migrations

│ ├── templates/ # HTML templates

│ ├── init.py

│ ├── admin.py # Admin configuration

│ ├── apps.py

│ ├── forms.py # Form definitions

│ ├── models.py # Database models

│ ├── tests.py

│ ├── urls.py # App URLs

│ └── views.py # View functions

├── todoproject/ # Project config

│ ├── init.py

│ ├── asgi.py

│ ├── settings.py # Django settings

│ ├── urls.py # Project URLs

│ └── wsgi.py

├── .gitignore

├── LICENSE

├── manage.py

├── README.md

└── requirements.txt
```