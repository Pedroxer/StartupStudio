# Generated by Django 4.0.1 on 2022-03-05 17:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('EventCalendar', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='eventpage',
            old_name='tags',
            new_name='event_tags',
        ),
    ]
