from django.db import models


class Airport(models.Model):
    iata_code = models.CharField(
        max_length=6, 
        null=True, 
        blank=True, 
        verbose_name='IATA код'
    )
    name = models.CharField(
        max_length=70,
        null=True,
        blank=True,
        verbose_name='Имя'
    )

    class Meta:
        verbose_name = 'Аэрапорт'
        verbose_name_plural = 'Аэропорта'

    def __str__(self):
        return f"{self.name}"
    
class Company(models.Model):
    iata_code = models.CharField(
        max_length=6, 
        null=True, 
        blank=True, 
        verbose_name='IATA код'
    )
    name = models.CharField(
        max_length=70,
        null=True,
        blank=True,
        verbose_name='Имя'
    )

    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'

    def __str__(self):
        return f"{self.name}"