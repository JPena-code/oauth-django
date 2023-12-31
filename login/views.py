from django.shortcuts import render
from django.http import HttpRequest

def home(request: HttpRequest, *args, **kwargs):
    return render(request, 'pages/login.html')
