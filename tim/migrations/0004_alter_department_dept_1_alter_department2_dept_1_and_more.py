# Generated by Django 4.1.7 on 2023-02-25 03:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tim', '0003_alter_department_dept_1_alter_department2_dept_1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='dept_1',
            field=models.OneToOneField(max_length=50, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='department2',
            name='dept_1',
            field=models.OneToOneField(max_length=50, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='department3',
            name='dept_1',
            field=models.OneToOneField(max_length=50, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
