# Generated by Django 3.0.1 on 2020-08-12 04:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organization',
            name='members',
        ),
    ]
