# Generated by Django 3.2.12 on 2022-03-31 00:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0037_move_speaker_voucher_in_conferences'),
    ]

    operations = [
        migrations.DeleteModel(
            name='SpeakerVoucher',
        ),
    ]