# Generated by Django 4.1 on 2022-08-28 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_activity_package'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userpackage',
            name='id',
        ),
        migrations.AddField(
            model_name='userpackage',
            name='code',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
