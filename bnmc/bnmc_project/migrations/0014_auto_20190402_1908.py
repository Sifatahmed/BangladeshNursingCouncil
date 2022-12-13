# Generated by Django 2.0.4 on 2019-04-02 13:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bnmc_project', '0013_auto_20190218_0746'),
    ]

    operations = [
        migrations.CreateModel(
            name='LicenseHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_id', models.IntegerField(blank=True, null=True)),
                ('license_number', models.IntegerField(blank=True, null=True)),
                ('registration_no', models.CharField(blank=True, max_length=300, null=True)),
                ('license_registration_date', models.CharField(blank=True, max_length=120, null=True)),
                ('license_start_date', models.CharField(blank=True, max_length=120, null=True)),
                ('license_end_date', models.CharField(blank=True, max_length=120, null=True)),
                ('date_of_passing', models.CharField(blank=True, max_length=120, null=True)),
                ('lock', models.BooleanField(default=False)),
                ('card_serial', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='final_exam',
            name='program',
        ),
        migrations.RemoveField(
            model_name='final_exam',
            name='year',
        ),
        migrations.RemoveField(
            model_name='license_receive',
            name='license_end_date',
        ),
        migrations.RemoveField(
            model_name='license_receive',
            name='license_number',
        ),
        migrations.RemoveField(
            model_name='license_receive',
            name='license_start_date',
        ),
        migrations.AddField(
            model_name='examsubject',
            name='program',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bnmc_project.Program'),
        ),
        migrations.AddField(
            model_name='examsubject',
            name='year',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bnmc_project.ExamYear'),
        ),
        migrations.AddField(
            model_name='examyear',
            name='program',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bnmc_project.Program'),
        ),
        migrations.AddField(
            model_name='institution',
            name='institution_second_code',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='license_receive',
            name='bank_draft_date',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='license_receive',
            name='bank_draft_no',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='license_receive',
            name='create_on',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='license_receive',
            name='district_snd',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='District_per', to='bnmc_project.District', verbose_name='District'),
        ),
        migrations.AddField(
            model_name='license_receive',
            name='division_snd',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Division_per', to='bnmc_project.Division', verbose_name='Division'),
        ),
        migrations.AddField(
            model_name='license_receive',
            name='email_address',
            field=models.EmailField(blank=True, max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='license_receive',
            name='employer_country',
            field=models.CharField(choices=[('1', 'Bangladesh')], max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='license_receive',
            name='employer_type',
            field=models.CharField(choices=[('1', 'Private'), ('2', 'Public')], max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='license_receive',
            name='entry_id',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='license_receive',
            name='fathers_name',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='license_receive',
            name='guardians_name',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='license_receive',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/', verbose_name='Upload photo'),
        ),
        migrations.AddField(
            model_name='license_receive',
            name='is_old_data',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='license_receive',
            name='license_registration_date',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='license_receive',
            name='license_registration_fee',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='license_receive',
            name='marital_status',
            field=models.CharField(choices=[('1', 'Single'), ('2', 'Married'), ('3', 'Widow'), ('4', 'Divorce'), ('5', 'Separated')], max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='license_receive',
            name='month_info',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='license_receive',
            name='mothers_name',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='license_receive',
            name='passport_no',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='license_receive',
            name='payment_method',
            field=models.CharField(choices=[('1', 'Bank Draft'), ('2', 'Cash'), ('3', 'Cheque')], max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='license_receive',
            name='post_office_snd',
            field=models.CharField(max_length=300, null=True, verbose_name='Post office'),
        ),
        migrations.AddField(
            model_name='license_receive',
            name='postal_code_snd',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='Postal code'),
        ),
        migrations.AddField(
            model_name='license_receive',
            name='quota',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bnmc_project.Quota'),
        ),
        migrations.AddField(
            model_name='license_receive',
            name='registration_fee',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='license_receive',
            name='relation_to_guardians',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bnmc_project.Relation_to_guardians'),
        ),
        migrations.AddField(
            model_name='license_receive',
            name='religions',
            field=models.CharField(choices=[('1', 'Islam'), ('2', 'Hindu'), ('3', 'Buddhist'), ('4', 'Christian'), ('5', 'Others')], max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='license_receive',
            name='sex',
            field=models.CharField(choices=[('1', 'Male'), ('2', 'Female'), ('3', 'Others')], max_length=12, null=True),
        ),
        migrations.AddField(
            model_name='license_receive',
            name='signature',
            field=models.ImageField(blank=True, null=True, upload_to='signature_student/', verbose_name='signature'),
        ),
        migrations.AddField(
            model_name='license_receive',
            name='students',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bnmc_project.Student'),
        ),
        migrations.AddField(
            model_name='license_receive',
            name='students_mobile_no',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='license_receive',
            name='thana_snd',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Thana_per', to='bnmc_project.Thana', verbose_name='Thana'),
        ),
        migrations.AddField(
            model_name='license_receive',
            name='village_snd',
            field=models.CharField(max_length=300, null=True, verbose_name='Village'),
        ),
        migrations.AddField(
            model_name='program',
            name='second_code',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='license_receive',
            name='date_of_birth',
            field=models.CharField(blank=True, max_length=129, null=True),
        ),
        migrations.AlterField(
            model_name='license_receive',
            name='institution',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bnmc_project.Institution'),
        ),
        migrations.AlterField(
            model_name='license_receive',
            name='program',
            field=models.ForeignKey(blank=True, max_length=120, null=True, on_delete=django.db.models.deletion.CASCADE, to='bnmc_project.Program'),
        ),
        migrations.AlterField(
            model_name='student',
            name='institution',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bnmc_project.Institution'),
        ),
        migrations.AddField(
            model_name='licensehistory',
            name='institution',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bnmc_project.Institution'),
        ),
        migrations.AddField(
            model_name='licensehistory',
            name='license_receive_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bnmc_project.license_receive'),
        ),
        migrations.AddField(
            model_name='licensehistory',
            name='license_registration_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bnmc_project.license_registrations'),
        ),
        migrations.AddField(
            model_name='licensehistory',
            name='money_recipte_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bnmc_project.BalanceHistory'),
        ),
        migrations.AddField(
            model_name='licensehistory',
            name='program',
            field=models.ForeignKey(blank=True, max_length=120, null=True, on_delete=django.db.models.deletion.CASCADE, to='bnmc_project.Program'),
        ),
        migrations.AddField(
            model_name='licensehistory',
            name='renew_history',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='bnmc_project.re_new_history', verbose_name='Renew History'),
        ),
        migrations.AddField(
            model_name='licensehistory',
            name='student_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bnmc_project.Student'),
        ),
        migrations.AddField(
            model_name='licensehistory',
            name='student_registration_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bnmc_project.Student_Registration'),
        ),
    ]
