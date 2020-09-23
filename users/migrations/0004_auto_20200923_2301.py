# Generated by Django 3.1.1 on 2020-09-23 23:01

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20200916_1607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='ethnicity',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=255, null=True, verbose_name='ethnicity'), blank=True, null=True, size=None),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='found_from',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=255, null=True, verbose_name='found from'), blank=True, null=True, size=None),
        ),
    ]
