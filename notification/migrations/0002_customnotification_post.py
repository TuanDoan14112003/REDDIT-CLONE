# Generated by Django 3.1.1 on 2020-09-26 10:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_auto_20200926_1645'),
        ('notification', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customnotification',
            name='post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='post.post'),
        ),
    ]