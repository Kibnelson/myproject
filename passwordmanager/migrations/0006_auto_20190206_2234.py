# Generated by Django 2.1.4 on 2019-02-06 22:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('passwordmanager', '0005_auto_20190206_1155'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Sacemaaccounts',
        ),
        migrations.DeleteModel(
            name='Socialmedia',
        ),
        migrations.AlterModelOptions(
            name='account',
            options={'verbose_name_plural': ' Accounts for Sacema Logins version 1'},
        ),
    ]