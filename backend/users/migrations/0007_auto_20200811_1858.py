# Generated by Django 3.0.1 on 2020-08-11 18:58

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20200807_1752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='ethnicity',
            field=models.CharField(choices=[(None, ''), ('american indian and alaska native', 'American Indian/Alaska Native'), ('asian', 'Asian'), ('black and african', 'Black/African'), ('hispanic and latinx', 'Hispanic/Latinx'), ('native hawaiian and pacific islander', 'Native Hawaiian/Pacific Islander'), ('white', 'White'), ('other', 'Other'), ('none', 'None')], default=None, max_length=40, null=True, verbose_name='ethinicity'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='found_from',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(choices=[('instagram', 'Instagram'), ('facebook', 'Facebook'), ('parent', 'Parent'), ('school or district staff', 'School or District Staff'), ('friend', 'Friend'), ('other', 'Other')], max_length=25, verbose_name='found from'), default=None, null=True, size=None),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='high_school_grad_year',
            field=models.IntegerField(blank=True, null=True, verbose_name='high school graduation year'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='income_quintile',
            field=models.CharField(choices=[('none', 'None'), ('lo', '$0 - $30,000'), ('m1', '$30,001 - $48,000'), ('m2', '$48,001 - $75,000'), ('h1', '$75,001 - $110,000'), ('h2', '$110,001+')], default=None, max_length=4, null=True, verbose_name='income quintile'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='user_type',
            field=models.CharField(choices=[('student', 'Student'), ('transfer', 'Transfer'), ('parent', 'Parent'), ('staff', 'Staff'), ('other', 'Other')], default=None, max_length=10, null=True, verbose_name='user type'),
        ),
    ]
