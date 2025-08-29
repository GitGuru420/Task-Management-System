from django.contrib import admin
from django.urls import path
from tasks.views import home_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home-view/', home_view),
]
