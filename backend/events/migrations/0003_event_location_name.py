# Generated by Django 2.2.5 on 2019-09-25 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_event_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='location_name',
            field=models.CharField(blank=True, max_length=200, verbose_name='location name'),
        ),
    ]
