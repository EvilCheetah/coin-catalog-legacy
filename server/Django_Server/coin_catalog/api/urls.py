from django.urls import path, include
from . import views
from rest_framework import routers


router  = routers.DefaultRouter()

#Model View Sets for Angular
#Pure Models
router.register('region',           views.RegionViewSet,            basename = 'region-model')
router.register('country',          views.CountryViewSet,           basename = 'coutry-model')
router.register('category',         views.CategoryViewSet,          basename = 'category-model')
router.register('collection',       views.CollectionViewSet,        basename = 'collection-model')
router.register('currency',         views.CurrencyViewSet,          basename = 'currency-model')
router.register('country_currency', views.CountryCurrencyViewSet,   basename = 'country_currency-model')
router.register('minted_by',        views.MintedByViewSet,          basename = 'minted_by-model')
router.register('author_name',      views.AuthorNameViewSet,        basename = 'author_name-model')
router.register('sculptor_name',    views.SculptorNameViewSet,      basename = 'sculptor_name-model')
router.register('material',         views.MaterialViewSet,          basename = 'material-model')
router.register('quality',          views.QualityViewSet,           basename = 'quality-model')
router.register('edge',             views.EdgeViewSet,              basename = 'edge-model')
router.register('shape',            views.ShapeViewSet,             basename = 'shape-model')
router.register('coin_family',      views.CoinFamilyViewSet,        basename = 'coin_family-model')
router.register('coin_style',       views.CoinStyleViewSet,         basename = 'coin_style-model')
router.register('sub_style',        views.SubStyleViewSet,          basename = 'sub_style-model')
router.register('note',             views.NoteViewSet,              basename = 'note-model')
router.register('side_of_coin',     views.SideOfCoinViewSet,        basename = 'side_of_coin-model')
router.register('coin_author',      views.CoinAuthorViewSet,        basename = 'coin_author-model')
router.register('coin_sculptor',    views.CoinSculptorViewSet,      basename = 'coin_sculptor-model')
router.register('image',            views.ImageViewSet,             basename = 'image-model')

#Human-Readable Substyle View Set
#Preformatted with Text
router.register('coin',             views.CoinViewSet,              basename = 'coin-full-detail')

urlpatterns = [
    path('', include(router.urls)),
]
