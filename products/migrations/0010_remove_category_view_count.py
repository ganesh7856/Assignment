# Generated by Django 3.0.8 on 2020-11-21 12:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_auto_20201121_1817'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='view_count',
        ),
    ]
