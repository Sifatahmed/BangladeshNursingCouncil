# Generated by Django 2.0.4 on 2019-07-10 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bnmc_project', '0025_auto_20190710_1602'),
    ]

    operations = [
        migrations.CreateModel(
            name='RequestedProgram',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('license_number', models.CharField(blank=True, max_length=120, null=True)),
                ('applyLicense', models.ForeignKey(blank=True, null=True, on_delete=None, to='bnmc_project.ApplyLicense')),
                ('program', models.ForeignKey(blank=True, null=True, on_delete=None, to='bnmc_project.Program')),
            ],
        ),
    ]
