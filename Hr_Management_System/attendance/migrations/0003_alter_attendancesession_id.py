# Generated by Django 5.2 on 2025-05-23 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0002_auto_20250520_2143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendancesession',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
