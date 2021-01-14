from rest_framework import status

import coin_catalog.models as CoinModel
import coin_catalog.api.serializers.list_serializers as serializers


def _success_create(serializer):
    """
    Returns the serialized 'response_data' and 'status'-code
    When objects is Created
    """
    response_data           = serializer.data
    response_data['status'] = 'Created Successfully'
    return response_data, status.HTTP_201_CREATED


def _success_find(serializer):
    """
    Returns the serialized 'response_data' and 'status'-code
    When objects is Found in DB
    """
    response_data           = serializer.data
    response_data['status'] = 'Already exists in DB'
    return response_data, status.HTTP_302_FOUND


#------------------------POST Functions Themselves------------------------#
"""
    When making a POST request, Create function follows this pattern:
        3) If data is not valid, returns Serializer errors
           (Doesn't check for UniqueTogether)
        1) Checks for existing object in DB
        2) If nothing found, tries to create one
"""
class RegionPostRequest:
    """
    This class is designated for
        - Model:   Region
        - Viewset: RegionViewSet
    """
    def get_response(request):
        serializer = serializers.RegionSerializer(data = request.data)
        serializer.is_valid(raise_exception = True)

        region     = CoinModel.Region.objects.filter(
                name__iexact = serializer.validated_data['name']
                )

        if region:
            serializer = serializers.RegionSerializer(region.first())
            return _success_find(serializer)

        serializer.save()
        return _success_create(serializer)


class CountryPostRequest:
    """
    This class is designated for
        - Model:   Country
        - Viewset: CountryViewSet
    """
    def get_response(request):
        serializer = serializers.CountrySerializer(data = request.data)
        serializer.is_valid(raise_exception = True)

        country    = CoinModel.Country.objects.filter(
                region_id    = serializer.validated_data['region'],
                name__iexact = serializer.validated_data['name']
                )

        if country:
            serializer = serializers.CountrySerializer(country.first())
            return _success_find(serializer)

        serializer.save()
        return _success_create(serializer)


class CategoryPostRequest:
    """
    This class is designated for
        - Model:   Category
        - Viewset: CategoryViewSet
    """
    def get_response(request):
        serializer = serializers.CategorySerializer(data = request.data)
        serializer.is_valid(raise_exception = True)

        category   = CoinModel.Category.objects.filter(
                country_id   = serializer.validated_data['country'],
                name__iexact = serializer.validated_data['name']
                )

        if category:
            serializer = serializers.CategorySerializer(category.first())
            return _success_find(serializer)

        serializer.save()
        return _success_create(serializer)


class CollectionPostRequest:
    """
    This class is designated for
        - Model:   Collection
        - Viewset: CollectionViewSet
    """
    def get_response(request):
        serializer = serializers.CollectionSerializer(data = request.data)
        serializer.is_valid(raise_exception = True)

        collection = CoinModel.Collection.objects.filter(
                category_id  = serializer.validated_data['category'],
                name__iexact = serializer.validated_data['name']
                )

        if collection:
            serializer = serializers.CollectionSerializer(collection.first())
            return _success_find(serializer)

        serializer.save()
        return _success_create(serializer)


class CurrencyPostRequest:
    """
    This class is designated for
        - Model:   Currency
        - Viewset: CurrencyViewSet
    """
    def get_response(request):
        serializer = serializers.CurrencySerializer(data = request.data)
        serializer.is_valid(raise_exception = True)

        currency = CoinModel.Currency.objects.filter(
                name__iexact = serializer.validated_data['name']
                )

        if currency:
            serializer = serializers.CurrencySerializer(currency.first())
            return _success_find(serializer)

        serializer.save()
        return _success_create(serializer)


class CountryCurrencyPostRequest:
    """
    This class is designated for
        - Model:   CountryCurrency
        - Viewset: CountryCurrencyViewSet
    """
    def get_response(request):
        serializer = serializers.CountryCurrencySerializer(data = request.data)
        serializer.is_valid(raise_exception = True)

        country_currency = CoinModel.CountryCurrency.objects.filter(
                country_id  = serializer.validated_data['country'],
                currency_id = serializer.validated_data['currency']
                )

        if country_currency:
            serializer = serializers.CountryCurrencySerializer(country_currency.first())
            return _success_find(serializer)

        serializer.save()
        return _success_create(serializer)


class MintedByPostRequest:
    """
    This class is designated for
        - Model:   MintedBy
        - Viewset: MintedByViewSet
    """
    def get_response(request):
        serializer = serializers.MintedBySerializer(data = request.data)
        serializer.is_valid(raise_exception = True)

        minted_by  = CoinModel.MintedBy.objects.filter(
                name__iexact = serializer.validated_data['name']
                )

        if minted_by:
            serializer = serializers.MintedBySerializer(minted_by.first())
            return _success_find(serializer)

        serializer.save()
        return _success_create(serializer)


class DesingerNamePostRequest:
    """
    This class is designated for
        - Model:   DesignerName
        - Viewset: DesignerNameViewSet
    """
    def get_response(request):
        serializer    = serializers.DesignerNameSerializer(data = request.data)
        serializer.is_valid(raise_exception = True)

        designer_name = CoinModel.DesignerName.objects.filter(
                name__iexact = serializer.validated_data['name']
                )

        if designer_name:
            serializer = serializers.MintedBySerializer(designer_name.first())
            return _success_find(serializer)

        serializer.save()
        return _success_create(serializer)


class SculptorNamePostRequest:
    """
    This class is designated for
        - Model:   SculptorName
        - Viewset: SculptorNameViewSet
    """
    def get_response(request):
        serializer    = serializers.SculptorNameSerializer(data = request.data)
        serializer.is_valid(raise_exception = True)

        sculptor_name = CoinModel.SculptorName.objects.filter(
                name__iexact = serializer.validated_data['name']
                )

        if sculptor_name:
            serializer = serializers.SculptorNameSerializer(sculptor_name.first())
            return _success_find(serializer)

        serializer.save()
        return _success_create(serializer)


class MaterialPostRequest:
    """
    This class is designated for
        - Model:   Material
        - Viewset: MaterialViewSet
    """
    def get_response(request):
        serializer    = serializers.MaterialSerializer(data = request.data)
        serializer.is_valid(raise_exception = True)

        material = CoinModel.Material.objects.filter(
                name__iexact = serializer.validated_data['name']
                )

        if material:
            serializer = serializers.MaterialSerializer(material.first())
            return _success_find(serializer)

        serializer.save()
        return _success_create(serializer)


class QualityPostRequest:
    """
    This class is designated for
        - Model:   Quality
        - Viewset: QualityViewSet
    """
    def get_response(request):
        serializer    = serializers.QualitySerializer(data = request.data)
        serializer.is_valid(raise_exception = True)

        quality = CoinModel.Quality.objects.filter(
                name__iexact = serializer.validated_data['name']
                )

        if quality:
            serializer = serializers.QualitySerializer(quality.first())
            return _success_find(serializer)

        serializer.save()
        return _success_create(serializer)


class EdgePostRequest:
    """
    This class is designated for
        - Model:   Edge
        - Viewset: EdgeViewSet
    """
    def get_response(request):
        serializer    = serializers.EdgeSerializer(data = request.data)
        serializer.is_valid(raise_exception = True)

        edge = CoinModel.Edge.objects.filter(
                name__iexact = serializer.validated_data['name']
                )

        if edge:
            serializer = serializers.EdgeSerializer(edge.first())
            return _success_find(serializer)

        serializer.save()
        return _success_create(serializer)


class ShapePostRequest:
    """
    This class is designated for
        - Model:   Shape
        - Viewset: ShapeViewSet
    """
    def get_response(request):
        serializer    = serializers.ShapeSerializer(data = request.data)
        serializer.is_valid(raise_exception = True)

        shape = CoinModel.Shape.objects.filter(
                name__iexact = serializer.validated_data['name']
                )

        if shape:
            serializer = serializers.ShapeSerializer(shape.first())
            return _success_find(serializer)

        serializer.save()
        return _success_create(serializer)


class CoinFamilyPostRequest:
    """
    This class is designated for
        - Model:   CoinFamily
        - Viewset: CoinFamilyViewSet
    """
    def get_response(request):
        serializer    = serializers.CoinFamilySerializer(data = request.data)
        serializer.is_valid(raise_exception = True)

        coin_family = CoinModel.CoinFamily.objects.filter(
                collection_id = serializer.validated_data['collection'],
                name__iexact  = serializer.validated_data['name']
                )

        if coin_family:
            serializer = serializers.CoinFamilySerializer(coin_family.first())
            return _success_find(serializer)

        serializer.save()
        return _success_create(serializer)


class CoinStylePostRequest:
    """
    This class is designated for
        - Model:   CoinStyle
        - Viewset: CoinStyleViewSet
    """
    def get_response(request):
        serializer    = serializers.CoinStyleSerializer(data = request.data)
        serializer.is_valid(raise_exception = True)

        coin_style = CoinModel.CoinStyle.objects.filter(
                coin_family_id           = serializer.validated_data['coin_family'],
                additional_name__iexact  = serializer.validated_data['additional_name'],
                year                     = serializer.validated_data['year'],
                denomination_value       = serializer.validated_data['denomination_value'],
                denomination_currency_id = serializer.validated_data['denomination_currency'],
                material_id              = serializer.validated_data['material'],
                standard                 = serializer.validated_data['standard'],
                shape_id                 = serializer.validated_data['shape'],
                quality_id               = serializer.validated_data['quality'],
                is_substyle              = serializer.validated_data['is_substyle']
                )

        if coin_style:
            serializer = serializers.CoinStyleSerializer(coin_style.first())
            return _success_find(serializer)

        serializer.save()
        return _success_create(serializer)


class SubStylePostRequest:
    """
    This class is designated for
        - Model:   SubStyle
        - Viewset: SubStyleViewSet
    """
    def get_response(request):
        serializer    = serializers.SubStyleSerializer(data = request.data)
        serializer.is_valid(raise_exception = True)

        sub_style = CoinModel.SubStyle.objects.filter(
                substyle_coin_id = serializer.validated_data['substyle_coin']
                )

        if sub_style:
            serializer = serializers.SubStyleSerializer(sub_style.first())
            return _success_find(serializer)

        serializer.save()
        return _success_create(serializer)


class NotePostRequest:
    """
    This class is designated for
        - Model:   Note
        - Viewset: NoteViewSet
    """
    def get_response(request):
        serializer    = serializers.NoteSerializer(data = request.data)
        serializer.is_valid(raise_exception = True)

        note = CoinModel.Note.objects.filter(
                coin_style_id       = serializer.validated_data['coin_style'],
                description__iexact = serializer.validated_data['description']
                )

        if note:
            serializer = serializers.NoteSerializer(note.first())
            return _success_find(serializer)

        serializer.save()
        return _success_create(serializer)


class SideOfCoinPostRequest:
    """
    This class is designated for
        - Model:   SideOfCoin
        - Viewset: SideOfCoinViewSet
    """
    def get_response(request):
        serializer    = serializers.SideOfCoinSerializer(data = request.data)
        serializer.is_valid(raise_exception = True)

        side_of_coin = CoinModel.SideOfCoin.objects.filter(
                name__iexact = serializer.validated_data['name']
                )

        if side_of_coin:
            serializer = serializers.SideOfCoinSerializer(side_of_coin.first())
            return _success_find(serializer)

        serializer.save()
        return _success_create(serializer)


class CoinDesignerPostRequest:
    """
    This class is designated for
        - Model:   CoinDesigner
        - Viewset: CoinDesignerViewSet
    """
    def get_response(request):
        serializer    = serializers.CoinAllDesignersSerializer(data = request.data)
        serializer.is_valid(raise_exception = True)

        coin_designer = CoinModel.CoinDesigner.objects.filter(
                coin_style_id = serializer.validated_data['coin_style'],
                side_id       = serializer.validated_data['side'],
                designer_id   = serializer.validated_data['designer']
                )

        if coin_designer:
            serializer = serializers.CoinAllDesignersSerializer(coin_designer.first())
            return _success_find(serializer)

        serializer.save()
        return _success_create(serializer)


class CoinSculptorPostRequest:
    """
    This class is designated for
        - Model:   CoinSculptor
        - Viewset: CoinSculptorViewSet
    """
    def get_response(request):
        serializer    = serializers.CoinAllSculptorsSerializer(data = request.data)
        serializer.is_valid(raise_exception = True)

        coin_sculptor = CoinModel.CoinSculptor.objects.filter(
                coin_style_id = serializer.validated_data['coin_style'],
                side_id       = serializer.validated_data['side'],
                sculptor_id   = serializer.validated_data['sculptor']
                )

        if coin_sculptor:
            serializer = serializers.CoinAllSculptorsSerializer(coin_sculptor.first())
            return _success_find(serializer)

        serializer.save()
        return _success_create(serializer)


class ImagePostRequest:
    """
    This class is designated for
        - Model:   Image
        - Viewset: ImageViewSet
    """
    def get_response(request):
        serializer    = serializers.ImageSerializer(data = request.data)
        serializer.is_valid(raise_exception = True)

        image = CoinModel.Image.objects.filter(
                coin_style_id = serializer.validated_data['coin_style'],
                side_id       = serializer.validated_data['side']
                )

        if image:
            serializer = serializers.ImageSerializer(image.first())
            return _success_find(serializer)

        serializer.save()
        return _success_create(serializer)
