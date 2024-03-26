# Generated by Django 4.2.11 on 2024-03-26 10:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_department_alter_user_options_user_full_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='users.department', verbose_name='Подразделение'),
        ),
    ]