# Generated by Django 2.2.28 on 2022-05-29 21:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('magdziungla', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plant',
            name='preparation_time',
        ),
    ]
