# Generated by Django 3.0.7 on 2020-07-21 15:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import mysite.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mysite', '0016_delete_skill'),
    ]

    operations = [
        migrations.CreateModel(
            name='social_media',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('github', models.URLField(blank=True, max_length=512, null=True)),
                ('linkedin', models.URLField(blank=True, max_length=512, null=True)),
                ('telegram', models.URLField(blank=True, max_length=512, null=True)),
                ('instagram', models.URLField(blank=True, max_length=512, null=True)),
                ('twitter', models.URLField(blank=True, max_length=512, null=True)),
                ('bale', models.URLField(blank=True, max_length=512, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='adminProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.FileField(upload_to='user_avatar/', validators=[mysite.models.validate_file_extension])),
                ('description', models.CharField(max_length=512)),
                ('theory', models.CharField(blank=True, max_length=512, null=True)),
                ('social_media', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='mysite.social_media')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
