# Generated by Django 3.0.6 on 2020-08-08 10:31

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0002_auto_20200807_1935'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='student',
            managers=[
                ('students', django.db.models.manager.Manager()),
            ],
        ),
    ]