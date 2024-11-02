from django.contrib import admin
from django.urls import path,include
from apps import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/',include('apps.users.api.urls')),
    path('api/',include('apps.users.api.urls')),
    path('customers/',include('apps.customers.api.urls')),
]
