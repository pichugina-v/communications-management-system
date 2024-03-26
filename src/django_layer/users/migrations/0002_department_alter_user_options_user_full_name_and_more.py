# Generated by Django 4.2.11 on 2024-03-26 09:36

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('name', models.CharField(max_length=128, verbose_name='Название')),
                ('internal_name', models.CharField(max_length=128, primary_key=True, serialize=False, verbose_name='Внутреннее название')),
            ],
            options={
                'verbose_name': 'Подразделение',
                'verbose_name_plural': 'Подразделения',
            },
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'Пользователь', 'verbose_name_plural': 'Пользователи'},
        ),
        migrations.AddField(
            model_name='user',
            name='full_name',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='ФИО'),
        ),
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='user',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(default='+79030000000', max_length=128, region=None, unique=True, verbose_name='Номер телефона'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='preferred_contact_method',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(choices=[('SMS', 'SMS'), ('Email', 'Email'), ('Messenger', 'Messenger'), ('Push', 'Push')], max_length=20), default=['SMS'], size=4, verbose_name='Предпочитаемый способ связи'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='status',
            field=models.CharField(choices=[('ACTIVE', 'Активен'), ('BLOCKED', 'Заблокирован')], default='ACTIVE', max_length=128, verbose_name='Статус'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='Адрес электронной почты'),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='first name'),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='last name'),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Пароль'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Ник'),
        ),
        migrations.AddField(
            model_name='user',
            name='department',
            field=models.ForeignKey(default='marketing', on_delete=django.db.models.deletion.PROTECT, to='users.department', verbose_name='Подразделение'),
            preserve_default=False,
        ),
    ]
