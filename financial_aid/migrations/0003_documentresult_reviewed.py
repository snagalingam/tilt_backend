# Generated by Django 3.1.1 on 2020-12-10 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financial_aid', '0002_auto_20201209_1526'),
    ]

    operations = [
        migrations.AddField(
            model_name='documentresult',
            name='reviewed',
            field=models.BooleanField(default=False),
        ),
    ]
