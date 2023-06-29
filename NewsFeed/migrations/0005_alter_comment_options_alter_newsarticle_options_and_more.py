# Generated by Django 4.0.1 on 2022-05-07 08:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('NewsFeed', '0004_alter_comment_user_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['pub_datetime']},
        ),
        migrations.AlterModelOptions(
            name='newsarticle',
            options={'ordering': ['-pub_date'], 'permissions': [('create_new_news', 'Can create new news'), ('delete_their_news', 'Can delete their own news'), ('delete_any_news', 'Can delete any news')]},
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='pub_time',
            new_name='pub_datetime',
        ),
    ]
