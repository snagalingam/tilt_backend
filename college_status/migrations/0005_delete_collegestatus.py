# Generated by Django 3.1.1 on 2020-12-19 11:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('financial_aid', '0007_auto_20201219_1128'),
        ('college_status', '0004_auto_20201213_1321'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CollegeStatus',
        ),
    ]
