# Generated by Django 3.1.5 on 2021-01-07 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_auto_20201201_1459'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book_Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_id', models.IntegerField()),
                ('code', models.TextField()),
                ('name', models.TextField()),
                ('author', models.TextField()),
                ('ISBN', models.TextField()),
                ('publisher', models.TextField()),
                ('year', models.TextField()),
                ('borrow_cnt', models.IntegerField()),
                ('rate_cnt', models.IntegerField()),
                ('total_rate', models.TextField()),
            ],
        ),
    ]
