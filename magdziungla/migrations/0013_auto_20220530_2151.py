# Generated by Django 2.2.28 on 2022-05-30 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magdziungla', '0012_auto_20220530_2118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan',
            name='created',
            field=models.DateTimeField(blank=True),
        ),
    ]
