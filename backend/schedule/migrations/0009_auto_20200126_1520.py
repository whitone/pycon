# Generated by Django 2.2.8 on 2020-01-26 15:20

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0008_auto_20200122_2149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scheduleitem',
            name='additional_speakers',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL, verbose_name='speakers'),
        ),
    ]
