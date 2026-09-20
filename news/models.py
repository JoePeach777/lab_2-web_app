from django.db import models


class CurrencyRate(models.Model):
    currency_code = models.CharField(max_length=10, verbose_name="Код валюты")
    rate = models.DecimalField(max_digits=10, decimal_places=4, verbose_name="Курс")
    date = models.DateField(verbose_name="Дата")
    change_percent = models.FloatField(default=0.0, verbose_name="Изменение в %")

    def __str__(self):
        return f"{self.currency_code} — {self.rate} ({self.date})"