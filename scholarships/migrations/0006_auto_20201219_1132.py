# Generated by Django 3.1.1 on 2020-12-19 11:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('scholarships', '0005_auto_20201217_1229'),
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(blank=True, max_length=255, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('scholarship', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scholarships.scholarship')),
                ('user', models.ManyToManyField(related_name='scholarship_status', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Scholarship statuses',
            },
        ),
        migrations.DeleteModel(
            name='ScholarshipStatus',
        ),
    ]
