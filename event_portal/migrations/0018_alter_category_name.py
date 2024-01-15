# Generated by Django 4.1.7 on 2023-03-06 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event_portal', '0017_rename_event_time_event_event_end_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(choices=[('Conferences', 'Conferences'), ('Trade Shows', 'Trade Shows'), ('Networking', 'Networking'), ('WorkShops', 'WorkShops'), ('Product Launch', 'Product Launch'), ('Charity', 'Charity'), ('Music', 'Music'), ('Concert', 'Concert'), ('Performing & Visual Arts', 'Performing & Visual Arts'), ('Food & Drink', 'Food & Drink'), ('Party', 'Party'), ('Sports & Fitness', 'Sports & Fitness')], max_length=40),
        ),
    ]