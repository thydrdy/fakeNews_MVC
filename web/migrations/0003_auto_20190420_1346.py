# Generated by Django 2.1.7 on 2019-04-20 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_search'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='down_val',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='news',
            name='up_val',
            field=models.BigIntegerField(default=0),
        ),
    ]
