# Generated by Django 3.1.1 on 2020-09-26 10:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True),
        ),
    ]
