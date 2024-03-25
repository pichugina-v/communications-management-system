from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

from django_layer.users.managers import UserManager


class Department(models.Model):
    name = models.CharField(verbose_name=_("Название"), max_length=128)

    class Meta:
        verbose_name = _('Подразделение')
        verbose_name_plural = _('Подразделения')

    def __str__(self):
        return self.name


class User(AbstractUser):
    class Status(models.TextChoices):
        ACTIVE = 'ACTIVE', _('Активен')
        NO_ACTIVE = 'BLOCKED', _('Заблокирован')

    CONTACT_METHODS = (
        ('SMS', 'SMS'),
        ('Email', 'Email'),
        ('Messenger', 'Messenger'),
        ('Push', 'Push'),
    )

    username = models.CharField(verbose_name=_('Ник'), max_length=128, blank=True, null=True)
    full_name = models.CharField(verbose_name=_('ФИО'), max_length=256, blank=True, null=True)
    email = models.EmailField(verbose_name=_('Адрес электронной почты'), unique=True)
    password = models.CharField(verbose_name=_('Пароль'), max_length=256, blank=True, null=True)
    phone = PhoneNumberField(unique=True, verbose_name=_('Номер телефона'))
    preferred_contact_method = ArrayField(
        models.CharField(max_length=20, choices=CONTACT_METHODS),
        size=4,
        verbose_name=_("Предпочитаемый способ связи"),
    )
    status = models.CharField(
        verbose_name=_('Статус'),
        max_length=128,
        choices=Status.choices,
        default=Status.ACTIVE
    )
    department = models.ForeignKey(to=Department, verbose_name=_("Подразделение"), on_delete=models.PROTECT, null=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name']

    class Meta:
        verbose_name = _('Пользователь')
        verbose_name_plural = _('Пользователи')

    def __str__(self):
        return self.email
