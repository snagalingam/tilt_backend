# Generated by Django 3.1.1 on 2020-12-22 19:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('college_status', '0005_auto_20201222_1914'),
        ('financial_aid', '0008_auto_20201222_1914'),
        ('colleges', '0013_auto_20201222_1914'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CollegeStatus',
        ),
        migrations.AddField(
            model_name='status',
            name='college',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='colleges.college'),
        ),
        migrations.AddField(
            model_name='status',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
