# Generated by Django 4.2.7 on 2023-11-20 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('echoApp', '0024_alter_user_country_alter_user_district_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='summary',
            name='currency',
            field=models.CharField(choices=[('USD', 'USD'), ('BYN', 'BYN'), ('RUB', 'RUB')], default=None, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='summary',
            name='education',
            field=models.CharField(choices=[('-', '-'), ('Higher', 'Higher'), ('Vocational', 'Vocational'), ('Specialized secondary', 'Specialized secondary')], default=None, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='summary',
            name='employment',
            field=models.CharField(choices=[('-', '-'), ('Full employment', 'Full employment'), ('Part-time employment', 'Part-time employment'), ('One-time job', 'One-time job'), ('Internship', 'Internship')], default=None, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='summary',
            name='is_publish',
            field=models.BooleanField(default=True),
        ),
    ]