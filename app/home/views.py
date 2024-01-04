from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/login/')
def index(request: HttpRequest):
    return HttpResponse('User logged')
