# Generated by Django 4.2.11 on 2024-03-23 10:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0005_department_alter_user_department'),
    ]

    operations = [
        migrations.CreateModel(
            name='DepartmentCommunicationRule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Название')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='users.department', verbose_name='Подразделение')),
            ],
            options={
                'verbose_name': 'Правило коммуникации подразделений',
                'verbose_name_plural': 'Правила коммуникации подразделений',
            },
        ),
    ]
