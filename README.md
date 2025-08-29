# Bus Ticket Booking Application

This project is a bus ticket booking application that allows users to book seats, view bus routes, and manage their bookings. The application uses a MySQL database to store and manage all the necessary data.

## Installation

1.  **Clone the repository (if applicable):**
    ```bash
    git clone <repository_url>
    cd project-cs
    ```
2.  **Install dependencies:**
    Ensure you have Python installed. Then, install the required libraries using pip:
    ```bash
    pip install -r requirements.txt
    ```

## Database Setup

1.  **MySQL Server:**
    Make sure you have a MySQL server running. The application connects to `localhost` with user `root` and password `test`. You might need to adjust these credentials in `pythonfiles/database adder.py` and `pythonfiles/projectmain.py` if your MySQL setup is different.

2.  **Create Database and Tables:**
    Run the following Python scripts to set up the database and populate it with initial data:
    ```bash
    python pythonfiles/database adder.py
    python pythonfiles/busdataadder.py
    ```
    These scripts will create the `busapp1` database and all necessary tables (`users`, `bus`, `bookings`, `places`, `bus_routes`).

## Running the Application

To start the bus ticket booking application, run the main Python script:
```bash
python pythonfiles/projectmain.py
```

## Database Schema

The application relies on a MySQL database named `busapp1`. The database consists of the following tables:

### `users`

Stores user information and credentials.

- `id`: Primary key (auto-incremented).
- `user_id`: Unique identifier for each user.
- `username`: User's name.
- `password`: User's password.
- `default_image`: A default image identifier for the user profile.

### `bus`

Contains details about the buses available for booking.

- `id`: Primary key (auto-incremented).
- `bus_id`: Unique identifier for each bus.
- `bus_name`: The name of the bus (e.g., "Rockfort Express").
- `cost_per_km`: The cost of travel per kilometer.
- `speed_km_per_h`: The average speed of the bus in km/h.
- `days_column`: Specifies the days the bus runs (e.g., "MondayTuesday").
- `date_column`: Specifies a specific date the bus runs.
- `departure_time`: The departure time of the bus.
- `no_of_columns`: The number of columns for seating arrangements.
- `no_of_rows`: The number of rows for seating arrangements.

### `bookings`

Stores information about all the bookings made by users.

- `id`: Primary key (auto-incremented).
- `user_id`: The ID of the user who made the booking.
- `seat_number`: The seat number that was booked.
- `bus_id`: The ID of the bus for which the booking was made.
- `busdate_id_date`: A composite identifier for the bus and date.
- `booking_date`: The date when the booking was made.

### `places`

A lookup table containing the distances between different places.

- `id`: Primary key (auto-incremented).
- `place1`: The starting location.
- `place2`: The destination.
- `distance`: The distance between `place1` and `place2` in kilometers.

### `bus_routes`

Defines the routes for each bus, listing the places in sequence.

- `route_id`: Primary key (auto-incremented).
- `bus_id`: The ID of the bus.
- `place`: A place on the bus's route.
- `sequence`: The order of the place in the route.
