from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='app.home'),
    path('logout', views.logout, name='app.logout')
]
