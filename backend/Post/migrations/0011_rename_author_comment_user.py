# Generated by Django 3.2.14 on 2023-02-28 10:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0010_post_comments'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='author',
            new_name='user',
        ),
    ]
