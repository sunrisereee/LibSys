# Generated by Django 5.0.3 on 2024-10-16 08:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('LybrarySystem', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reader',
            old_name='bookBirthday',
            new_name='readerBirthday',
        ),
    ]
