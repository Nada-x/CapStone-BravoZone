# Generated by Django 4.2.5 on 2023-09-08 18:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_comment_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='user',
        ),
    ]