# Generated by Django 3.0.1 on 2020-09-02 21:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_customuser_is_onboarded'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='terms_and_conditions',
        ),
    ]
