# Generated by Django 4.0.1 on 2022-05-07 08:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('EventCalendar', '0008_alter_eventcomment_user_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='eventpage',
            options={'ordering': ['-start_date']},
        ),
    ]
