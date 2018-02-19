# Generated by Django 2.0.1 on 2018-02-19 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pollingSite', '0004_poll_correct'),
    ]

    operations = [
        migrations.AddField(
            model_name='classroom',
            name='classKey',
            field=models.CharField(default=123456, max_length=6, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='poll',
            name='key',
            field=models.CharField(max_length=6, unique=True),
        ),
    ]
