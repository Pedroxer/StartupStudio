# Generated by Django 4.0.1 on 2022-05-07 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_project_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='project_status',
            field=models.CharField(blank=True, choices=[('p', 'Pending'), ('a', 'Accepted'), ('d', 'Denied'), ('act', 'Active'), ('fin', 'finished')], default='p', help_text='Current project status', max_length=3),
        ),
    ]
