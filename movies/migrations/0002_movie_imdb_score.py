# Generated by Django 3.0.3 on 2020-02-22 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='imdb_score',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
