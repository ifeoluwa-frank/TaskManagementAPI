
# Task Management API

This project is a Django REST Framework (DRF) application for managing tasks. Users can create, view, update, and delete tasks. Admins have additional functionalities such as viewing all tasks in the system. The project also supports filtering and sorting tasks.

## Features

1. User authentication (registration, login, logout).
2. Token-based authorization for secure API access.
3. Task creation, retrieval, update, and deletion.
4. Mark tasks as complete/incomplete.
5. Filter tasks by status, priority, and due date.
6. Sort tasks by priority or due date.
7. Admin-only functionality to view all tasks.

## Requirements

Before setting up the project, ensure the following are installed:

1. **Python** (version 3.8 or higher)
2. **Pip** (Python package manager)
3. **Virtualenv** (for creating a virtual environment)
4. **MySQL** (database server)

Optional but recommended:
- **Git** (for version control)

## Setup Instructions

Follow these steps to set up the project on a new device:

### 1. Clone the Repository
```bash
$ git clone https://github.com/ifeoluwa-frank/TaskManagementAPI.git
```

### 2. Create a Virtual Environment
```bash
$ python3 -m venv env
$ source env/bin/activate  # On Windows: env\Scripts\activate
```

### 3. Install Dependencies
```bash
$ pip install -r requirements.txt
```

### 4. Configure MySQL Database
1. Create a database in MySQL for the project.
2. Update the `.env` file with the database credentials:

```env
SECRET_KEY=<your-secret-key>
DEBUG=True  # Set to False in production
ALLOWED_HOSTS=127.0.0.1,localhost
DATABASE_URL=mysql://<username>:<password>@localhost/<database_name>
```

### 5. Apply Database Migrations
```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

### 6. Create a Superuser
Create an admin user for managing the application:
```bash
$ python manage.py createsuperuser
```
Follow the prompts to set up the superuser credentials.

### 7. Run the Development Server
Start the server to test the application:
```bash
$ python manage.py runserver
```
Access the application in your browser at `http://127.0.0.1:8000/`.

## API Endpoints

### Authentication
- `POST /api/users/` - Register a new user
To authenticate a user and receive a token:
- `POST /api-token-auth/` - Log in and retrieve a token
- Use `x-www-form-urlencoded` with the following parameters:
  - `username`: Your username
  - `password`: Your password

### Task Management
- `GET /api/tasks/` - Retrieve tasks (authenticated users only)
- `POST /api/tasks/` - Create a new task (authenticated users only)
- `PUT /api/tasks/<id>/` - Update a task (authenticated users only)
- `DELETE /api/tasks/<id>/` - Delete a task (authenticated users only)
- `GET /api/tasks/<id>/` - Get a single task (authenticated users only)
- `POST /api/tasks/<id>/status/` - Mark a task as complete/incomplete

### Admin-Specific
- `GET /api/admin/tasks/` - Retrieve all tasks (admins only)

### Filters and Sorting
- Filter tasks by `status`, `priority`, and `due_date`
- Sort tasks by `priority` or `due_date`

Example:
```http
GET /api/tasks/?status=todo&priority=high&ordering=due_date
```

### API Documentation
Comprehensive API documentation is available at:
`https://documenter.getpostman.com/view/28717118/2sAYQUotGa`

## Running Tests
Run tests to ensure everything is functioning correctly:
```bash
$ python manage.py test
```

## Deployment

For deployment:

1. Set `DEBUG=False` in the `.env` file.
2. Configure a production database (e.g., MySQL) and update the `DATABASE_URL` in `.env`.
3. Use a production WSGI server like Gunicorn:
   ```bash
   $ pip install gunicorn
   $ gunicorn project_name.wsgi:application
   ```
4. Use a reverse proxy server like Nginx for better performance and security.

## Troubleshooting

- **Issue:** `ModuleNotFoundError` for installed dependencies
  - **Solution:** Ensure the virtual environment is activated and dependencies are installed using `pip install -r requirements.txt`.

- **Issue:** `RuntimeError: You called this URL via POST, but the URL doesn't end in a slash`
  - **Solution:** Ensure your URLs end with a slash, or set `APPEND_SLASH=False` in `settings.py`.


## License


