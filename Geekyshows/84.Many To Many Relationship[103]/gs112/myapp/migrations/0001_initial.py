# Generated by Django 3.0.6 on 2020-08-12 07:48

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('song_name', models.CharField(max_length=70)),
                ('song_duration', models.IntegerField()),
                ('user', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
