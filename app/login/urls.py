from django.urls import path

from . import views

urlpatterns = [
    path('', views.Login.as_view(), name='app.login'),
    path('callback', views.CallbackOAUTH.as_view(), name='app.callback')
]
