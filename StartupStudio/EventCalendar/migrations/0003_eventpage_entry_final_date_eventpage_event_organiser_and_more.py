# Generated by Django 4.0.1 on 2022-03-07 13:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('EventCalendar', '0002_rename_tags_eventpage_event_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventpage',
            name='entry_final_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='entry deadline'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='eventpage',
            name='event_organiser',
            field=models.CharField(default='Аэрофлот', max_length=60),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='eventpage',
            name='event_prize',
            field=models.CharField(default='1 000 000 ₽', max_length=40),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='eventpage',
            name='event_text',
            field=models.TextField(max_length=2000),
        ),
    ]
