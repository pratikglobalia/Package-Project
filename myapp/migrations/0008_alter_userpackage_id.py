# Generated by Django 4.1 on 2022-08-28 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_remove_activity_code_remove_userpackage_code_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpackage',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
