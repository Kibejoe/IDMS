# Generated by Django 5.2.4 on 2025-07-09 09:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manufacturers', '0007_alter_employees_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employees',
            old_name='casual_female',
            new_name='casual_females',
        ),
        migrations.RenameField(
            model_name='employees',
            old_name='casual_male',
            new_name='casual_males',
        ),
        migrations.RenameField(
            model_name='employees',
            old_name='proprietor_female',
            new_name='proprietor_females',
        ),
        migrations.RenameField(
            model_name='employees',
            old_name='proprietor_male',
            new_name='proprietor_males',
        ),
        migrations.RenameField(
            model_name='employees',
            old_name='regular_female',
            new_name='regular_females',
        ),
        migrations.RenameField(
            model_name='employees',
            old_name='regular_male',
            new_name='regular_males',
        ),
    ]
