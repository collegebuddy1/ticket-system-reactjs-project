# Generated by Django 4.1.7 on 2023-10-26 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event_portal', '0023_rename_ticket_id_ticket_id_category_date_created_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_end_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_end_time',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_start_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_start_time',
            field=models.TimeField(),
        ),
    ]
