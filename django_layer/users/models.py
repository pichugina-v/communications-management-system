from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from django_layer.users.managers import UserManager


class User(AbstractUser):

    username = models.CharField(verbose_name=_('Ник'), max_length=128, blank=True, null=True)
    last_name = models.CharField(verbose_name=_('Фамилия'), max_length=128, blank=True, null=True)
    email = models.EmailField(verbose_name=_('Адрес электронной почты'), unique=True)
    password = models.CharField(verbose_name=_('Пароль'), max_length=256, blank=True, null=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name']

    class Meta:
        verbose_name = _('Пользователь')
        verbose_name_plural = _('Пользователи')

    def __str__(self):
        return self.email
