# Generated by Django 4.1.7 on 2023-05-20 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('badge_scanner', '0003_badgescan_conference'),
    ]

    operations = [
        migrations.AddField(
            model_name='badgescan',
            name='attendee_email',
            field=models.EmailField(default='', max_length=2048, verbose_name='Attendee Email'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='badgescan',
            name='attendee_name',
            field=models.CharField(default='', max_length=2048, verbose_name='Attendee Name'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='badgescan',
            name='scanned_user_id',
            field=models.IntegerField(blank=True, null=True, verbose_name='Attendee'),
        ),
    ]