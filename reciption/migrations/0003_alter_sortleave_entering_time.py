# Generated by Django 4.1.5 on 2023-02-05 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reciption', '0002_sortleave'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sortleave',
            name='entering_time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
