# Generated by Django 2.2 on 2020-05-27 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0004_auto_20200527_1826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailservice',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
