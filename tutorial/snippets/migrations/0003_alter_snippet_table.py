# Generated by Django 3.2.19 on 2023-06-05 07:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0002_rename_snippets_snippet'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='snippet',
            table='snippets_snippet',
        ),
    ]
