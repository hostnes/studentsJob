# Generated by Django 4.2.7 on 2023-11-15 17:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('echoApp', '0015_vacancy_education'),
    ]

    operations = [
        migrations.CreateModel(
            name='Summary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('date_of_create', models.DateField(auto_now_add=True)),
                ('experience', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='echoApp.experience')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='echoApp.user')),
            ],
        ),
    ]
