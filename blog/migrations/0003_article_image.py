# Generated by Django 3.1.6 on 2021-02-14 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210212_2144'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='image',
            field=models.FilePathField(default='default.png', path='/img'),
        ),
    ]