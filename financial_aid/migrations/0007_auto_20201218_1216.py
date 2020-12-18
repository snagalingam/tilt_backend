# Generated by Django 3.1.1 on 2020-12-18 12:16

from django.db import migrations, models
import django.db.models.deletion
import django_better_admin_arrayfield.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('colleges', '0012_auto_20201218_1216'),
        ('financial_aid', '0006_auto_20201217_1225'),
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, null=True)),
                ('amount', models.IntegerField(blank=True, null=True)),
                ('table_number', models.IntegerField(blank=True, null=True)),
                ('row_index', models.IntegerField(blank=True, null=True)),
                ('col_index', models.IntegerField(blank=True, null=True)),
                ('row_data', django_better_admin_arrayfield.models.fields.ArrayField(base_field=models.TextField(blank=True, null=True), blank=True, default=None, null=True, size=None)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
            ],
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
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='colleges.status')),
            ],
            options={
                'verbose_name_plural': 'Summaries',
            },
        ),
        migrations.RemoveField(
            model_name='aiddata',
            name='aid_category',
        ),
        migrations.RemoveField(
            model_name='aiddata',
            name='college_status',
        ),
        migrations.DeleteModel(
            name='BucketCheck',
        ),
        migrations.DeleteModel(
            name='BucketResult',
        ),
        migrations.RenameModel(
            old_name='AidCategory',
            new_name='Category',
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.DeleteModel(
            name='AidData',
        ),
        migrations.AddField(
            model_name='data',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='financial_aid.category'),
        ),
        migrations.AddField(
            model_name='data',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='colleges.status'),
        ),
    ]
