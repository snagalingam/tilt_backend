# Generated by Django 3.0.1 on 2020-08-28 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('colleges', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='college',
            name='favicon',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
