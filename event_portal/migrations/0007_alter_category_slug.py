# Generated by Django 4.1.7 on 2023-02-24 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event_portal', '0006_category_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(editable=False),
        ),
    ]
