# Generated by Django 4.2.1 on 2023-06-18 07:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0004_alltextsstorage'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='alltextsstorage',
            options={'ordering': ['id'], 'verbose_name': 'Тексты для обучения RNN', 'verbose_name_plural': 'Тексты для обучения RNN'},
        ),
    ]
