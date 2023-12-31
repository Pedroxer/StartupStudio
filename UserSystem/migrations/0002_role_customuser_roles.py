# Generated by Django 4.0.1 on 2022-05-04 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserSystem', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role_name', models.CharField(max_length=30)),
                ('role_description', models.CharField(max_length=800)),
            ],
        ),
        migrations.AddField(
            model_name='CustomUser',
            name='roles',
            field=models.ManyToManyField(to='UserSystem.Role'),
        ),
    ]
