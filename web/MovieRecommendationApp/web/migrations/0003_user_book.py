# Generated by Django 2.2.1 on 2020-12-01 14:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_movie_isbn'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.Movie')),
            ],
        ),
    ]
