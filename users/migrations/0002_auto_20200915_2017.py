# Generated by Django 3.1.1 on 2020-09-15 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0002_organization_students'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='organization',
            field=models.ManyToManyField(related_name='to_user', to='organizations.Organization'),
        ),
    ]
