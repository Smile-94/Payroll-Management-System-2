# Generated by Django 4.1.5 on 2023-03-14 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authority', '0024_weeklyoffday'),
    ]

    operations = [
        migrations.AddField(
            model_name='leaveapplication',
            name='total_days',
            field=models.IntegerField(default=0),
        ),
    ]