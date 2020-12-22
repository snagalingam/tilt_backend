# Generated by Django 3.1.1 on 2020-12-21 22:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('scholarships', '0005_auto_20201217_1229'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='scholarshipstatus',
            options={'verbose_name_plural': 'Scholarship statuses'},
        ),
        migrations.AddField(
            model_name='scholarshipstatus',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='scholarshipstatus',
            name='updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='provider',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='provider',
            name='updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='scholarship',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='scholarship',
            name='updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.RemoveField(
            model_name='scholarshipstatus',
            name='scholarship',
        ),
        migrations.AddField(
            model_name='scholarshipstatus',
            name='scholarship',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='scholarships.scholarship'),
        ),
        migrations.RemoveField(
            model_name='scholarshipstatus',
            name='user',
        ),
        migrations.AddField(
            model_name='scholarshipstatus',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
