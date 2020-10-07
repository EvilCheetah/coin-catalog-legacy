from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('region',        views.RegionViewSet)
router.register('country',       views.CountryViewSet)
router.register('category',      views.CategoryViewSet)
router.register('collection',    views.CollectionViewSet)
router.register('currency',      views.CurrencyViewSet)
router.register('minted_by',     views.MintedByViewSet)
router.register('author_name',   views.AuthorNameViewSet)
router.register('sculptor_name', views.SculptorNameViewSet)
router.register('material',      views.MaterialViewSet)
router.register('quality',       views.QualityViewSet)
router.register('edge',          views.EdgeViewSet)
router.register('shape',         views.ShapeViewSet)
router.register('coin_family',   views.CoinFamilyViewSet)
router.register('coin_style',    views.CoinStyleViewSet)
router.register('sub_style',     views.SubStyleViewSet)
router.register('note',          views.NoteViewSet)
router.register('side_of_coin',  views.SideOfCoinViewSet)
router.register('coin_author',   views.CoinAuthorViewSet)
router.register('coin_sculptor', views.CoinSculptorViewSet)
router.register('image',         views.ImageViewSet)


urlpatterns = [
    path('', include(router.urls))
]
