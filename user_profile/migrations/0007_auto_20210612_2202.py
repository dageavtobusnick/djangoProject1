# Generated by Django 3.2 on 2021-06-12 17:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('user_profile', '0006_rename_maincycle_boost_main_cycle'),
    ]

    operations = [
        migrations.AddField(
            model_name='boost',
            name='boostType',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='maincycle',
            name='autoClickPower',
            field=models.IntegerField(default=1),
        ),
    ]
