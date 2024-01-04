from django.urls import reverse
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect

# Create your views here.
@login_required(login_url='/login/')
def index(request: HttpRequest):
    return HttpResponse('User logged')

def log_out(request: HttpRequest):
    logout(request)
    return HttpResponseRedirect(reverse('app.login'), )
