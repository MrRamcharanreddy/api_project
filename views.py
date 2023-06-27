from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_http_methods
import csv
import os
from datetime import datetime

def read_csv_data(file_path):
    data = []
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        next(reader, None)
        for row in reader:
            data.append(row)
    return data


def filter_transactions_by_date(transactions, start_date, end_date):
    filtered_transactions = []
    for transaction in transactions:
        transaction_date = datetime.strptime(transaction['date'], "%d-%m-%Y %H:%M:%S").date()
        if start_date <= transaction_date <= end_date:
            filtered_transactions.append(transaction)
    return filtered_transactions


def calculate_total_items(transactions):
    total_items = sum(int(transaction['seats']) for transaction in transactions)
    return total_items


def calculate_n_most_sold_item(transactions, item_by, n):
    if item_by == 'quantity':
        sorted_transactions = sorted(transactions, key=lambda t: int(t['seats']), reverse=True)
    elif item_by == 'price':
        sorted_transactions = sorted(transactions, key=lambda t: int(t['amount']), reverse=True)
    else:
        raise ValueError('Invalid item_by parameter.')

    if n <= 0 or n > len(sorted_transactions):
        raise ValueError('Invalid n parameter.')

    nth_item = sorted_transactions[n - 1]['software']
    return nth_item


def calculate_percentage_of_department_wise_sold_items(transactions):
    department_counts = {}
    total_items = 0.0

    for transaction in transactions:
        department = transaction['department']
        seats = int(transaction['seats'])

        if department in department_counts:
            department_counts[department] += seats
        else:
            department_counts[department] = seats

        total_items += seats

    percentages = {
        department: (count / total_items) * 100
        for department, count in department_counts.items()
    }

    return percentages


def calculate_monthly_sales(transactions, product, year):
    monthly_sales = [0] * 12

    for transaction in transactions:
        if transaction['software'] == product and int(transaction['date'][:4]) == year:
            month = int(transaction['date'][5:7])
            monthly_sales[month - 1] += float(transaction['amount'])

    return monthly_sales


def home(request):
    return HttpResponse("Welcome to the API homepage.")


@require_http_methods(["GET"])
def total_items(request):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    csv_file_path = os.path.join(base_dir, 'api_app', 'data.csv')

    try:
        transactions = read_csv_data(csv_file_path)
        start_date = datetime.strptime(request.GET.get('start_date'), '%d-%m-%Y %H:%M:%S').date()
        end_date = datetime.strptime(request.GET.get('end_date'), '%d-%m-%Y %H:%M:%S').date()
        department = request.GET.get('department')

        filtered_transactions = filter_transactions_by_date(transactions, start_date, end_date)

        if department:
            filtered_transactions = [t for t in filtered_transactions if t['department'] == department]

        total_items_count = calculate_total_items(filtered_transactions)

        return JsonResponse({'total_items': total_items_count})

    except FileNotFoundError:
        return JsonResponse({'error': 'Data file not found.'}, status=404)

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


@require_http_methods(["GET"])
def nth_most_total_item(request):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    csv_file_path = os.path.join(base_dir, 'api_app', 'data.csv')

    try:
        transactions = read_csv_data(csv_file_path)
        start_date = datetime.strptime(request.GET.get('start_date'), '%d-%m-%Y %H:%M:%S').date()
        end_date = datetime.strptime(request.GET.get('end_date'), '%d-%m-%Y %H:%M:%S').date()
        item_by = request.GET.get('item_by')
        n = int(request.GET.get('n'))

        filtered_transactions = filter_transactions_by_date(transactions, start_date, end_date)

        nth_item = calculate_n_most_sold_item(filtered_transactions, item_by, n)

        return JsonResponse({'nth_most_total_item': nth_item})

    except FileNotFoundError:
        return JsonResponse({'error': 'Data file not found.'}, status=404)

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


@require_http_methods(["GET"])
def percentage_of_department_wise_sold_items(request):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    csv_file_path = os.path.join(base_dir, 'api_app', 'data.csv')

    try:
        transactions = read_csv_data(csv_file_path)
        start_date = datetime.strptime(request.GET.get('start_date'), '%d-%m-%Y %H:%M:%S').date()
        end_date = datetime.strptime(request.GET.get('end_date'), '%d-%m-%Y %H:%M:%S').date()

        filtered_transactions = filter_transactions_by_date(transactions, start_date, end_date)

        percentages = calculate_percentage_of_department_wise_sold_items(filtered_transactions)

        return JsonResponse({'percentage_of_department_wise_sold_items': percentages})

    except FileNotFoundError:
        return JsonResponse({'error': 'Data file not found.'}, status=404)

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


@require_http_methods(["GET"])
def monthly_sales(request):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    csv_file_path = os.path.join(base_dir, 'api_app', 'data.csv')

    try:
        transactions = read_csv_data(csv_file_path)
        product = request.GET.get('product')
        year = int(request.GET.get('year'))

        filtered_transactions = [t for t in transactions if t['software'] == product and int(t['date'][:4]) == year]

        monthly_sales_data = calculate_monthly_sales(filtered_transactions, product, year)

        return JsonResponse({'monthly_sales': monthly_sales_data})

    except FileNotFoundError:
        return JsonResponse({'error': 'Data file not found.'}, status=404)

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
