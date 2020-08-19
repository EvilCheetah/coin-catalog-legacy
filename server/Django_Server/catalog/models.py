from django.db import models


##------------------Fundamental Information------------------##
class Region(models.Model):
    """
    name - Region Name, e.g. Europe, North America and etc.
    """

    name = models.CharField(max_length = 20, unique = True)


class Country(models.Model):
    """
    region - Reference to Region Table
    name   - Country Name, e.g. UK, Russia, USA
    """

    region = models.ForeignKey(Region, on_delete = models.CASCADE, unique = True)
    name   = models.CharField(max_length = 100, unique = True)


class Category(models.Model):
    """
    country - Reference to Country Table
    name    - Category Name, e.g. History and Culture, Myths and etc.
    """

    country = models.ForeignKey(Country, on_delete = models.CASCADE, unique = True)
    name    = models.CharField(max_length = 255, unique = True)


class Collection(models.Model):
    """
    category - Reference to Category Table
    name     - Collection (SubCategory), e.g. Saints, Greek Gods and etc.
    """

    category = models.ForeignKey(Category, on_delete = models.CASCADE, unique = True)
    name     = models.CharField(max_length = 255, unique = True)


##------------------MintedBy Information------------------##
class MintedBy(models.Model):
    """
    name - Name of Mint(Origin)
    """

    name = models.CharField(max_length = 255, unique = True)


class Author(models.Model):
    """
    name - Name of Author or Designer of Coin
    """

    name = models.CharField(max_length = 255, unique = True)


class Sculptor(models.Model):
    """
    name - Name of Sculptor or 3D Designer of Coin
    """

    name = models.CharField(max_length = 255, unique = True)



##----------------Base Information----------------##
class Material(models.Model):
    """
    name - Name of Material, e.g. Gold, Silver, Cooper-Nickel and etc.
    """

    name = models.CharField(max_length = 255, unique = True)


class Quality(models.Model):
    """
    name - Name of Quality, e.g. Brilliant–Uncirculated, Proof, Uncirculated and etc.
    """

    name = models.CharField(max_length = 255, unique = True)


class Edge(models.Model):
    """
    name - Style of edge, e.g. reeded, corrugated and etc.
    """

    name = models.CharField(max_length = 255, unique = True)


##-----------Characteristics Information-----------##
class Shape(models.Model):
    """
    name - Name of Shape, e.g. Round, Square, Oval and etc.
    """

    name = models.CharField(max_length = 255, unique = True)


##---------------Coin Information---------------##
class Coin(models.Model):
    """
    Holds base information about the single coin

    collection - Reference to Collection Table
    name       - Name of Coin or set of coins, e.g. Porthos, Mercury, Libra and etc.
    mintedBy   - Reference to MintedBy Table
    authorID   - Reference to Author   Table
    sculptor   - Reference to Sculptor Table
    """

    collection = models.ForeignKey(Collection, on_delete = models.CASCADE, unique = True)
    name       = models.CharField(max_length = 255, unique = True)

    minted_by   = models.ForeignKey(MintedBy, on_delete = models.CASCADE)
    author      = models.ForeignKey(Author,   on_delete = models.CASCADE)
    sculptor    = models.ForeignKey(Sculptor, on_delete = models.CASCADE)


class CoinInformation(models.Model):
    """
    Holds the information of different styles of the coin with same names


    coin         - Reference to Coin Table
    year         - Put into Circulation
    material     - Reference to Material Table
    standard     - Standard of the Material(Fineness), e.g. 925/1000, 999/1000 and etc.
    mintage      - Amount of coins minted, e.g. 20k, 500 and etc.
    quality      - Reference to Quality Table
    denomination - Actual "Worth of Coin" in local currency
    """

    coin         = models.ForeignKey(Coin,     on_delete = models.CASCADE, unique = True)
    year         = models.IntegerField(unique = True)
    shape        = models.ForeignKey(Shape,    on_delete = models.CASCADE, unique = True)
    material     = models.ForeignKey(Material, on_delete = models.CASCADE, unique = True)
    standard     = models.CharField(max_length = 30, unique = True)
    mintage      = models.IntegerField()
    quality      = models.ForeignKey(Quality,  on_delete = models.CASCADE)
    denomination = models.CharField(max_length = 255, unique = True)


class CoinStyle(models.Model):
    """
    Holds the information of a signle coin style.
    If there are multiple SubStyles in the CoinStyle, this table will take care of it

    coin_style       - Reference to CoinStyle Table
    name             - Additional Name(Postfix), e.g. 25 Years Anniversary and etc.
    weight           - Weight of coin in Metric units
    length           - Length of coin in Metric units, always present
    width            - Width  of coin in Metric units, may be absent, e.g. Shape is Round
    notes            - Additional information about coin, e.g. coin is inlaid with smth, pad-printing and etc.
    """
    coin_information = models.ForeignKey(CoinInformation, on_delete = models.CASCADE, unique = True)
    name             = models.CharField(max_length = 255, unique = True)

    weight           = models.FloatField()

    length           = models.FloatField()
    width            = models.FloatField(

    notes            = models.TextField()


class Image(models.Model):
    """
    Holds the path to the coin images

    coin_style - Reference to CoinStyle Table
    path       - Path to image
    """

    coin_style = models.ForeignKey(CoinInformation, on_delete = models.CASCADE, unique = True)
    paths      = models.CharField(max_length = 255, unique = True)
