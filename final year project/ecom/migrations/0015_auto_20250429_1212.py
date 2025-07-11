# Generated by Django 3.0.5 on 2025-04-29 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0014_comment_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='OfferBanner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='offer_banner/')),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(max_length=5000),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=400),
        ),
    ]
