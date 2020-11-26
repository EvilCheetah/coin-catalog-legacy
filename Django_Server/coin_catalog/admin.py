from django.contrib import admin
from coin_catalog import models as CoinModel


class RegionAdmin(admin.ModelAdmin):
    list_display  = ['id', 'name']
    search_fields = ['name']


class CountryAdmin(admin.ModelAdmin):
    list_display  = ['id', 'region', 'name']
    search_fields = ['name']


class CategoryAdmin(admin.ModelAdmin):
    list_display  = ['id', 'region_name', 'country', 'name']
    search_fields = ['name']


class CollectionAdmin(admin.ModelAdmin):
    list_display  = ['id', 'region_name', 'country_name', 'category_name', 'name']
    search_fields = ['name']


class CurrencyAdmin(admin.ModelAdmin):
    list_display  = ['id', 'name']
    search_fields = ['name']


class CountryCurrencyAdmin(admin.ModelAdmin):
    list_display  = ['id', 'country', 'currency']


class MintedByAdmin(admin.ModelAdmin):
    list_display  = ['id', 'name']
    search_fields = ['name']


class DesignerNameAdmin(admin.ModelAdmin):
    list_display  = ['id', 'name']
    search_fields = ['name']


class SculptorNameAdmin(admin.ModelAdmin):
    list_display  = ['id', 'name']
    search_fields = ['name']


class MaterialAdmin(admin.ModelAdmin):
    list_display  = ['id', 'name']
    search_fields = ['name']


class QualityAdmin(admin.ModelAdmin):
    list_display  = ['id', 'name']
    search_fields = ['name']


class EdgeAdmin(admin.ModelAdmin):
    list_display  = ['id', 'name']
    search_fields = ['name']


class ShapeAdmin(admin.ModelAdmin):
    list_display  = ['id', 'name']
    search_fields = ['name']


class CoinFamilyAdmin(admin.ModelAdmin):
    list_display  = ['id', 'region_name', 'country_name', 'category_name', 'collection_name', 'name']
    search_fields = ['name']


class CoinStyleAdmin(admin.ModelAdmin):
    list_display  = ['id', 'country_name', 'coin_family_name', 'additional_name', 'year', 'minted_by',
                     'km_number', 'denomination',  'material', 'standard', 'quality']
    search_fields = ['additional_name']


class SubStyleAdmin(admin.ModelAdmin):
    list_display  = ['parent_coin', 'substyle_coin']


class NoteAdmin(admin.ModelAdmin):
    list_display  = ['coin_style', 'description']


class SideOfCoinAdmin(admin.ModelAdmin):
    list_display  = ['id', 'name']


class CoinDesignerAdmin(admin.ModelAdmin):
    list_display = ['id', 'coin_style', 'side', 'designer']


class CoinSculptorAdmin(admin.ModelAdmin):
    list_display = ['id', 'coin_style', 'side', 'sculptor']


class ImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'coin_style', 'side', 'image']


admin.site.register(CoinModel.Region,          RegionAdmin)
admin.site.register(CoinModel.Country,         CountryAdmin)
admin.site.register(CoinModel.Category,        CategoryAdmin)
admin.site.register(CoinModel.Collection,      CollectionAdmin)
admin.site.register(CoinModel.Currency,        CurrencyAdmin)
admin.site.register(CoinModel.CountryCurrency, CountryCurrencyAdmin)
admin.site.register(CoinModel.MintedBy,        MintedByAdmin)
admin.site.register(CoinModel.DesignerName,    DesignerNameAdmin)
admin.site.register(CoinModel.SculptorName,    SculptorNameAdmin)
admin.site.register(CoinModel.Material,        MaterialAdmin)
admin.site.register(CoinModel.Quality,         QualityAdmin)
admin.site.register(CoinModel.Edge,            EdgeAdmin)
admin.site.register(CoinModel.Shape,           ShapeAdmin)
admin.site.register(CoinModel.CoinFamily,      CoinFamilyAdmin)
admin.site.register(CoinModel.CoinStyle,       CoinStyleAdmin)
admin.site.register(CoinModel.Note,            NoteAdmin)
admin.site.register(CoinModel.SideOfCoin,      SideOfCoinAdmin)
admin.site.register(CoinModel.CoinDesigner,    CoinDesignerAdmin)
admin.site.register(CoinModel.CoinSculptor,    CoinSculptorAdmin)
admin.site.register(CoinModel.Image,           ImageAdmin)
