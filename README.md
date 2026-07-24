# Meta Back End Developer Capstone Project

This is the capstone project for the Meta Back End Developer course. The project involves creating a web
application for the Little Lemon Restaurant using Django. Additionally, it includes an API for managing
bookings and menus.

## Project Structure

- `littlelemon/`: Django project configuration directory.
- `restaurant/`: Django app for the restaurant functionality.
- `templates/`: Directory containing HTML templates.
- `static/`: Directory containing static files like CSS, JavaScript, and images.
- `tests/`: Directory containing test files.
- `manage.py`: Django management script.

## Setup Instructions

1. Clone the repository.
2. Navigate to the project directory.
3. Create a virtual environment and activate it. Create it by running `python3 -m venv .venv` or the equivalent command for your system.
4. Install the required dependencies using `pip install -r requirements.txt`.
5. Create an empty MySQL database named `LittleLemon`.
6. If you are not using the root MySQL user, create or use a MySQL user with privileges on the `LittleLemon` database.
7. Make sure you change the MySql credentials to match the database, username, and password on your system in `settings.py`
8. Apply migrations using `python manage.py migrate`.
9. Run the development server using `python manage.py runserver`.

## URL Structure and API Testing

- `http://localhost:8000/`: Project Home page.
- `http://localhost:8000/admin/`: Django admin interface.
- `http://localhost:8000/restaurant/`: Restaurant index page.
- `http://localhost:8000/restaurant/menu/`: Menu API list and create endpoint.
- `http://localhost:8000/restaurant/menu/<pk>`: Menu API detail endpoint.
- `http://localhost:8000/restaurant/booking/`: API Bookings page (GET). No Token Needed due to Default Router settings
- `http://localhost:8000/restaurant/booking/tables/`: Table booking list and create endpoint.
- `http://localhost:8000/restaurant/booking/tables/<pk>`: Table booking detail endpoint.
- `http://localhost:8000/auth/`: Root API Authentication endpoints. (GET)
- `http://localhost:8000/auth/users/`: Browsable API URL User List (GET)
- `http://localhost:8000/auth/token/login/`: Authentication token create/login endpoint (POST)
- `http://localhost:8000/auth/token/logout/`: Authentication token logout endpoint (POST)
- `http://localhost:8000/restaurant/api-token-auth/`: Authentication obtain auth token (POST)

Use Insomnia or Postman to test the API endpoints.

Menu API:

- `GET /restaurant/menu/`
- `POST /restaurant/menu/`
- `GET /restaurant/menu/<pk>`
- `PUT /restaurant/menu/<pk>`
- `PATCH /restaurant/menu/<pk>`
- `DELETE /restaurant/menu/<pk>`

Booking API:

- `GET /restaurant/booking/`
- `GET /restaurant/booking/tables/`
- `POST /restaurant/booking/tables/`
- `GET /restaurant/booking/tables/<pk>`
- `PUT /restaurant/booking/tables/<pk>`
- `PATCH /restaurant/booking/tables/<pk>`
- `DELETE /restaurant/booking/tables/<pk>`

Authentication:

- Use a valid token for protected endpoints.
- The booking detail endpoints require authentication.

## Running Tests

Run tests using:

    python manage.py test

The Django test runner creates a temporary database (`test_LittleLemon`) and applies migrations before
running tests.

If your MySQL user is restricted, it must have permission to create databases and modify the temporary test
database. Otherwise, `python manage.py test` may fail during test database creation.

## Usage

Open a web browser and navigate to `http://127.0.0.1:8000/` to access the Little Lemon Restaurant web
application.

## Admin User

To access the Django admin interface, follow these steps:

1. Create an admin user by running `python manage.py createsuperuser`.
2. Start the development server using `python manage.py runserver`.
3. Open a web browser and navigate to `http://127.0.0.1:8000/admin/`.
4. Log in using the admin credentials you created during the setup process.
5. You can manage bookings, menus, and users through the Django admin interface.

## Database Schema

The database schema for the Little Lemon Restaurant web application includes the following models:

- `Booking`: Represents a booking made by a customer.
- `Menu`: Represents a menu item with a Title, Price, and Inventory.
- `User`: Represents a user with a username, email, and password.

## Static Assets

I found the exercise for the static assets instructs the learner to create a blank page leading
to `http://localhost:8000/restaurant/` and does not provide anything regarding the project home page.
At least as far as I understand the instructions. So I am using the index page provided in the static
assets download, and I use that for that restaurant index page and the project home page. Note, none of
the internal links on the home page actually work as they would otherwise lead to protected DRF
endpoints you are supposed to test via Insomnia.

## Using SQLite instead of MySql

By default the Django setup will use the local MySql database which was required for the peer review.
If you want to test the project without using MySql directly you can do this by setting an environement variable before starting the server:

`USE_SQLITE=1`

I set this up so that I can quickly test downloading and setting the project up on my laptop without having to set up a MySql database. The SQLite database will be created in the project root directory as `db.sqlite3`.
