# Generated by Django 4.1.3 on 2023-01-19 23:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_alter_contactus_options_alter_contactus_enquiry_info'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactus',
            name='date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
