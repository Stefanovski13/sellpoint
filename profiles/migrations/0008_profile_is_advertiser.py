# Generated by Django 3.1.6 on 2021-04-02 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0007_remove_profile_savedad'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='is_advertiser',
            field=models.BooleanField(default=False),
        ),
    ]