# Generated by Django 3.1.6 on 2021-02-14 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20210214_1653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.FilePathField(),
        ),
    ]
