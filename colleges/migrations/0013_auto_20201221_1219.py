# Generated by Django 3.1.1 on 2020-12-21 12:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('colleges', '0012_status'),
    ]

    operations = [
                migrations.RunSQL("""
            INSERT INTO colleges_collegestatus (
                id,
                user_id,
                college_id,
                status,
                net_price,
                award_uploaded,
                award_reviewed,
                user_notified,
                created,
                updated
            )
            SELECT
                id,
                user_id,
                college_id,
                status,
                net_price,
                award_uploaded,
                reviewed,
                user_notified,
                created,
                updated
            FROM
                college_status_collegestatus;
        """, reverse_sql="""
            INSERT INTO college_status_collegestatus (
                id,
                user_id,
                college_id,
                status,
                net_price,
                award_uploaded,
                reviewed,
                user_notified,
                created,
                updated
            )
            SELECT
                id,
                user_id,
                college_id,
                status,
                net_price,
                award_uploaded,
                award_reviewed,
                user_notified,
                created,
                updated
            FROM
                colleges_collegestatus;
        """)
    ]
