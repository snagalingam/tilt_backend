# Generated by Django 3.1.1 on 2020-09-15 19:43

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='College',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit_id', models.CharField(blank=True, max_length=255, null=True)),
                ('ope_id', models.CharField(blank=True, max_length=255, null=True)),
                ('place_id', models.CharField(blank=True, max_length=255, null=True)),
                ('business_status', models.CharField(blank=True, max_length=255, null=True)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=255, null=True)),
                ('lat', models.IntegerField(blank=True, null=True)),
                ('lng', models.IntegerField(blank=True, null=True)),
                ('url', models.TextField(blank=True, null=True)),
                ('website', models.TextField(blank=True, null=True)),
                ('favicon', models.TextField(blank=True, null=True)),
                ('main_photo', models.TextField(blank=True, null=True)),
                ('photos', django.contrib.postgres.fields.ArrayField(base_field=models.TextField(blank=True, null=True), default=None, null=True, size=None)),
                ('types', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=255, null=True), default=None, null=True, size=None)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
    ]
