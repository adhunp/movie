# Generated by Django 4.1.3 on 2022-12-07 07:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('USER', '0002_rename_user_userdetails'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='userdetails',
            table='tb_user',
        ),
    ]
