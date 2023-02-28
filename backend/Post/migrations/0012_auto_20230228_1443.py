# Generated by Django 3.2.14 on 2023-02-28 14:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0011_rename_author_comment_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='comments',
        ),
        migrations.AddField(
            model_name='comment',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='Post.comment'),
        ),
    ]
