# Generated by Django 3.2.25 on 2024-07-20 11:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='asset',
            name='description',
        ),
        migrations.RemoveField(
            model_name='asset',
            name='owner',
        ),
    ]
