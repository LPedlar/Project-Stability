# Generated by Django 4.2 on 2023-05-06 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employer', '0004_applicant_last_login'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicant',
            name='is_applicant',
            field=models.BooleanField(default=True),
        ),
    ]
