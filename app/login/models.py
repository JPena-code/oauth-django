import uuid

from django.db import models
from django.contrib.auth.models import User
from django.core.validators import URLValidator

from django.utils.translation import gettext_lazy as _

# Create your models here.

class AppUser(models.Model):

    url_validator = URLValidator(['https'])

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,)
    auth_user = models.OneToOneField(
        User,
        verbose_name=_('auth user'),
        on_delete=models.CASCADE,
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
