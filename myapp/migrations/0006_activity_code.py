# Generated by Django 4.1 on 2022-08-28 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_remove_userpackage_id_userpackage_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='code',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
