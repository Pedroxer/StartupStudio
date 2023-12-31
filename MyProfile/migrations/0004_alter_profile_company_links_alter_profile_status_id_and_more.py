# Generated by Django 4.2.1 on 2023-07-06 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyProfile', '0003_merge_20230706_2354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='company_links',
            field=models.CharField(help_text='Укажите сайт компании', max_length=500, verbose_name='Company Information'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='status_id',
            field=models.CharField(help_text='Введите статус', max_length=30, verbose_name='Status Name'),
        ),
        migrations.DeleteModel(
            name='Status',
        ),
    ]
