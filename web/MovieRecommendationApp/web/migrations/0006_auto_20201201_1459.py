# Generated by Django 2.2.1 on 2020-12-01 14:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_auto_20201201_1455'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user_book',
            old_name='username',
            new_name='student_id',
        ),
    ]
