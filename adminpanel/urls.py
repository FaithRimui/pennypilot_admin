from django.contrib import admin
from django.urls import path
from adminpanel.views import api_admin_login, admin_home

urlpatterns = [
    path('', admin_home),  # This will handle localhost:8000/
    path('admin/', admin.site.urls),
    path('api/admin/login', api_admin_login, name='api_admin_login'),
]
