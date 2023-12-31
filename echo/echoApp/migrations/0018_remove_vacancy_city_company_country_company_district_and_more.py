# Generated by Django 4.2.7 on 2023-11-16 08:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('echoApp', '0017_vacancy_responses'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vacancy',
            name='city',
        ),
        migrations.AddField(
            model_name='company',
            name='country',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='echoApp.country'),
        ),
        migrations.AddField(
            model_name='company',
            name='district',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='echoApp.district'),
        ),
        migrations.AddField(
            model_name='company',
            name='region',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='echoApp.region'),
        ),
        migrations.AddField(
            model_name='user',
            name='country',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='echoApp.country'),
        ),
        migrations.AddField(
            model_name='user',
            name='district',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='echoApp.district'),
        ),
        migrations.AddField(
            model_name='vacancy',
            name='country',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='echoApp.country'),
        ),
        migrations.AddField(
            model_name='vacancy',
            name='district',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='echoApp.district'),
        ),
        migrations.AddField(
            model_name='vacancy',
            name='region',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='echoApp.region'),
        ),
        migrations.AlterField(
            model_name='summary',
            name='experience',
            field=models.CharField(choices=[], default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='echoApp.company'),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='experience',
            field=models.CharField(choices=[], default=None, max_length=255, null=True),
        ),
        migrations.DeleteModel(
            name='Experience',
        ),
    ]
