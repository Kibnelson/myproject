# Generated by Django 2.1.4 on 2018-12-21 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Intbursary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(max_length=200)),
                ('first_name', models.CharField(max_length=200)),
                ('id_number', models.CharField(max_length=200)),
                ('nationality', models.CharField(max_length=200)),
                ('race', models.CharField(choices=[('Black', 'Black'), ('White', 'White'), ('Indian', 'Indian'), ('Colored', 'Colored'), ('Other', 'Other')], max_length=7)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=8)),
                ('telephone_number', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('employed', models.CharField(choices=[('FullTime', 'FullTime'), ('PartTime', 'PartTime'), ('No', 'No')], max_length=10)),
                ('employed_at', models.CharField(max_length=200)),
                ('full_part_time', models.CharField(choices=[('FullTime', 'FullTime'), ('PartTime', 'PartTime')], max_length=10)),
                ('employed_study', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3)),
                ('employed_study_details', models.TextField(max_length=200)),
                ('proposed_degree', models.CharField(choices=[('Msc', 'Msc'), ('PhD', 'PhD')], max_length=3)),
                ('other_funding', models.TextField(max_length=200)),
                ('referee_details', models.TextField(max_length=200)),
                ('degree_1', models.CharField(blank=True, max_length=200)),
                ('f_o_study_1', models.CharField(blank=True, max_length=200)),
                ('major_sub_1', models.CharField(blank=True, max_length=200)),
                ('institution_1', models.CharField(blank=True, max_length=200)),
                ('year_obtained_1', models.CharField(blank=True, max_length=10)),
                ('degree_2', models.CharField(blank=True, max_length=200)),
                ('f_o_study_2', models.CharField(blank=True, max_length=200)),
                ('major_sub_2', models.CharField(blank=True, max_length=200)),
                ('institution_2', models.CharField(blank=True, max_length=200)),
                ('year_obtained_2', models.CharField(blank=True, max_length=10)),
                ('degree_3', models.CharField(blank=True, max_length=200)),
                ('f_o_study_3', models.CharField(blank=True, max_length=200)),
                ('major_sub_3', models.CharField(blank=True, max_length=200)),
                ('institution_3', models.CharField(blank=True, max_length=200)),
                ('year_obtained_3', models.CharField(blank=True, max_length=10)),
                ('degree_4', models.CharField(blank=True, max_length=200)),
                ('f_o_study_4', models.CharField(blank=True, max_length=200)),
                ('major_sub_4', models.CharField(blank=True, max_length=200)),
                ('institution_4', models.CharField(blank=True, max_length=200)),
                ('year_obtained_4', models.CharField(blank=True, max_length=10)),
                ('personal_statement', models.FileField(default='media/uploads/uploadtestdocument.pdf', upload_to='media/uploads/%Y/%m')),
                ('cv', models.FileField(default='media/uploads/uploadtestdocument.pdf', upload_to='media/uploads/%Y/%m')),
                ('transcript', models.FileField(default='media/uploads/uploadtestdocument.pdf', upload_to='media/uploads/%Y/%m')),
                ('ref_letter', models.FileField(default='media/uploads/uploadtestdocument.pdf', upload_to='media/uploads/%Y/%m')),
                ('id_copy', models.FileField(default='media/uploads/uploadtestdocument.pdf', upload_to='media/uploads/%Y/%m')),
                ('article', models.FileField(default='media/uploads/uploadtestdocument.pdf', upload_to='media/uploads/%Y/%m')),
                ('created_at', models.DateTimeField()),
            ],
        ),
    ]
