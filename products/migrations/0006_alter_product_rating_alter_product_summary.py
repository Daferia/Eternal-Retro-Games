# Generated by Django 4.1.3 on 2022-12-07 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_alter_product_summary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='rating',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='summary',
            field=models.TextField(blank=True, null=True),
        ),
    ]
