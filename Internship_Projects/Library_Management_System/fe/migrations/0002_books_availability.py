# Generated by Django 5.1.7 on 2025-03-24 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fe', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='availability',
            field=models.BooleanField(default=False),
        ),
    ]
