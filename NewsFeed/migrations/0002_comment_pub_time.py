# Generated by Django 4.0.1 on 2022-03-06 17:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('NewsFeed', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='pub_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date published'),
            preserve_default=False,
        ),
    ]
