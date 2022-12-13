# Generated by Django 2.0.4 on 2019-09-14 07:36

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bnmc_project', '0039_userpermissionresult'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userpermissionresult',
            name='user',
        ),
        migrations.AddField(
            model_name='userpermissionresult',
            name='user',
            field=models.ForeignKey(null=True, on_delete=None, to=settings.AUTH_USER_MODEL),
        ),
    ]