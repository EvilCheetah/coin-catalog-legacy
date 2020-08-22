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

    region = models.ForeignKey(Region, on_delete = models.CASCADE)
    name   = models.CharField(max_length = 100)

    class Meta():
        unique_together = ['region', 'name']


class Category(models.Model):
    """
    country - Reference to Country Table
    name    - Category Name, e.g. History and Culture, Myths and etc.
    """

    country = models.ForeignKey(Country, on_delete = models.CASCADE)
    name    = models.CharField(max_length = 255)

    class Meta():
        unique_together = ['country', 'name']


class Collection(models.Model):
    """
    category - Reference to Category Table
    name     - Collection (SubCategory), e.g. Saints, Greek Gods and etc.
    """

    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    name     = models.CharField(max_length = 255)

    class Meta():
        unique_together = ['category', 'name']


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

    collection = models.ForeignKey(Collection, on_delete = models.CASCADE)
    name       = models.CharField(max_length = 255)

    minted_by  = models.ForeignKey(MintedBy, on_delete = models.CASCADE,
                                   blank = True, default = "")
    author     = models.ForeignKey(Author,   on_delete = models.CASCADE,
                                   blank = True, default = "")
    sculptor   = models.ForeignKey(Sculptor, on_delete = models.CASCADE,
                                   blank = True, default = "")

    class Meta():
        unique_together = ['collection', 'name']


class CoinStyle(models.Model):
    """
    Holds the information of different styles of the coin with same names

    year             - Put into Circulation
    coin             - Reference to Coin Table
    shape            - Reference to Shape Table
    quality          - Reference to Quality Table
    edge             - Reference to Edge Table
    material         - Reference to Material Table
    standard         - Standard of the Material(Fineness), e.g. 925/1000, 999/1000 and etc.
    denomination     - Actual "Worth of Coin" in local currency
    mintage          - Amount of coins minted, e.g. 20k, 500 and etc.
    additional_name  - Additional Name(Postfix), e.g. 25 Years Anniversary and etc.
    km_number        - KM(Krause-Mishler) catalog number
    is_rare          - To indicate if coin can be viewed under a subscription mode.
    is_substyle      - To indicate that the coin is the Child(substyle) of different coin
    weight           - Weight of coin in Metric units
    length           - Length of coin in Metric units, always present
    width            - Width  of coin in Metric units, may be absent, e.g. Shape is Round
    notes            - Additional information about coin, e.g. coin is inlaid with smth,
                       pad-printing and etc.

    Uniqueness of coin identifies by:
        - Year
        - CoinID (Primary Name)
        - Material
        - Material Standard
        - Denomination
        - Shape
        - Quality
        - SubStyle State
        - KM Number
        - Additional Name
    """

    year            = models.IntegerField()
    coin            = models.ForeignKey(Coin,     on_delete = models.CASCADE)
    shape           = models.ForeignKey(Shape,    on_delete = models.CASCADE)
    quality         = models.ForeignKey(Quality,  on_delete = models.CASCADE)
    edge            = models.ForeignKey(Edge,     on_delete = models.CASCADE)
    material        = models.ForeignKey(Material, on_delete = models.CASCADE)
    standard        = models.CharField(max_length = 30, blank = True, default = "")
    denomination    = models.CharField(max_length = 255)
    mintage         = models.IntegerField()

    additional_name = models.CharField(max_length = 255, blank = True, default = "")
    km_number       = models.CharField(max_length = 255, blank = True, default = "")

    is_rare         = models.BooleanField()
    is_substyle     = models.BooleanField()

    weight          = models.FloatField()
    length          = models.FloatField()
    width           = models.FloatField()

    class Meta():
        unique_together = ['year',         'coin',
                           'shape',        'quality',
                           'material',     'standard',
                           'denomination', 'is_substyle',
                           'km_number',    'additional_name']


class SubStyle(models.Model):
    """
    Used to map the Sub-Styles of the coins to their parents.

    parent_coin   - Points to the initial(parent) style of the coin
    substyle_coin - Points to the coin substyle
    """

    parent_coin   = models.ForeignKey(CoinStyle, on_delete = models.CASCADE,
                                      related_name = "coin_base_edition")
    substyle_coin = models.ForeignKey(CoinStyle, on_delete = models.CASCADE,
                                      related_name = "coin_special_edition")


    class Meta():
        unique_together = ['parent_coin', 'substyle_coin']


class Note(models.Model):
    """
    Holds the notes about coin. Makes possible to return the notes in array

    coin_style  - Reference to CoinStyle Table
    description - Holds the key points about design of coin, e.g. it has pad-printing,
                  inlaid with something and etc.
    """

    coin_style  = models.ForeignKey(CoinStyle, on_delete = models.CASCADE)
    description = models.CharField(max_length = 255)

    class Meta():
        unique_together = ['coin_style', 'description']


##------------------Visual Information------------------##
class SideOfCoin(models.Model):
    """
    Holds the name of side for Image Table

    name - name of side, e.g. Front(Obverse), Back(Reverse), Edge and etc.
    """

    name = models.CharField(max_length = 255, unique = True)


class Image(models.Model):
    """
    Holds the path to the coin images

    side       - Reference to SideOfCoin
    coin_style - Reference to CoinStyle Table
    path       - Path to image
    """

    side       = models.ForeignKey(SideOfCoin, on_delete = models.CASCADE)
    coin_style = models.ForeignKey(CoinStyle,  on_delete = models.CASCADE)
    path       = models.CharField(max_length = 255)

    class Meta():
        unique_together = ['side', 'coin_style', 'path']
