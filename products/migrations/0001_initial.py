# Generated by Django 4.1.3 on 2022-12-06 22:27

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('friendly_name', models.CharField(blank=True, max_length=254, null=True)),
            ],
            options={
                'verbose_name': 'Manufacturer',
                'verbose_name_plural': 'Manufacturers',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku', models.CharField(blank=True, max_length=254, null=True)),
                ('name', models.CharField(blank=True, max_length=254, null=True)),
                ('platform', models.CharField(max_length=35)),
                ('year_of_release', models.IntegerField(default=0)),
                ('has_sizes', models.BooleanField(blank=True, default=False, null=True)),
                ('genre', models.CharField(blank=True, max_length=35, null=True)),
                ('publisher', models.CharField(blank=True, max_length=35, null=True)),
                ('meta_score', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('user_review', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('developer', models.CharField(blank=True, max_length=35, null=True)),
                ('rating', models.CharField(blank=True, max_length=1, null=True)),
                ('selling_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('summary', models.TextField()),
                ('image_url', models.URLField(blank=True, max_length=1024, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('manufacturer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.manufacturer')),
            ],
        ),
    ]
