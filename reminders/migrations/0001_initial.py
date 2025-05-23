# Generated by Django 4.2.16 on 2025-05-21 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reminder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('message', models.TextField()),
                ('reminder_type', models.CharField(choices=[('SMS', 'SMS'), ('EMAIL', 'Email')], max_length=10)),
            ],
        ),
    ]
