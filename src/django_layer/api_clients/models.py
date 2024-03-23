from django.db import models
from django.utils.translation import gettext_lazy as _


class APIClient(models.Model):
    app_name = models.CharField(verbose_name=_('Наименование приложения-партнера'), max_length=256)
    description = models.TextField(verbose_name=_('Описание приложения-партнера'), blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Дата создания'))
    access_datetime = models.DateTimeField(verbose_name=_('Срок действия доступа'))
    client_secret = models.CharField(verbose_name=_('Код авторизации клиента'), max_length=64, blank=True)

    class Meta:
        verbose_name = _('Клиент')
        verbose_name_plural = _('Клиенты')

    def __str__(self):
        return self.app_name
