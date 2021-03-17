# Generated by Django 3.1.6 on 2021-03-11 09:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('advertisements', '0008_advertisement_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='advertisement', to='advertisements.category'),
        ),
    ]