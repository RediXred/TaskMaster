# TaskMaster

TaskMaster is a task management application built with Django, Celery, Redis, and PostgreSQL. Users can create, update, delete, and track tasks. The project uses Redis for caching and Celery for asynchronous task processing to improve performance.

## Tech Stack

- Python
- Django
- Django REST Framework
- Celery
- Redis
- PostgreSQL (or any other database of your choice)

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/RediXred/TaskMaster.git
cd TaskMaster
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # for Linux/macOS
venv\Scripts\activate     # for Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the database

This project uses PostgreSQL, but you can use any database. In your `settings.py`, configure the database settings.

Example for PostgreSQL:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'taskmaster_db',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

```

### 6. Apply database migrations

```bash
python manage.py migrate
```

### 7. Create a superuser (optional)

```bash
python manage.py createsuperuser
```

### 8. Run the Django server

```bash
python manage.py runserver
```

The admin panel will be available at [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin).

### 9. Run Celery

To run Celery for handling asynchronous tasks, make sure Redis is running and then start Celery:

Example for Redis:

```bash
celery -A TaskMaster.celery worker --loglevel=info
```

## Testing

Once everything is set up and running, you can test task creation, fetching, updating, and deletion via the API or through the Django admin panel.

### API Endpoints

- **POST** `/api/tasks/` — Create a new task
- **GET** `/api/tasks/` — List all tasks
- **GET** `/api/tasks/{id}/` — Get task details
- **PUT/PATCH** `/api/tasks/{id}/` — Update a task
- **DELETE** `/api/tasks/{id}/` — Delete a task
- **REGISTER** `/api/register/` — Register an account
- **LOGIN** `/api/login/` — Login into account

### Authentication

To interact with the tasks, user authentication is required. JWT tokens are used for authentication. You can get a token by making a request to the login endpoint:
- **LOGIN** `/api/login/` — Login into account
  
Once you have the token, include it in the Authorization header to access protected endpoints.

## Author

XRediX

