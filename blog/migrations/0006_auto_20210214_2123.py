# Generated by Django 3.1.6 on 2021-02-14 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20210214_2121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.FilePathField(path='/image'),
        ),
    ]
