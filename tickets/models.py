from django.db import models


class Pnr(models.Model):
    code = models.CharField(
        max_length=225, 
        null=True, 
        blank=True, 
        verbose_name='PNR код'
    )

    class Meta:
        verbose_name = 'Код'
        verbose_name_plural = 'Коды'