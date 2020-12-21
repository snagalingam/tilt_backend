# Generated by Django 3.1.1 on 2020-12-21 12:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('colleges', '0011_auto_20201109_1133'),
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(blank=True, max_length=255, null=True)),
                ('net_price', models.IntegerField(blank=True, null=True)),
                ('award_uploaded', models.BooleanField(default=False)),
                ('award_reviewed', models.BooleanField(default=False)),
                ('user_notified', models.BooleanField(default=False)),
                ('residency', models.CharField(blank=True, max_length=255, null=True)),
                ('in_state_tuition', models.CharField(blank=True, max_length=255, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('college', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='colleges.college')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='college_status', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'College statuses',
            },
        ),
    ]
