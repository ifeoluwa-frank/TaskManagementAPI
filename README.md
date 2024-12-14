# Task Management API

## Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/ifeoluwa-frank/TaskManagementAPI.git

## Navigate to the project directory:
2. cd TaskManagementAPI

## Set up the virtual environment:
3. python -m venv venv
    source venv/bin/activate  # macOS/Linux
    venv\Scripts\activate    # Windows

## Install dependencies:
4. pip install django mysqlclient djangorestframework

## Run the server:
5. python manage.py runserver

## Authentication Setup

This API uses token-based authentication to secure the endpoints.

### 1. Obtain a Token

To authenticate a user and receive a token:

- Send a `POST` request to the `api-token-auth/` endpoint.
- Use `x-www-form-urlencoded` with the following parameters:
  - `username`: Your username
  - `password`: Your password

**Example:**
```bash
POST http://localhost:8000/api-token-auth/
