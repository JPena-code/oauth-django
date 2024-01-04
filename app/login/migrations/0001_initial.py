# Generated by Django 5.0 on 2024-01-03 13:54

import django.core.validators
import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AppUser',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150, verbose_name='name')),
                ('avatar_url', models.TextField(blank=True, help_text='Url of the user avatar', validators=[django.core.validators.URLValidator(['https'])])),
                ('bio', models.TextField(blank=True, help_text='Text description from the user profile', null=True, verbose_name='Bio description')),
                ('auth_user', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='auth user')),
            ],
        ),
    ]