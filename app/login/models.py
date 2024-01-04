import uuid
from typing import Any

from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.core.validators import URLValidator, EmailValidator
from django.contrib.auth.validators import UnicodeUsernameValidator

from django.utils.translation import gettext_lazy as _

# Create your models here.

class AppUserManager(models.Manager):

    def create(self, **object_values: Any) -> Any:
        # Create auth user for first login
        if 'auth_user' not in object_values.keys() and 'auth_user' in object_values:
            auth_user = object_values['auth_user']
            object_values['auth_user'] = User.objects.create(**auth_user)
        return super().create(**object_values)

    # def get_or_none(self, *args, **kwargs):
    #     try:
    #         return self.get(args, kwargs)
    #     except ObjectDoesNotExist:
    #         return None


class AppUser(models.Model):

    username_validator = UnicodeUsernameValidator()
    email_validator = EmailValidator()
    url_validator = URLValidator(['https'])

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,)
    auth_user = models.OneToOneField(
        User,
        verbose_name=_('auth user'),
        on_delete=models.DO_NOTHING,
        null=False)
    name = models.CharField(_('name'), max_length=150, blank=False, null=False)
    avatar_url = models.TextField(
        blank=True,
        editable=True,
        help_text='Url of the user avatar',
        validators=[url_validator])
    bio = models.TextField(
        _('Bio description'),
        blank=True,
        null=True,
        help_text=_(
            'Text description from the user profile'))

    REQUIRED_FIELDS = ['name', 'auth_user']

    # objects = AppUserManager()
