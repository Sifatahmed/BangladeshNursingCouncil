# Generated by Django 2.0.4 on 2019-07-27 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bnmc_project', '0030_auto_20190710_1652'),
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='applylicense',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
    ]
