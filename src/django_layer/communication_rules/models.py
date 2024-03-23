from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.utils.translation import gettext_lazy as _


class DepartmentCommunicationRule(models.Model):
    PERSONAL_CONTACT_METHODS = (
        ('SMS', 'SMS'),
        ('Email', 'Email'),
        ('Messenger', 'Messenger'),
        ('Meeting', 'Meeting'),
        ('Phone call', 'Phone call'),
    )
    MASS_CONTACT_METHODS = (
        ('SMS', 'SMS'),
        ('Email', 'Email'),
        ('Messenger', 'Messenger'),
        ('Push', 'Push'),
    )
    name = models.CharField(verbose_name=_('Название'), max_length=256)
    description = models.TextField(verbose_name=_('Описание'), blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Дата создания'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Дата обновления'))
    department = models.ForeignKey("users.Department", verbose_name=_('Подразделение'), on_delete=models.PROTECT)
    communication_limit = models.PositiveSmallIntegerField(verbose_name=_("Лимит коммуникаций"))
    preferred_mass_channels = ArrayField(
        models.CharField(max_length=20, choices=MASS_CONTACT_METHODS),
        size=4,
        verbose_name=_("Предпочитаемый способ связи"),
    )
    preferred_personal_channels = ArrayField(
        models.CharField(max_length=20, choices=PERSONAL_CONTACT_METHODS),
        size=4,
        verbose_name=_("Предпочитаемый способ связи"),
    )

    class Meta:
        verbose_name = _('Правило коммуникации подразделений')
        verbose_name_plural = _('Правила коммуникации подразделений')

    def __str__(self):
        return self.name
