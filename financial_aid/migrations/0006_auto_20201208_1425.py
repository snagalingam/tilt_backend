# Generated by Django 3.1.1 on 2020-12-08 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financial_aid', '0005_auto_20201208_1424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bucketcheck',
            name='bucket',
            field=models.CharField(blank=True, max_length=255, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='documentdata',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='documentresult',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True, unique=True),
        ),
    ]
