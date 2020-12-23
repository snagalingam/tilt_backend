# Generated by Django 3.1.1 on 2020-12-22 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college_status', '0004_auto_20201213_1321'),
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(blank=True, max_length=255, null=True)),
                ('net_price', models.IntegerField(blank=True, null=True)),
                ('award_uploaded', models.BooleanField(default=False)),
                ('reviewed', models.BooleanField(default=False)),
                ('user_notified', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='collegestatus',
            name='college',
        ),
        migrations.RemoveField(
            model_name='collegestatus',
            name='user',
        ),
    ]
