# Generated by Django 2.0.2 on 2018-02-20 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pollingSite', '0017_auto_20180220_2320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classroom',
            name='classKey',
            field=models.CharField(max_length=6, unique=True),
        ),
    ]
