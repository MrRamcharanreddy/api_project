from django.urls import path
from api_app import views

urlpatterns = [
    path('', views.home, name='home'),  # Add this line for the root URL
    path('api/total_items/', views.total_items, name='total_items'),
    path('api/nth_most_total_item/', views.nth_most_total_item, name='nth_most_total_item'),
    path('api/percentage_of_department_wise_sold_items/', views.percentage_of_department_wise_sold_items, name='percentage_of_department_wise_sold_items'),
    path('api/monthly_sales/', views.monthly_sales, name='monthly_sales'),
]
