# Generated by Django 4.1.5 on 2023-01-20 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='score',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
