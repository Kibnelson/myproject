# Generated by Django 2.1.4 on 2019-02-05 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sacemaaccounts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sacemadatabase', models.CharField(blank=True, max_length=200, null=True)),
                ('sacemawebserver', models.CharField(blank=True, max_length=200, null=True)),
                ('boardroomphone', models.CharField(blank=True, max_length=200, null=True)),
                ('GmailCourseApplications', models.CharField(blank=True, max_length=200, null=True)),
                ('eventinvite', models.CharField(blank=True, max_length=200, null=True)),
                ('doorpin', models.CharField(blank=True, max_length=200, null=True)),
                ('pclock', models.CharField(blank=True, max_length=200, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Sacema Account Logins',
            },
        ),
        migrations.CreateModel(
            name='Socialmedia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facebook', models.CharField(blank=True, max_length=200, null=True)),
                ('twitter', models.CharField(blank=True, max_length=200, null=True)),
                ('eventinvite', models.CharField(blank=True, max_length=200, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Social Media',
            },
        ),
    ]
