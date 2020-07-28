# Generated by Django 3.0.7 on 2020-07-28 08:32

from django.db import migrations, models
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0019_main'),
    ]

    operations = [
        migrations.CreateModel(
            name='centure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('centure_name', models.CharField(max_length=64)),
                ('centure_phone', phone_field.models.PhoneField(blank=True, max_length=31, null=True)),
                ('centure_email', models.EmailField(max_length=254)),
                ('centure_description', models.TextField()),
                ('centure_promote', models.BooleanField(default=False)),
            ],
        ),
    ]