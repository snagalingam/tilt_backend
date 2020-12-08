# Generated by Django 3.1.1 on 2020-12-08 14:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('financial_aid', '0003_auto_20201208_1410'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aiddata',
            name='aid_category',
        ),
        migrations.AddField(
            model_name='aiddata',
            name='aid_category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='financial_aid.aidcategory'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bucketcheck',
            name='bucket',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='documentdata',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
