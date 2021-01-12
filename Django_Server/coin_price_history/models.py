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


class Grade(models.Model):
    """
        name         - Holds the Full Name of the Grade, e.g. 'Mint State', 'Proof', 'Choice About Uncirculated' and etc.
        abbreviation - Holds the shortened name of the grade, e.g. 'MS70', 'PR-63'
    """
    name         = models.CharField(max_length = 100)
    abbreviation = models.CharField(max_length = 20, unique = True)

    class Meta:
        db_table        = 'coin_history_grade'


class CoinPriceHistory(models.Model):
    """
        Holds the price History for individual CoinStyle

        coin_style      - Reference to CoinStyle Table(located in coin_catalog)
        platform        - Reference to Platform Table
        grade           - Reference to Grade Table
        purchase_id     - Unique Platform Purchase ID(item hash)
        date            - Purchase Date
        purchase_price  - Purchase Price(in USD)
    """

    coin_style      = models.ForeignKey(CoinStyle, on_delete = models.CASCADE)
    platform        = models.ForeignKey(Platform,  on_delete = models.CASCADE)
    grade           = models.ForeignKey(Grade,     on_delete = models.CASCADE)
    purchase_id     = models.CharField(max_length = 255, blank = True)
    date            = models.DateTimeField(default = timezone.now)
    purchase_price  = models.DecimalField(max_digits = 20, decimal_places = 2)

    class Meta:
        db_table        = 'coin_price_history'
        unique_together = ['coin_style', 'platform', 'date', 'purchase_price']
