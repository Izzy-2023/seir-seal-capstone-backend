# Generated by Django 5.0.3 on 2024-04-22 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='updated_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
