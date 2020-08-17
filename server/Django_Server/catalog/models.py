from django.db import models

#COMES FROM scrapper/scraperHandler.py


##------------------Fundamental Information------------------##
class Region(models.Model):
    name = models.CharField(max_length = 20, unique = True)


class Country(models.Model):
    region = models.ForeignKey(Region, on_delete = models.CASCADE, unique = True)
    name   = models.CharField(max_length = 100, unique = True)


class Category(models.Model):
    country = models.ForeignKey(Country, on_delete = models.CASCADE, unique = True)
    name    = models.CharField(max_length = 255, unique = True)


class Collection(models.Model):
    category = models.ForeignKey(Category, on_delete = models.CASCADE, unique = True)
    name     = models.CharField(max_length = 255, unique = True)



##------------------MintedBy Information------------------##
class MintedBy(models.Model):
    name = models.CharField(max_length = 255, unique = True)


class Author(models.Model):
    name = models.CharField(max_length = 255, unique = True)


class Sculptor(models.Model):
    name = models.CharField(max_length = 255, unique = True)



##----------------Base Information----------------##
class Material(models.Model):
    name = models.CharField(max_length = 255, unique = True)


class Quality(models.Model):
    name = models.CharField(max_length = 255, unique = True)



##-----------Characteristics Information-----------##
class Shape(models.Model):
    name = models.CharField(max_length = 255, unique = True)


class SizeUnits(models.Model):
    name = models.CharField(max_length = 255, unique = True)


class WeightUnits(models.Model):
    name = models.CharField(max_length = 255, unique = True)


##---------------Coin Information---------------##
class Coin(models.Model):
    collection = models.ForeignKey(Collection, on_delete = models.CASCADE, unique = True)
    name       = models.CharField(max_length = 255, unique = True)
    year       = models.IntegerField()

    mintedBy   = models.ForeignKey(MintedBy, on_delete = models.SET_NULL)


class CoinStyles(models.Model):
    coin     = models.ForeignKey(Coin, on_delete = models.CASCADE, unique = True)
    material = models.ForeignKey(Material, on_delete = models.SET_NULL, unique = True)
    standard = models.CharField(max_length = 30, unique = True)
