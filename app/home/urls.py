from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='profile'),
    path('profile', views.profile, name='profile'),
    path('logout', views.log_out, name='logout')
]
