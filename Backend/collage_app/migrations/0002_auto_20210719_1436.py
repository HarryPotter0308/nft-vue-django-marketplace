# Generated by Django 3.2.5 on 2021-07-19 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collage_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serie',
            name='slug',
            field=models.SlugField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='tokenimage',
            name='slug',
            field=models.SlugField(max_length=100, unique=True),
        ),
    ]
