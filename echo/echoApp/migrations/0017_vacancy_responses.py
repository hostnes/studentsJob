# Generated by Django 4.2.7 on 2023-11-15 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('echoApp', '0016_summary'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacancy',
            name='responses',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
