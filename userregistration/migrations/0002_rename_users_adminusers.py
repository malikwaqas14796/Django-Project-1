# Generated by Django 3.2.5 on 2022-05-09 18:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userregistration', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Users',
            new_name='AdminUsers',
        ),
    ]