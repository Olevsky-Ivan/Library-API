# LIBRARY API

A RESTful API for managing a library system, built with Django and Django REST Framework (DRF). 

## Features
- User authentication and JWT-based authorization
- Book and author management
- Borrowing system with due dates
- Search and filtering
- Redis caching for performance
- Telegram bot integration for notifications

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/library-api.git
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Apply migrations:
   ```sh
   python manage.py migrate
   ```
4. Run the development server:
   ```sh
   python manage.py runserver
   ```

## API Endpoints
### Authentication
- `POST /api/token/` - Obtain JWT token
- `POST /api/token/refresh/` - Refresh JWT token

### Books
- `GET /api/books/` - List all books
- `POST /api/books/` - Add a new book (admin only)
- `GET /api/books/{id}/` - Retrieve a book
- `PUT /api/books/{id}/` - Update a book (admin only)
- `DELETE /api/books/{id}/` - Delete a book (admin only)

### Authors
- `GET /api/authors/` - List all authors
- `POST /api/authors/` - Add a new author (admin only)
- `GET /api/authors/{id}/` - Retrieve an author
- `PUT /api/authors/{id}/` - Update an author (admin only)
- `DELETE /api/authors/{id}/` - Delete an author (admin only)

### Borrowing
- `GET /api/borrows/` - List all borrow records (admin only)
- `POST /api/borrows/` - Borrow a book (authenticated users)
- `GET /api/borrows/{id}/` - Retrieve a borrow record
- `PUT /api/borrows/{id}/return/` - Return a book

## Technologies
- Django & Django REST Framework
- PostgreSQL
- Redis (for caching and optimization)
- Celery (for background tasks)
- Telegram Bot API (for notifications)

## Usage
- Redis is used to cache frequently accessed data.
- Telegram bot sends notifications about overdue books.
