# Generated by Django 3.1.1 on 2020-12-09 15:26

from django.db import migrations, models
import django.db.models.deletion
import django_better_admin_arrayfield.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('college_status', '0003_auto_20200928_2130'),
        ('financial_aid', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AidCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('main_category', models.CharField(blank=True, max_length=255, null=True)),
                ('sub_category', models.CharField(blank=True, max_length=255, null=True)),
                ('sub_sub_category', models.CharField(blank=True, max_length=255, null=True)),
                ('year', models.IntegerField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'aid categories',
            },
        ),
        migrations.RemoveField(
            model_name='documentresult',
            name='expired',
        ),
        migrations.RemoveField(
            model_name='documentresult',
            name='start_date',
        ),
        migrations.AddField(
            model_name='bucketresult',
            name='missing',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='documentresult',
            name='missing_amounts',
            field=django_better_admin_arrayfield.models.fields.ArrayField(base_field=models.CharField(blank=True, max_length=255, null=True), blank=True, null=True, size=None),
        ),
        migrations.AddField(
            model_name='documentresult',
            name='number_of_missing',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='documentresult',
            name='pass_fail',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.CreateModel(
            name='AidData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('amount', models.IntegerField(blank=True, null=True)),
                ('table_number', models.IntegerField(blank=True, null=True)),
                ('row_index', models.IntegerField(blank=True, null=True)),
                ('col_index', models.IntegerField(blank=True, null=True)),
                ('row_data', django_better_admin_arrayfield.models.fields.ArrayField(base_field=models.TextField(blank=True, null=True), blank=True, default=None, null=True, size=None)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('aid_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='financial_aid.aidcategory')),
                ('college_status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='college_status.collegestatus')),
            ],
        ),
    ]
