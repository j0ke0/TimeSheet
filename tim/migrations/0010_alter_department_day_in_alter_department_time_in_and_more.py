# Generated by Django 4.1.7 on 2023-03-01 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tim', '0009_department_day_in_department_time_in_department3_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='day_in',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='department',
            name='time_in',
            field=models.TimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='department2',
            name='day_in',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='department2',
            name='time_in',
            field=models.TimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='department3',
            name='day_in',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='department3',
            name='time_in',
            field=models.TimeField(auto_now_add=True),
        ),
    ]
