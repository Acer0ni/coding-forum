# Generated by Django 4.0 on 2021-12-20 21:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_thread_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='thread',
            name='original_post',
        ),
    ]
