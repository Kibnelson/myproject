# Generated by Django 2.1.4 on 2019-04-26 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TRAP', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tsetse',
            name='alphanumeric_label_for_tube',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='tsetse',
            name='capture_end_time',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='tsetse',
            name='capture_method_code',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='tsetse',
            name='capture_start_time',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='tsetse',
            name='cut_off_al_length_for_deciding_if_fly_aborted',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='tsetse',
            name='determinant_for_pregnancy_stage',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='tsetse',
            name='dissection_day',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='tsetse',
            name='dissection_month',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='tsetse',
            name='dwu',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='tsetse',
            name='error_code_1',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='tsetse',
            name='error_code_2',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='tsetse',
            name='estimated_age_days',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='tsetse',
            name='estimated_birth_day_julian',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='tsetse',
            name='estimated_day_of_pregnancy',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='tsetse',
            name='facwlmnew',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='tsetse',
            name='fatu',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='tsetse',
            name='fwu',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='tsetse',
            name='genus',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='tsetse',
            name='hunger_stage',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='tsetse',
            name='inter_larval_perioed',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='tsetse',
            name='largest_ooctye_diameter_mm_x100',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='tsetse',
            name='largest_ooctye_length_mm_x100',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='tsetse',
            name='left_spermatophore_content_0_to_10',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='tsetse',
            name='mark',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='tsetse',
            name='mother_plus_pupa_dry_weight',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='tsetse',
            name='mother_plus_pupa_fat_weight',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='tsetse',
            name='mother_plus_pupa_resid_dry_weight',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='tsetse',
            name='mother_thorasic_residue_dry_weight',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='tsetse',
            name='mothers_abdominal_resid_dry_weight',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='tsetse',
            name='mothers_dry_weight',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='tsetse',
            name='mothers_fat_weight',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='tsetse',
            name='mothers_haematin',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='tsetse',
            name='mothers_resid_dry_weight',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='tsetse',
            name='ovarian_category',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='tsetse',
            name='percent_pregnancy_completed',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='tsetse',
            name='pteridine',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='tsetse',
            name='puparial_dry_weight_dwp',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='tsetse',
            name='puparial_dry_weight_est_from_volume_erdwp',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='tsetse',
            name='puparial_fat_weight_corrected_for_process_delay_fatp0',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='tsetse',
            name='puparial_fat_weight_fatp',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='tsetse',
            name='puparial_fresh_weight_fwp',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='tsetse',
            name='puparial_length_mm_x100_dpm',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='tsetse',
            name='puparial_length_mm_x100_lpm',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='tsetse',
            name='puparial_resid_dry_weight_rdwp',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='tsetse',
            name='r_is_1_if_disector_noted_a_problem_r_is_0_otherwise',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='tsetse',
            name='rdwu',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='tsetse',
            name='right_spermatophore_content_0_to_10',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='tsetse',
            name='sex',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='tsetse',
            name='time_of_disection_am_or_pm',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='tsetse',
            name='tr',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='tsetse',
            name='tube_number',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='tsetse',
            name='uterine_content',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='tsetse',
            name='uterine_dry_weight_est_from_volume',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='tsetse',
            name='uterine_fat_weight_est_from_volume',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='tsetse',
            name='uterine_fresh_weight_est_from_volume',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='tsetse',
            name='uterine_length_udm_mm_x100',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='tsetse',
            name='uterine_length_ulm_mm_x100',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='tsetse',
            name='uterine_resid_dry_weight_est_from_volume',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='tsetse',
            name='uterine_volume',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='tsetse',
            name='uterine_volume_volp',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='tsetse',
            name='wing_fray_1_to_6',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='tsetse',
            name='wing_length_mm_x100_wlm',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='tsetse',
            name='wing_length_mm_x100_wlm2',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='tsetse',
            name='wing_length_scale_wl',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
