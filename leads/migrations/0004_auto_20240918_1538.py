# Generated by Django 3.1.4 on 2024-09-18 06:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0003_auto_20240918_1516'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='is_organizar',
            new_name='is_organizer',
        ),
    ]
