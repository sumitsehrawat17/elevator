# Generated by Django 4.2.2 on 2023-06-20 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elevator', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='is_complete',
            field=models.BooleanField(default=False),
        ),
    ]
