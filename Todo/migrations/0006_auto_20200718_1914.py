# Generated by Django 3.0.8 on 2020-07-18 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Todo', '0005_auto_20200718_1912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='complete',
            field=models.BooleanField(default=False),
        ),
    ]
