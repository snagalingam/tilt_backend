# Generated by Django 3.1.1 on 2020-09-16 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200916_0402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='income_quintile',
            field=models.CharField(blank=True, default=None, max_length=255, null=True, verbose_name='income quintile'),
        ),
    ]
