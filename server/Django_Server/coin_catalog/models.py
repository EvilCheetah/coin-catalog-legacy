from django.db import models


##------------------Fundamental Information------------------##
class Region(models.Model):
    """
    name - Region Name, e.g. Europe, North America and etc.
    """

    name = models.CharField(max_length = 20, unique = True)

    class Meta():
        db_table = 'coin_region'

    def __str__(self):
        return self.name


class Country(models.Model):
    """
    region - Reference to Region Table
    name   - Country Name, e.g. UK, Russia, USA
    """

    region = models.ForeignKey(Region, related_name = 'countries', on_delete = models.CASCADE)
    name   = models.CharField(max_length = 100)

    class Meta():
        unique_together = ['region', 'name']
        ordering        = ['region', 'name']
        db_table        = 'coin_country'

    def __str__(self):
        return self.name


class Category(models.Model):
    """
    country - Reference to Country Table
    name    - Category Name, e.g. History and Culture, Myths and etc.
    """

    country = models.ForeignKey(Country, related_name = 'categories', on_delete = models.CASCADE)
    name    = models.CharField(max_length = 255)

    class Meta():
        unique_together = ['country', 'name']
        ordering        = ['country', 'name']
        db_table        = 'coin_category'

    def __str__(self):
        return (self.country.name + ' > ' + self.name)


class Collection(models.Model):
    """
    category - Reference to Category Table
    name     - Collection (SubCategory), e.g. Saints, Greek Gods and etc.
    """

    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    name     = models.CharField(max_length = 255)

    class Meta():
        unique_together = ['category', 'name']
        ordering        = ['category', 'name']
        db_table        = 'coin_collection'

    def __str__(self):
        return (self.category.name + ' > ' + self.name)


##------------------MintedBy Information------------------##
class MintedBy(models.Model):
    """
    name - Name of Mint(Origin)
    """

    name = models.CharField(max_length = 255, unique = True)

    class Meta():
        db_table = 'coin_minted_by'

    def __str__(self):
        return self.name


class AuthorName(models.Model):
    """
    name - Single name of Author or Designer of Coin
    """

    name = models.CharField(max_length = 255, unique = True)

    class Meta():
        db_table = 'coin_author_name'

    def __str__(self):
        return self.name


class SculptorName(models.Model):
    """
    name - Single name of Sculptor or 3D Designer of Coin
    """

    name = models.CharField(max_length = 255, unique = True)

    class Meta():
        db_table = 'coin_sculptor_name'

    def __str__(self):
        return self.name



##----------------Base Information----------------##
class Material(models.Model):
    """
    name - Name of Material, e.g. Gold, Silver, Cooper-Nickel and etc.
    """

    name = models.CharField(max_length = 255, unique = True)

    class Meta():
        db_table = 'coin_material'

    def __str__(self):
        return self.name


class Quality(models.Model):
    """
    name - Name of Quality, e.g. Brilliant–Uncirculated, Proof, Uncirculated and etc.
    """

    name = models.CharField(max_length = 255, unique = True)

    class Meta():
        db_table = 'coin_quality'

    def __str__(self):
        return self.name


class Edge(models.Model):
    """
    name - Style of edge, e.g. reeded, corrugated and etc.
    """

    name = models.CharField(max_length = 255, unique = True)

    class Meta():
        db_table = 'coin_edge'

    def __str__(self):
        return self.name


##-----------Characteristics Information-----------##
class Shape(models.Model):
    """
    name - Name of Shape, e.g. Round, Square, Oval and etc.
    """

    name = models.CharField(max_length = 255, unique = True)

    class Meta():
        db_table = 'coin_shape'

    def __str__(self):
        return self.name


##---------------Coin Information---------------##
class CoinFamily(models.Model):
    """
    Holds base information about the single coin or family of coins
    that have the same name, but differs in material, mintage, quality and etc.

    collection - Reference to Collection Table
    name       - Name of Coin or set of coins, e.g. Porthos, Mercury, Libra and etc.
    mintedBy   - Reference to MintedBy Table
    """

    collection = models.ForeignKey(Collection, on_delete = models.CASCADE)
    name       = models.CharField(max_length = 255)
    minted_by  = models.ForeignKey(MintedBy, on_delete = models.CASCADE,
                                   blank = True, default = "")


    class Meta():
        unique_together = ['collection', 'name']
        ordering        = ['collection', 'name', 'minted_by']
        db_table        = 'coin_family'

    def __str__(self):
        return (self.collection.category.country.name + ' > ' + self.name)


class CoinStyle(models.Model):
    """
    Holds the information of different styles of the coin with same names

    year             - Put into Circulation
    coin_family      - Reference to Coin Table
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
        - CoinFamilyID (Primary Name)
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
    coin_family     = models.ForeignKey(CoinFamily, on_delete = models.CASCADE)
    shape           = models.ForeignKey(Shape,      on_delete = models.CASCADE)
    quality         = models.ForeignKey(Quality,    on_delete = models.CASCADE)
    edge            = models.ForeignKey(Edge,       on_delete = models.CASCADE)
    material        = models.ForeignKey(Material,   on_delete = models.CASCADE)
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
        unique_together = ['year',         'coin_family',
                           'shape',        'quality',
                           'material',     'standard',
                           'denomination', 'is_substyle',
                           'km_number',    'additional_name']
        ordering        = ['year', 'coin_family', 'material', 'standard']
        db_table        = 'coin_style'

    def __str__(self):
        return (self.year + self.coin_family.name + self.material.name + self.standard)


class SubStyle(models.Model):
    """
    Used to map the Sub-Styles of the coins to their parents.

    substyle_coin - Points to the coin substyle, can be only one, acts
                    as Primary Key
    parent_coin   - Points to the initial(parent) style of the coin
    """

    substyle_coin = models.OneToOneField(CoinStyle, on_delete = models.CASCADE,
                                         related_name = "coin_special_edition",
                                         primary_key  = True)

    parent_coin   = models.ForeignKey(CoinStyle, on_delete = models.CASCADE,
                                      related_name = "coin_base_edition")

    class Meta():
        unique_together = ['parent_coin', 'substyle_coin']
        db_table        = 'coin_style_connector'


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
        db_table        = 'coin_note'


##------------------Visual Information------------------##
class SideOfCoin(models.Model):
    """
    Holds the name of side for Image Table
    name - name of side, e.g. Front(Obverse), Back(Reverse), Edge and etc.
    """

    name = models.CharField(max_length = 255, unique = True)

    class Meta():
        db_table = 'coin_side'


class CoinAuthor(models.Model):
    """
    Holds the name of author or a list of authors of a single coin(family of coins)

    coin_family - Reference to Coin Table
    author      - Reference to AuthorName Table
    side        - Reference to SideOfCoin Table
    """

    coin_family = models.ForeignKey(CoinFamily, on_delete = models.CASCADE)
    author      = models.ForeignKey(AuthorName, on_delete = models.CASCADE)
    side        = models.ForeignKey(SideOfCoin, on_delete = models.CASCADE)

    class Meta():
        unique_together = ['coin_family', 'author', 'side']
        ordering        = ['coin_family', 'side', 'author']
        db_table        = 'coin_authors'


class CoinSculptor(models.Model):
    """
    Holds the name of sculptor or a list of sculptors of a single coin(family of coins)

    coin_family - Reference to Coin Table
    sculptor    - Reference to SculptorName Table
    side        - Reference to SideOfCoin Table
    """

    coin_family = models.ForeignKey(CoinFamily,   on_delete = models.CASCADE)
    sculptor    = models.ForeignKey(SculptorName, on_delete = models.CASCADE)
    side        = models.ForeignKey(SideOfCoin,   on_delete = models.CASCADE)

    class Meta():
        unique_together = ['coin_family', 'sculptor', 'side']
        ordering        = ['coin_family', 'side', 'sculptor']
        db_table        = 'coin_sculptors'


class Image(models.Model):
    """
    Holds the path to the coin images

    coin_style - Reference to CoinStyle Table
    side       - Reference to SideOfCoin
    path       - Path to image
    """

    coin_style = models.ForeignKey(CoinStyle,  on_delete = models.CASCADE)
    side       = models.ForeignKey(SideOfCoin, on_delete = models.CASCADE)
    path       = models.CharField(max_length = 255)

    class Meta():
        unique_together = ['coin_style', 'side', 'path']
        ordering        = ['coin_style', 'side', 'path']
        db_table        = 'coin_image'
