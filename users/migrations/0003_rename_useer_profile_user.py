# Generated by Django 5.0 on 2023-12-10 13:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile_delete_userhistory'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='useer',
            new_name='user',
        ),
    ]
