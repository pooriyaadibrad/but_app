# Generated by Django 5.1.4 on 2025-01-03 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentDormitory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('student_code', models.CharField(max_length=20)),
                ('mobile_number', models.CharField(max_length=20)),
                ('parent_mobile_number', models.CharField(max_length=20)),
                ('nation_code', models.CharField(max_length=20)),
                ('grade', models.IntegerField()),
                ('field', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
            ],
        ),
    ]
