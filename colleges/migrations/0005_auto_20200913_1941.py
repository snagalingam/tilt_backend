# Generated by Django 3.1.1 on 2020-09-13 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('colleges', '0004_auto_20200831_2138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='college',
            name='phone_number',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
