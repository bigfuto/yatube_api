# Generated by Django 2.2.16 on 2022-10-10 11:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20221010_1426'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='follow',
            name='created',
        ),
    ]
