# Generated by Django 3.2.12 on 2023-01-18 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conferences', '0029_store_selected_bed_layout'),
    ]

    operations = [
        migrations.AddField(
            model_name='keynotespeaker',
            name='user_id',
            field=models.IntegerField(null=True, verbose_name='user'),
        ),
        migrations.AlterField(
            model_name='keynotespeaker',
            name='name',
            field=models.CharField(blank=True, max_length=512, verbose_name='fullname'),
        ),
        migrations.AlterField(
            model_name='keynotespeaker',
            name='photo',
            field=models.ImageField(null=True, upload_to='keynotes', verbose_name='photo'),
        ),
    ]