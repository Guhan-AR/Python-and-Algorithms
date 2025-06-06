# Generated by Django 4.2.20 on 2025-04-09 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0009_venue_db_venue_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='event_db',
            name='event_images',
            field=models.ImageField(blank=True, upload_to='event_images/', verbose_name='event image'),
        ),
        migrations.AddField(
            model_name='turfusers_db',
            name='dp_image',
            field=models.ImageField(blank=True, upload_to='dp_images/', verbose_name='image'),
        ),
    ]
