# Generated by Django 3.0.7 on 2020-07-28 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0021_auto_20200728_0845'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='main',
            options={'verbose_name': 'navbar', 'verbose_name_plural': 'navbars'},
        ),
        migrations.AlterField(
            model_name='main',
            name='field1',
            field=models.URLField(max_length=64),
        ),
        migrations.AlterField(
            model_name='main',
            name='field2',
            field=models.URLField(max_length=64),
        ),
        migrations.AlterField(
            model_name='main',
            name='field3',
            field=models.URLField(max_length=64),
        ),
        migrations.AlterField(
            model_name='main',
            name='field4',
            field=models.URLField(max_length=64),
        ),
    ]
