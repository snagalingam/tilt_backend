# Generated by Django 3.1.1 on 2020-09-13 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_auto_20200912_2126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='gpa',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='GPA'),
        ),
    ]
