# Django API App

This Django project provides APIs to retrieve and analyze data from a CSV file.

## Setup

1. Clone the repository:

$ git clone <repository_url>
$ cd django-api-app

2. Create and activate a virtual environment:

$ python3 -m venv env
$ source env/bin/activate


3. Install the project dependencies:

$ pip install -r requirements.txt

4. Run database migrations:

$ python manage.py migrate
5. Start the development server:


$ python manage.py runserver


6. The API endpoints are accessible at `http://localhost:8000/api/`.

## API Endpoints

The following API endpoints are available:

- `GET /api/total_items`: Retrieves the total number of items sold within a specified date range and department.

Query Parameters:
- `start_date` (string): Start date in the format 'YYYY-MM-DD'.
- `end_date` (string): End date in the format 'YYYY-MM-DD'.
- `department` (string): Optional department name.

- `GET /api/nth_most_total_item`: Retrieves the nth most sold item in terms of quantity or total price within a specified date range.

Query Parameters:
- `start_date` (string): Start date in the format 'YYYY-MM-DD'.
- `end_date` (string): End date in the format 'YYYY-MM-DD'.
- `item_by` (string): 'quantity' or 'price' to determine the sorting parameter.
- `n` (integer): The value of n for the nth most sold item.

- `GET /api/percentage_of_department_wise_sold_items`: Retrieves the percentage of sold items for each department within a specified date range.

Query Parameters:
- `start_date` (string): Start date in the format 'YYYY-MM-DD'.
- `end_date` (string): End date in the format 'YYYY-MM-DD'.

- `GET /api/monthly_sales`: Retrieves the monthly sales data for a specific product and year.

Query Parameters:
- `product` (string): Product name.
- `year` (integer): Year for which to retrieve the sales data.

## Postman Collection

A Postman collection file named `django_api_app.postman_collection.json` is provided with predefined requests for the above API endpoints. Import the collection into Postman to test the APIs conveniently.
