# Generated by Django 3.1.1 on 2020-12-08 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financial_aid', '0004_auto_20201208_1423'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documentresult',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
