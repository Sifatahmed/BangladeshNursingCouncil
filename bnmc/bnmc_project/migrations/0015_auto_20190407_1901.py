# Generated by Django 2.1.1 on 2019-04-07 19:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bnmc_project', '0014_auto_20190402_1908'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubSubject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marks', models.FloatField(blank=True, default=0.0, null=True)),
                ('pass_marks', models.FloatField(blank=True, default=0.0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SubSubjectName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
            ],
        ),
        migrations.AddField(
            model_name='examinationstudentregistration',
            name='student_id',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='examinationstudentregistration',
            name='student_signature',
            field=models.ImageField(blank=True, upload_to='signature_student/', verbose_name='Candidate Signature'),
        ),
        migrations.AddField(
            model_name='examsubject',
            name='discription',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='examsubject',
            name='is_active',
            field=models.BooleanField(blank=True, default=True),
        ),
        migrations.AlterField(
            model_name='institution',
            name='principal_signature',
            field=models.FileField(blank=True, null=True, upload_to='media/', verbose_name='Upload photo'),
        ),
        migrations.AlterField(
            model_name='license_receive',
            name='is_old_data',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='licensehistory',
            name='lock',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AddField(
            model_name='subsubject',
            name='exam_subject',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bnmc_project.ExamSubject'),
        ),
        migrations.AddField(
            model_name='subsubject',
            name='subject_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bnmc_project.SubSubjectName'),
        ),
    ]
