# Generated by Django 2.0.1 on 2018-02-23 02:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20180209_1552'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='upload',
        ),
    ]
