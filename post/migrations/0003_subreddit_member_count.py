# Generated by Django 3.1.1 on 2020-10-07 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_auto_20200926_1645'),
    ]

    operations = [
        migrations.AddField(
            model_name='subreddit',
            name='member_count',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
