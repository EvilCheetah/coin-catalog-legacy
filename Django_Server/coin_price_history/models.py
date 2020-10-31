from django.db import models
from django.utils import timezone
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

    coin_style  - Reference to CoinStyle Table(located in coin_catalog)
    platform    - Reference to Platform Table
    purchase_id - Unique Platform Purchase ID(item hash)
    date        - Purchase Date
    amount      - Purchase Price(in USD)
    """

    coin_style  = models.ForeignKey(CoinStyle, on_delete = models.CASCADE)
    platform    = models.ForeignKey(Platform,  on_delete = models.CASCADE)
    purchase_id = models.CharField(max_length = 255, blank = True)
    date        = models.DateTimeField(default = timezone.now)
    amount      = models.DecimalField(max_digits = 20, decimal_places = 2)

    class Meta:
        unique_together = ['coin_style', 'platform', 'date', 'amount']
        db_table = 'coin_price_history'
