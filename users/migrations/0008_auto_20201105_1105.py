# Generated by Django 3.1.1 on 2020-11-05 11:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20201104_1151'),
    ]

    operations = [
        migrations.RenameField(
            model_name='action',
            old_name='action',
            new_name='description',
        ),
    ]
