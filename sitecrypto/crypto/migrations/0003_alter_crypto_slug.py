# Generated by Django 4.2.15 on 2024-08-28 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crypto', '0002_crypto_slug_alter_crypto_time_update_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crypto',
            name='slug',
            field=models.SlugField(max_length=255, unique=True),
        ),
    ]
