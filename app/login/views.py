import secrets

import requests
from oauthlib.oauth2 import WebApplicationClient

from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.views.generic import TemplateView
from django.http import HttpRequest, HttpResponseRedirect, Http404

from oath import settings
from .models import AppUser

class Login(TemplateView):
    template_name = 'pages/login.html'

    def post(self, request: HttpRequest, *args, **kwargs):
        client_id = settings.ENV_VARS['CLIENT_ID']
        client = WebApplicationClient(client_id)

        self.request.session['X-STATE'] = secrets.token_urlsafe(16)

        url = client.prepare_request_uri(
            'https://github.com/login/oauth/authorize',
            redirect_uri=settings.ENV_VARS['REDIRECT_URI'],
            scope=['read:user'],
            state=request.session['X-STATE'],
            allow_signup=False)
        client = WebApplicationClient(settings.ENV_VARS['CLIENT_ID'])

        return HttpResponseRedirect(url)


class CallbackOAUTH(TemplateView):

    def get(self, request: HttpRequest, *args, **kwargs):
        request_data = request.GET
        if request_data.get('error', None):
            return Http404()

        if  request_data.get('state', None) != self.request.session['X-STATE']:
            messages.add_message(
                request,
                messages.ERROR,
                'State information mismatch!!!!')
            return HttpResponseRedirect(reverse('login:login'))
        del self.request.session['X-STATE']

        app_client = WebApplicationClient(settings.ENV_VARS['CLIENT_ID'])
        token_body = app_client.prepare_request_body(
            code=request_data['code'],
            client_id=settings.ENV_VARS['CLIENT_ID'],
            client_secret=settings.ENV_VARS['CLIENT_SECRET'],
            redirect_uri=settings.ENV_VARS['REDIRECT_URI'])
        token_response = requests.post(
            'https://github.com/login/oauth/access_token',
            token_body)
        app_client.parse_request_body_response(token_response.text)
        header = {
            'Authorization': f'token {app_client.token["access_token"]}'
        }
        response = requests.get('https://api.github.com/user', headers=header)
        user_info = response.json()

        auth_user, created = User.objects.get_or_create(
            username=user_info['login'],
            defaults={
                'is_superuser': False,
                'email': user_info['email'],
                'first_name': user_info['name']})
        login(self.request, auth_user)
        if created:
            AppUser.objects.create(
                auth_user=auth_user,
                name=user_info['name'],
                avatar_url=user_info['avatar_url'],
                bio=user_info['bio'])

        return HttpResponseRedirect(reverse('home:profile'))
