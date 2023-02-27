# Generated by Django 3.2.14 on 2023-02-27 14:10

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0002_alter_post_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='unique_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]