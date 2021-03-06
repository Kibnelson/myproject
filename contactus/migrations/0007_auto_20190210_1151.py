# Generated by Django 2.1.4 on 2019-02-10 11:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('contactus', '0006_place'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='place',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
