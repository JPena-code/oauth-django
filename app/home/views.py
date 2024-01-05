from django.urls import reverse
from django.shortcuts import render
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect

# Create your views here.

@login_required(login_url='/login/')
def profile(request: HttpRequest):
    return render(request, 'pages/profile.html')

def index(request: HttpRequest):
    return HttpResponseRedirect(reverse('login:login'), )

def log_out(request: HttpRequest):
    print(request.method)
    if request.method == 'POST':
        logout(request)
        return HttpResponseRedirect(reverse('login:login'), )
    return HttpResponse('request must be post')
