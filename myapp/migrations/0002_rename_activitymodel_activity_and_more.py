# Generated by Django 4.1 on 2022-08-25 04:28

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ActivityModel',
            new_name='Activity',
        ),
        migrations.RenameModel(
            old_name='PackageModel',
            new_name='Package',
        ),
    ]