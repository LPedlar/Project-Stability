# Generated by Django 4.2 on 2023-05-08 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employer', '0007_alter_job_dateposted_alter_job_jobdescription_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicant',
            name='Profession',
            field=models.CharField(default='Unemployed', max_length=255),
        ),
    ]