# Meta Back End Developer Capstone Project

This is the capstone project for the Meta Back End Developer course. The project involves creating a web application for the Little Lemon Restaurant using Django.

## Project Structure

- `littlelemon/`: Django project configuration directory.
- `restaurant/`: Django app for the restaurant functionality.
- `templates/`: Directory containing HTML templates.
- `static/`: Directory containing static files like CSS, JavaScript, and images.
- `manage.py`: Django management script.

## Setup Instructions

1. Clone the repository.
2. Navigate to the project directory.
3. Create a virtual environment and activate it.
4. Install the required dependencies using `pip install -r requirements.txt`.
5. Make sure you change the MySql credentials to match the database, username, and password on your system
6. Apply migrations using `python manage.py migrate`.
7. Run the development server using `python manage.py runserver`.

## Usage

Open a web browser and navigate to `http://127.0.0.1:8000/` to access the Little Lemon Restaurant web application.

## Admin User

To access the Django admin interface, follow these steps:

1. Start the development server using `python manage.py runserver`.
2. Open a web browser and navigate to `http://127.0.0.1:8000/admin/`.
3. Log in using the admin credentials you created during the setup process.
4. You can now manage bookings and menus through the Django admin interface.

## Database Schema

The database schema for the Little Lemon Restaurant web application includes the following models:

- `Booking`: Represents a booking made by a customer.
- `Menu`: Represents a menu item with a title, price, and inventory.
