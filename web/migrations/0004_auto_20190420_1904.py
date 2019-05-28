# Generated by Django 2.1.7 on 2019-04-20 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_auto_20190420_1346'),
    ]

    operations = [
        migrations.AddField(
            model_name='search',
            name='status',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='news',
            name='img_path',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]
