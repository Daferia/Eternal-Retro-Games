# Generated by Django 4.1.3 on 2022-12-18 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_remove_userprofile_first_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='default_full_name',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]
