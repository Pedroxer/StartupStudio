# Generated by Django 4.0.1 on 2022-05-18 07:59

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_alter_project_options_alter_project_pub_date_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['project_start'], 'permissions': [('can_manage_projects', 'Can manage projects'), ('can_moderate_projects', 'Can moderate incoming projects'), ('can_create_projects', 'Can create projects')]},
        ),
        migrations.AddField(
            model_name='projectentry',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 18, 7, 59, 4, 97322, tzinfo=utc), verbose_name='Время, когда заяка была отправлена'),
        ),
        migrations.AddField(
            model_name='projectentry',
            name='status_changed_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 18, 7, 59, 4, 97322, tzinfo=utc), verbose_name='Время, когда статус заявки был изменен'),
        ),
        migrations.AlterField(
            model_name='project',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 18, 7, 59, 4, 95321, tzinfo=utc), verbose_name='Date Time published'),
        ),
        migrations.AlterField(
            model_name='projectentry',
            name='status',
            field=models.CharField(blank=True, choices=[('pen', 'На рассмотрении'), ('acc', 'Заявка одобрена'), ('den', 'Заявка отклонена')], default='pen', help_text='Current entry status', max_length=3),
        ),
    ]
