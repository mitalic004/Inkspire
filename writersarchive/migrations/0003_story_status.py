# Generated by Django 4.2.18 on 2025-02-02 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('writersarchive', '0002_rename_stories_story'),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='status',
            field=models.IntegerField(choices=[(0, 'Draft'), (1, 'Published')], default=0),
        ),
    ]
