# Generated by Django 3.0.3 on 2020-02-28 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0015_auto_20200227_1141'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment_in_comment',
            name='like_num',
        ),
        migrations.AlterField(
            model_name='comment',
            name='like_num',
            field=models.IntegerField(default='0'),
        ),
    ]
