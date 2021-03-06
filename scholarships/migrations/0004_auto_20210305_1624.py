# Generated by Django 3.1.1 on 2021-03-05 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scholarships', '0003_auto_20210207_1100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scholarshipstatus',
            name='status',
            field=models.CharField(choices=[('not interested', 'not interested'), ('interested', 'interested'), ('applied', 'applied'), ('awarded', 'awarded'), ('not awarded', 'not awarded')], max_length=50),
        ),
    ]
