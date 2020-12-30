from django.db import models


##------------------Fundamental Information------------------##
class Region(models.Model):
    """
    name - Region Name, e.g. Europe, North America and etc.
    """

    name = models.CharField(max_length = 20)

    class Meta:
        db_table            = 'coin_region'
        unique_together     = ['name']
        verbose_name_plural = 'Regions'

    def __str__(self):
        return self.name


class Country(models.Model):
    """
    region - Reference to Region Table
    name   - Country Name, e.g. UK, Russia, USA
    """

    region = models.ForeignKey(Region, related_name = 'country_list', on_delete = models.CASCADE)
    name   = models.CharField(max_length = 100)

    class Meta:
        db_table            = 'coin_country'
        unique_together     = ['region', 'name']
        verbose_name_plural = 'Countries'

    def __str__(self):
        return self.name

    @property
    def region_name(self):
        return self.region.name


class Category(models.Model):
    """
    country - Reference to Country Table
    name    - Category Name, e.g. History and Culture, Myths and etc.

    Note:
        - '@property' attributes are created for AdminPanel
    """

    country = models.ForeignKey(Country, related_name = 'category_list', on_delete = models.CASCADE)
    name    = models.CharField(max_length = 255)

    class Meta:
        db_table            = 'coin_category'
        unique_together     = ['country', 'name']
        verbose_name_plural = 'Categories'

    def __str__(self):
        return (self.country.name + ' > ' + self.name)

    @property
    def region_name(self):
        return self.country.region_name

    @property
    def country_name(self):
        return self.country.name


class Collection(models.Model):
    """
    category - Reference to Category Table
    name     - Collection (SubCategory), e.g. Saints, Greek Gods and etc.

    Note:
        - '@property' attributes are created for AdminPanel
    """

    category = models.ForeignKey(Category, related_name = 'collection_list', on_delete = models.CASCADE)
    name     = models.CharField(max_length = 255)

    class Meta:
        db_table            = 'coin_collection'
        unique_together     = ['category', 'name']
        verbose_name_plural = 'Collections'

    def __str__(self):
        return (self.category.name + ' > ' + self.name)

    @property
    def region_name(self):
        return self.category.region_name

    @property
    def country_name(self):
        return self.category.country_name

    @property
    def category_name(self):
        return self.category.name


##---------------Currency Information---------------##
class Currency(models.Model):
    """
    name - Name of the Currency
    """

    name = models.CharField(max_length = 255)

    class Meta:
        db_table            = 'coin_currrency'
        unique_together     = ['name']
        verbose_name_plural = 'Currencies'

    def __str__(self):
        return self.name


class CountryCurrency(models.Model):
    """
    country  - Reference to Country Table
    currency - Reference to Currency Table
    """

    country  = models.ForeignKey(Country,  on_delete = models.CASCADE)
    currency = models.ForeignKey(Currency, on_delete = models.CASCADE)

    class Meta:
        db_table            = 'coin_country_currency_connector'
        unique_together     = ['country', 'currency']
        verbose_name_plural = 'Country-Currencies'

    def __str__(self):
        return (self.country.name + ': ' + self.currency.name)

    @property
    def currency_name(self):
        return self.currency.name


##------------------MintedBy Information------------------##
class MintedBy(models.Model):
    """
    name - Name of Mint(Origin)
    """

    name = models.CharField(max_length = 255)

    class Meta:
        db_table            = 'coin_minted_by'
        unique_together     = ['name']
        verbose_name_plural = 'Minted By'

    def __str__(self):
        return self.name


class DesignerName(models.Model):
    """
    name - Single name of Author or Designer of Coin
    """

    name = models.CharField(max_length = 255)

    class Meta:
        db_table            = 'coin_designer_name'
        unique_together     = ['name']
        verbose_name_plural = 'Designers\' Name'

    def __str__(self):
        return self.name


class SculptorName(models.Model):
    """
    name - Single name of Sculptor or 3D Designer of Coin
    """

    name = models.CharField(max_length = 255)

    class Meta:
        db_table            = 'coin_sculptor_name'
        unique_together     = ['name']
        verbose_name_plural = 'Sculptors\' Name'

    def __str__(self):
        return self.name


##----------------Base Information----------------##
class Material(models.Model):
    """
    name - Name of Material, e.g. Gold, Silver, Copper-Nickel and etc.
    """

    name = models.CharField(max_length = 255)

    class Meta:
        db_table            = 'coin_material'
        unique_together     = ['name']
        verbose_name_plural = 'Materials'

    def __str__(self):
        return self.name


class Quality(models.Model):
    """
    name - Name of Quality, e.g. Brilliant–Uncirculated, Proof, Uncirculated and etc.
    """

    name = models.CharField(max_length = 255)

    class Meta:
        db_table            = 'coin_quality'
        unique_together     = ['name']
        verbose_name_plural = 'Qualities'

    def __str__(self):
        return self.name


class Edge(models.Model):
    """
    name - Style of edge, e.g. reeded, corrugated and etc.
    """

    name = models.CharField(max_length = 255)

    class Meta:
        db_table            = 'coin_edge'
        unique_together     = ['name']
        verbose_name_plural = 'Edge Styles'

    def __str__(self):
        return self.name


##-----------Characteristics Information-----------##
class Shape(models.Model):
    """
    name - Name of Shape, e.g. Round, Square, Oval and etc.
    """

    name = models.CharField(max_length = 255)

    class Meta:
        db_table            = 'coin_shape'
        unique_together     = ['name']
        verbose_name_plural = 'Shapes'

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

    Note:
        - '@property' attributes are created for AdminPanel
    """

    collection = models.ForeignKey(Collection, related_name = 'coin_family_list', on_delete = models.CASCADE)
    name       = models.CharField(max_length = 255)

    class Meta:
        db_table            = 'coin_family'
        unique_together     = ['collection', 'name']
        verbose_name_plural = 'Coin Families'

    def __str__(self):
        return self.name

    @property
    def region_name(self):
        return self.collection.region_name

    @property
    def country_name(self):
        return self.collection.country_name

    @property
    def category_name(self):
        return self.collection.category_name

    @property
    def collection_name(self):
        return self.collection.name


class CoinStyle(models.Model):
    """
    Holds the information of different styles of the coin with same names

    coin_family           - Reference to CoinFamily Table
    additional_name       - Additional Name(Postfix), e.g. 25 Years Anniversary and etc.
    minted_by             - Reference to MintedBy Table
    year                  - Put into Circulation
    denomination_value    - Value of "Worth of Coin" in local currency
    denomination_currency - Reference to CountryCurrency Table, Actutual Name of Currency
    shape                 - Reference to Shape Table
    quality               - Reference to Quality Table
    edge                  - Reference to Edge Table
    material              - Reference to Material Table
    standard              - Standard of the Material(Fineness), e.g. 925/1000, 999/1000 and etc.
    mintage               - Amount of coins minted, e.g. 20k, 500 and etc.
    km_number             - KM(Krause-Mishler) catalog number
    is_rare               - To indicate if coin can be viewed under a subscription mode.
    is_substyle           - To indicate that the coin is the Child(substyle) of different coin
    weight                - Weight(in grams) of coin in Metric units
    length                - Length(in mm)    of coin in Metric units, always present
    width                 - Width(in mm)     of coin in Metric units, may be absent, e.g. Shape is Round
    thickness             - Thickness(in mm) of coin in Metric units, may be absent,
    notes                 - Additional information about coin, e.g. coin is inlaid with smth,
                            pad-printing and etc.

    Uniqueness of coin identifies by:
        - Year
        - CoinFamilyID (Primary Name)
        - Material
        - Material Standard
        - Denomination Value
        - Denomination Currency
        - Shape
        - Quality
        - SubStyle State
        - KM Number
        - Additional Name

    Notes:
        - Minted_By may differ from CoinStyle to CoinStyle (ex. https://bit.ly/3m8hlFX)
        - '@property' attributes are created for AdminPanel
    """

    coin_family           = models.ForeignKey(CoinFamily, related_name = 'coin_style_list', on_delete = models.CASCADE)
    additional_name       = models.CharField(max_length = 255, blank = True, default = "")
    minted_by             = models.ForeignKey(MintedBy, on_delete = models.CASCADE,
                                              blank = True, default = "")

    year                  = models.IntegerField()
    denomination_value    = models.FloatField()
    denomination_currency = models.ForeignKey(CountryCurrency, on_delete = models.CASCADE)
    shape                 = models.ForeignKey(Shape,           on_delete = models.CASCADE)
    quality               = models.ForeignKey(Quality,         on_delete = models.CASCADE)
    edge                  = models.ForeignKey(Edge,            on_delete = models.CASCADE)
    material              = models.ForeignKey(Material,        on_delete = models.CASCADE)
    standard              = models.DecimalField(max_digits = 5, decimal_places = 2)
    mintage               = models.IntegerField()

    km_number             = models.CharField(max_length = 255, blank = True, default = "")

    is_substyle           = models.BooleanField(default = False)

    weight                = models.DecimalField(max_digits = 11, decimal_places = 2)
    length                = models.DecimalField(max_digits = 11, decimal_places = 2)
    width                 = models.DecimalField(max_digits = 11, decimal_places = 2)
    thickness             = models.DecimalField(max_digits = 11, decimal_places = 2)

    class Meta:
        db_table            = 'coin_style'
        unique_together     = ['coin_family', 'additional_name',
                               'year',
                               'denomination_value', 'denomination_currency',
                               'shape',        'quality',
                               'material',     'standard',
                               'is_substyle',  'km_number']
        verbose_name_plural = 'Coin Styles'

    def __str__(self):
        return (str(self.year) + ' ' +
                str(self.coin_family.name) + ' - ' +
                str(self.additional_name) + ' - ' +
                str(self.material.name) + ' ' +
                str(self.standard))

    @property
    def region_name(self):
        return self.coin_family.region_name

    @property
    def country_name(self):
        return self.coin_family.country_name

    @property
    def category_name(self):
        return self.coin_family.category_name

    @property
    def collection_name(self):
        return self.coin_family.collection_name

    @property
    def coin_family_name(self):
        return self.coin_family.name

    @property
    def denomination(self):
        return (str(self.denomination_value) + ' ' + self.denomination_currency.currency_name)


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

    class Meta:
        db_table            = 'coin_style_connector'
        unique_together     = ['parent_coin', 'substyle_coin']
        verbose_name_plural = 'Coin SubStyle Connectors'


class Note(models.Model):
    """
    Holds the notes about coin. Makes possible to return the notes in array

    coin_style  - Reference to CoinStyle Table
    description - Holds the key points about design of coin, e.g. it has pad-printing,
                  inlaid with something and etc.
    """

    coin_style  = models.ForeignKey(CoinStyle, on_delete = models.CASCADE)
    description = models.CharField(max_length = 255)

    class Meta:
        db_table            = 'coin_note'
        unique_together     = ['coin_style', 'description']
        verbose_name_plural = 'Notes'


##------------------Visual Information------------------##
class SideOfCoin(models.Model):
    """
    Holds the name of side for Images, Designers and Sculptors
    name - name of side, e.g. Front(Obverse), Back(Reverse), Edge and etc.
    """

    name = models.CharField(max_length = 255)

    class Meta:
        db_table            = 'coin_side'
        unique_together     = ['name']
        verbose_name_plural = 'Coin Sides'

    def __str__(self):
        return self.name


class CoinDesigner(models.Model):
    """
    Holds the name of author or a list of authors of a single coin(family of coins)

    coin_style - Reference to CoinStyle Table
    side       - Reference to SideOfCoin Table
    designer   - Reference to DesignerName Table

    Note:
        - Designers in single CoinFamily may differ from CoinStyle
          to CoinStyle, used CoinStyle instead of CoinFamily
    """

    coin_style = models.ForeignKey(CoinStyle,    on_delete = models.CASCADE)
    side       = models.ForeignKey(SideOfCoin,   on_delete = models.CASCADE)
    designer   = models.ForeignKey(DesignerName, on_delete = models.CASCADE)

    class Meta:
        db_table            = 'coin_designers'
        unique_together     = ['coin_style', 'designer', 'side']
        verbose_name_plural = 'Coin Style Designers'


class CoinSculptor(models.Model):
    """
    Holds the name of sculptor or a list of sculptors of a single coin(family of coins)

    coin_style - Reference to CoinStyle
    side       - Reference to SideOfCoin Table
    sculptor   - Reference to SculptorName Table

    Note:
        - Sculptors in single CoinFamily may differ from CoinStyle
          to CoinStyle, used CoinStyle instead of CoinFamily
    """

    coin_style = models.ForeignKey(CoinStyle,    on_delete = models.CASCADE)
    side       = models.ForeignKey(SideOfCoin,   on_delete = models.CASCADE)
    sculptor   = models.ForeignKey(SculptorName, on_delete = models.CASCADE)

    class Meta:
        db_table            = 'coin_sculptors'
        unique_together     = ['coin_style', 'sculptor', 'side']
        verbose_name_plural = 'Coin Style Sulptors'


class Image(models.Model):
    """
    Holds the path to the coin images

    coin_style - Reference to CoinStyle Table
    side       - Reference to SideOfCoin
    image       - Path to image
    """

    coin_style = models.ForeignKey(CoinStyle,  on_delete = models.CASCADE)
    side       = models.ForeignKey(SideOfCoin, on_delete = models.CASCADE)
    image      = models.ImageField(upload_to = 'coin_images/')

    class Meta:
        db_table            = 'coin_image'
        unique_together     = ['coin_style', 'side', 'image']
        verbose_name_plural = 'Images'
