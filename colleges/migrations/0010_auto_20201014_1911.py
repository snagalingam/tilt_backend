# Generated by Django 3.1.1 on 2020-10-14 19:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('colleges', '0009_auto_20201006_1740'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scorecard',
            name='college',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='colleges.college'),
        ),
    ]
