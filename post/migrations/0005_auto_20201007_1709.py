# Generated by Django 3.1.1 on 2020-10-07 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_auto_20201007_1705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subreddit',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
