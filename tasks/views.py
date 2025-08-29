from django.shortcuts import render
from django.http import HttpResponse

def home_view(request):
    return HttpResponse("<h1>Welcome to the Task Management System Home Page</h1>")

def admin_view(request):
    return HttpResponse("<h1>Welcome to the Task Management System Admin Page</h1>")