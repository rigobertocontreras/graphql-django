# Generated by Django 2.1.7 on 2019-03-17 23:53

from django.db import migrations
from django.contrib.auth.models import User


def create_superuser(apps, schema_editor):
    # admin exists?
    admin_id = 'admin'
    user_list = User.objects.filter(username=admin_id)
    if len(user_list) == 0:
        User.objects.create_superuser(
            username=admin_id, password='admin', email='myemail@gmail.com')


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0001_initial'),
    ]

    operations = [migrations.RunPython(create_superuser)]