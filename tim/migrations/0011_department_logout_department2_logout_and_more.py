# Generated by Django 4.1.7 on 2023-03-01 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tim', '0010_alter_department_day_in_alter_department_time_in_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='logout',
            field=models.TimeField(blank=True, max_length=8, null=True),
        ),
        migrations.AddField(
            model_name='department2',
            name='logout',
            field=models.TimeField(blank=True, max_length=8, null=True),
        ),
        migrations.AddField(
            model_name='department3',
            name='logout',
            field=models.TimeField(blank=True, max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='department',
            name='time_in',
            field=models.TimeField(auto_now_add=True, max_length=8),
        ),
        migrations.AlterField(
            model_name='department2',
            name='time_in',
            field=models.TimeField(auto_now_add=True, max_length=8),
        ),
        migrations.AlterField(
            model_name='department3',
            name='time_in',
            field=models.TimeField(auto_now_add=True, max_length=8),
        ),
    ]