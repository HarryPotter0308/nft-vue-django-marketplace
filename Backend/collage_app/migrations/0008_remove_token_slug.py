# Generated by Django 3.2.5 on 2021-07-29 14:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collage_app', '0007_auto_20210729_1409'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='token',
            name='slug',
        ),
    ]
