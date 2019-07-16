# Generated by Django 2.2 on 2019-07-16 16:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resources_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resourcemodel',
            name='user',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='resource_user', to=settings.AUTH_USER_MODEL, verbose_name='Pracownik'),
        ),
    ]
