# Generated by Django 3.2 on 2021-05-20 21:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0003_boost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boost',
            name='mainCycle',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='boosts', to='user_profile.maincycle'),
        ),
    ]
