# Generated by Django 2.2 on 2020-08-17 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0030_comment_permission'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='permission',
            field=models.BooleanField(default=False),
        ),
    ]
