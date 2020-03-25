# Generated by Django 3.0.1 on 2020-03-25 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Scholarship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('url', models.URLField(max_length=500)),
                ('amount', models.IntegerField()),
                ('amount_descriptor', models.CharField(choices=[('upto', 'up to'), ('exact', 'exact')], default='exact', max_length=5)),
                ('deadline', models.DateField()),
            ],
        ),
    ]
