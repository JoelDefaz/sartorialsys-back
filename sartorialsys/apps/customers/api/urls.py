from django.urls import path
from apps.customers.api.api import *

urlpatterns = [
    path('', customer_api_view, name='customers'),
    path('<int:pk>/', customer_update_view, name='customer-update'),
]
