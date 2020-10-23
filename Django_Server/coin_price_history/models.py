from django.db import models
from coin_catalog.models import CoinStyle


class Platform(models.Model):
    """
    name - Holds the Name of Platform, such as eBay, Ay.By, etc.
    """
    name = models.CharField(max_length = 255, unique = True)

    class Meta:
        db_table = 'coin_history_platform'


class CoinPriceHistory(models.Model):
    """
    Holds the price History for individual CoinStyle

    platform - Reference to Platform Table
    u_id     - Unique Platform Purchase ID(item hash)
    date     - Purchase Date
    amount   - Purchase Price(in USD)
    """

    platform = models.ForeignKey(Platform, on_delete = models.CASCADE)
    u_id     = models.CharField(max_length = 255, blank = True)
    date     = models.DateTimeField(auto_now_add = True)
    amount   = models.FloatField()

    class Meta:
        unique_together = ['platform', 'date', 'amount']
        db_table = 'price_history'
