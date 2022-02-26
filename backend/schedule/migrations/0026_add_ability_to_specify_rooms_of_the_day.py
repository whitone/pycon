# Generated by Django 3.2.12 on 2022-02-26 19:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0025_additional_speakers_fk'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='order',
        ),
        migrations.CreateModel(
            name='DayRoomThroughModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveIntegerField(db_index=True, editable=False, verbose_name='order')),
                ('day', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='added_rooms', to='schedule.day', verbose_name='day')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedule.room', verbose_name='room')),
            ],
            options={
                'verbose_name': 'Day - Room',
                'verbose_name_plural': 'Day - Rooms',
                'ordering': ('day', 'order'),
            },
        ),
    ]