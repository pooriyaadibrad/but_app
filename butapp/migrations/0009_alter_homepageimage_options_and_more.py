# Generated by Django 5.1.5 on 2025-02-03 23:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('butapp', '0008_alter_homepageimage_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='homepageimage',
            options={'verbose_name': 'عکس های صفحه اصلی خوابگاه', 'verbose_name_plural': 'عکس های صفحه اصلی خوابگاه'},
        ),
        migrations.AlterField(
            model_name='homepageimage',
            name='image',
            field=models.ImageField(upload_to='images/Home', verbose_name='عکس'),
        ),
        migrations.AlterField(
            model_name='studentdormitory',
            name='gender',
            field=models.CharField(choices=[('پسرونه', 'پسرونه'), ('دخترونه', 'دخترونه')], default='دخترونه', max_length=20, verbose_name='جنسیت'),
        ),
        migrations.CreateModel(
            name='CapacityBut',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(verbose_name='تعداد ظرفیت بافی مانده')),
                ('but', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='capacity', to='butapp.but')),
            ],
            options={
                'verbose_name': 'ظرفیت باقی مانده هر خوابگاه',
                'verbose_name_plural': 'ظرفیت باقی مانده هر خوابگاه',
            },
        ),
    ]
