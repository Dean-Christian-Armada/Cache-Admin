from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _
from django.db import models

# Create your models here.


class CacheAdmin(models.Model):
    """
    @brief      A model not for database but for dmin display
    """

    class Meta:
    	_name = 'Cache Dashboard'
        verbose_name = _(_name)
        verbose_name_plural = _(_name)
        managed = False
