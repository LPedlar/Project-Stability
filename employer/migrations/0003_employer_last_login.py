# Generated by Django 4.2 on 2023-05-05 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employer', '0002_delete_jobpost_rename_statusid_applicationstatus_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='employer',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
