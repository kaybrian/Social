# Generated by Django 3.2.14 on 2023-02-24 13:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20230224_1241'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='admin',
        ),
    ]