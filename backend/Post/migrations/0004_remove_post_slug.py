# Generated by Django 3.2.14 on 2023-02-27 14:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0003_auto_20230227_1410'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='slug',
        ),
    ]
