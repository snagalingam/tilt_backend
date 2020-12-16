# Generated by Django 3.1.1 on 2020-12-15 15:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('colleges', '0012_status'),
        ('financial_aid', '0005_auto_20201213_1321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aiddata',
            name='college_status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='colleges.status'),
        ),
        migrations.CreateModel(
            name='Summary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_cost', models.IntegerField(blank=True, null=True)),
                ('total_aid', models.IntegerField(blank=True, null=True)),
                ('net_price', models.IntegerField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('college_status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='colleges.status')),
            ],
        ),
    ]
