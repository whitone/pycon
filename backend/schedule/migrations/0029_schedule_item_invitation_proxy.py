# Generated by Django 3.2.12 on 2022-02-26 03:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0028_add_more_speaker_statuses_to_allowed_schedule_item_statuses'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScheduleItemInvitation',
            fields=[
            ],
            options={
                'verbose_name': 'Schedule invitation',
                'verbose_name_plural': 'Schedule invitations',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('schedule.scheduleitem',),
        ),
    ]
