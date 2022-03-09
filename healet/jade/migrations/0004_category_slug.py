# Generated by Django 4.0.3 on 2022-03-09 14:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('jade', '0003_product_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default=django.utils.timezone.now, max_length=500, unique_for_date='created'),
            preserve_default=False,
        ),
    ]