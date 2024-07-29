from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls, name="admin-site"),
    path('', include('app.urls')),
]