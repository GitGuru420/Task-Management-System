from django.urls import path
from tasks.views import admin_view

urlpatterns = [
    path('admin-view/', admin_view),
]
