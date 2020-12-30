"""
    General Purpose Parser for "Coin Catalog"

    Accepts:  JSON File
    Performs: Insertion of the Coins in the file
"""
import os
import requests
import json


PATH_TO_FILE = 'formatted_data/Belarus/formatted.json'
IMAGE_PATH   = 'formatted_data/Belarus/'
API_URLS = {
    'region':           'http://localhost:8000/api/catalog/region/',
    'country':          'http://localhost:8000/api/catalog/country/',
    'category':         'http://localhost:8000/api/catalog/category/',
    'collection':       'http://localhost:8000/api/catalog/collection/',
    'currency':         'http://localhost:8000/api/catalog/currency/',
    'country_currency': 'http://localhost:8000/api/catalog/country_currency/',
    'minted_by':        'http://localhost:8000/api/catalog/minted_by/',
    'designer_name':    'http://localhost:8000/api/catalog/designer_name/',
    'sculptor_name':    'http://localhost:8000/api/catalog/sculptor_name/',
    'material':         'http://localhost:8000/api/catalog/material/',
    'quality':          'http://localhost:8000/api/catalog/quality/',
    'edge':             'http://localhost:8000/api/catalog/edge/',
    'shape':            'http://localhost:8000/api/catalog/shape/',
    'coin_family':      'http://localhost:8000/api/catalog/coin_family/',
    'coin_style':       'http://localhost:8000/api/catalog/coin_style/',
    'sub_style':        'http://localhost:8000/api/catalog/sub_style/',
    'note':             'http://localhost:8000/api/catalog/note/',
    'side_of_coin':     'http://localhost:8000/api/catalog/side_of_coin/',
    'coin_designer':    'http://localhost:8000/api/catalog/coin_designer/',
    'coin_sculptor':    'http://localhost:8000/api/catalog/coin_sculptor/',
    'image':            'http://localhost:8000/api/catalog/image/'
}


class COLOR:
    """
        Class holds the specific characters that manage output color
    """
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


class Coin:
    """
        This Class is designated to hold all necessary information
        of a single coin for better readability that is read from the file
    """
    def __init__(self, coin: dict):
        self.region = {
            'id':   -1,
            'name': coin['region']
        }
        self.country = {
            'id':   -1,
            'name': coin['country']
        }
        self.category = {
            'id':   -1,
            'name': coin['category']
        }
        self.collection = {
            'id':   -1,
            'name': coin['collection']
        }
        self.denomination = {
            'id':               -1,
            'country_currency': -1,
            'currency_name':    coin['denomination']['currency'],
            'value':            coin['denomination']['value']
        }
        self.minted_by = {
            'id':   -1,
            'name': coin['minted_by']
        }
        self.material = {
            'id':       -1,
            'name':     coin['material'],
            'standard': coin['standard']
        }
        self.quality = {
            'id':   -1,
            'name': coin['quality']
        }
        self.edge = {
            'id':   -1,
            'name': coin['edge']
        }
        self.shape = {
            'id':   -1,
            'name': coin['shape']
        }
        self.coin_family = {
            'id':   -1,
            'name': coin['coin_family']
        }
        self.coin_style = {
            'id':                       -1,
            'name':                     coin['additional_name'] if coin['additional_name'] else "",
            'is_substyle':              False if not coin['substyle_of'] else True,
            # relative means - 'relative id' to the file that is being parsed
            'relative_parent_style_id': coin['substyle_of'],
            # absolute means - 'absolute id' to the DB that information is sent to
            'absolute_parent_style_id': -1
        }
        self.information = {
            'year':         coin['year'],
            'mintage':      coin['mintage'],
            'weight':       coin['weight'],
            'length':       coin['length'],
            'width':        coin['width'],
            'thickness':    coin['thickness']
        }
        self.designers = [
            {
                'id':           -1,
                'name':         designer,
                'side_id':      -1,
                'side_name':    side
            }
            # First 'for' loop creates a touple that have the format:
            # ('SIDE_NAME', 'ARRAY_OF_DESIGNERS')
            #
            # e.g ('Side', [Designers])
            for side, designers in coin['authors'].items()
            # Second 'for' loop splits array into single item:
            # ('SIDE_NAME', DESIGNER)
            for designer in designers
        ]
        self.sculptors = [
            {
                'id':           -1,
                'name':         sculptor,
                'side_id':      -1,
                'side_name':    side
            }
            # First 'for' loop creates a touple that have the format:
            # ('SIDE_NAME', 'ARRAY_OF_SCULPTORS')
            #
            # e.g ('Side', [Sculptors])
            for side, designers in coin['sculptors'].items()
            # Second 'for' loop splits array into single item:
            # ('SIDE_NAME', SCULPTOR)
            for sculptor in sculptors
        ]
        self.notes  = coin['notes']
        self.images = [
            {
                'side_id':       -1,
                'side_name':     side,
                'path_to_image': image_path
            }
            for side, image_path in coin['images'].items()
        ]


def _find_coin_with_specified_id(coins: list, id: int):
    """
        Loops over the array of all coins in file
        to find the coin with specified relative to file
        'coin_id'
    """
    for coin in coins:
        if id == coin['id']:
            return coin

    return None


def _send_region(coin: 'Coin'):
    """
        Sends the ('region_name') to the server and returns
        'region_id' based on the response
    """
    data = {'name': coin.region['name']}

    r = requests.post(API_URLS['region'], data = data)
    coin.region['id'] = ( r.json() )['id']


def _send_country(coin: 'Coin'):
    """
        Sends the ('region_id' and 'country_name') to the server and returns
        'country_id' based on the response
    """
    data = {
        'region': coin.region['id'],
        'name':   coin.country['name']
        }

    r = requests.post(API_URLS['country'], data = data)
    coin.country['id'] = ( r.json() )['id']


def _send_category(coin: 'Coin'):
    """
        Sends the ('country_id' and 'category_name') to the server and returns
        'category_id' based on the response
    """
    data = {
        'country': coin.country['id'],
        'name':    coin.category['name']
        }

    r = requests.post(API_URLS['category'], data = data)
    coin.category['id'] = ( r.json() )['id']


def _send_collection(coin: 'Coin'):
    """
        Sends the ('category_id' and 'collection_name') to the server
            - If the 'collection_name' equals to NULL, replace it with 'N/A'
        and returns
        'collection_id' based on the response
    """
    data = {
        'category': coin.category['id'],
        'name':     coin.collection['name'] if coin.collection['name'] else 'N/A'
        }

    r = requests.post(API_URLS['collection'], data = data)
    coin.collection['id'] = ( r.json() )['id']


def _send_currency_name(coin: 'Coin'):
    """
        Sends the ('currency_name') to the server
        and returns
        'currency_id' based on the response
    """
    data = {
        'name': coin.denomination['currency_name']
        }

    r = requests.post(API_URLS['currency'], data = data)
    coin.denomination['id'] = ( r.json() )['id']


def _send_country_currency(coin: 'Coin'):
    """
        Sends the ('country_id' and 'currency_id') to the server
        and returns
        'country_currency_id' based on the response
    """
    data = {
        'country':  coin.country['id'],
        'currency': coin.denomination['id']
        }

    r = requests.post(API_URLS['country_currency'], data = data)
    coin.denomination['country_currency'] = ( r.json() )['id']


def _send_minted_by(coin: 'Coin'):
    """
        Sends the ('minted_by_name') to the server
        and returns
        'minted_by_id' based on the response
    """
    data = {
        'name': coin.minted_by['name']
        }

    r = requests.post(API_URLS['minted_by'], data = data)
    coin.minted_by['id'] = ( r.json() )['id']


def _send_designer_name(designer: dict):
    """
        Sends the single Designer name to the server and
        returns its ID
    """
    data = {
        'name': designer['name']
    }

    r = requests.post(API_URLS['designer_name'], data = data)
    designer['id'] = ( r.json() )['id']


def _send_sculptor_name(sculptor: dict):
    """
        Sends the single Sculptor name to the server and
        returns its ID
    """
    data = {
        'name': sculptor['name']
    }

    r = requests.post(API_URLS['sculptor_name'], data = data)
    sculptor['id'] = ( r.json() )['id']


def _send_material(coin: 'Coin'):
    """
        Sends the ('material_name') to the server
        and returns
        'material_id' based on the response
    """
    data = {
        'name': coin.material['name']
        }

    r = requests.post(API_URLS['material'], data = data)
    coin.material['id'] = ( r.json() )['id']


def _send_quality(coin: 'Coin'):
    """
        Sends the ('quality_name') to the server
        and returns
        'quality_id' based on the response
    """
    data = {
        'name': coin.quality['name']
        }

    r = requests.post(API_URLS['quality'], data = data)
    coin.quality['id'] = ( r.json() )['id']


def _send_edge(coin: 'Coin'):
    """
        Sends the ('edge_name') to the server
        and returns
        'edge_id' based on the response
    """
    data = {
        'name': coin.edge['name']
        }

    r = requests.post(API_URLS['edge'], data = data)
    coin.edge['id'] = ( r.json() )['id']


def _send_shape(coin: 'Coin'):
    """
        Sends the ('shape_name') to the server
        and returns
        'shape_id' based on the response
    """
    data = {
        'name': coin.shape['name']
        }

    r = requests.post(API_URLS['shape'], data = data)
    coin.shape['id'] = ( r.json() )['id']


def _send_coin_family(coin: 'Coin'):
    """
        Sends the ('collection_id' and 'coin_family_name') to the server
        and returns
        'coin_family_id' based on the response
    """
    data = {
        'collection': coin.collection['id'],
        'name':       coin.coin_family['name']
        }

    r = requests.post(API_URLS['coin_family'], data = data)
    coin.coin_family['id'] = ( r.json() )['id']


def _send_substyle_connector(coin: 'Coin'):
    data = {
        'substyle_coin':    coin.coin_style['id'],
        'parent_coin':      coin.coin_style['absolute_parent_style_id']
    }

    r = requests.post(API_URLS['sub_style'], data = data)


def _send_coin_style(coin: 'Coin', coins: list):
    """
        Sends the necessary information to the server for coin_style
        and returns
        'coin_style_id' based on the response

        If 'coin_style' is a sub_style of another coin,
        looks for the parent style and
    """
    data = {
        'coin_family':           coin.coin_family['id'],
        'additional_name':       coin.coin_style['name'],
        'minted_by':             coin.minted_by['id'],
        'year':                  coin.information['year'],
        'denomination_value':    coin.denomination['value'],
        'denomination_currency': coin.denomination['country_currency'],
        'shape':                 coin.shape['id'],
        'quality':               coin.quality['id'],
        'edge':                  coin.edge['id'],
        'material':              coin.material['id'],
        'standard':              coin.material['standard'],
        'mintage':               coin.information['mintage'],
        'weight':                coin.information['weight'],
        'length':                coin.information['length'],
        'width':                 coin.information['width'],
        'thickness':             coin.information['thickness'],
        'is_substyle':           coin.coin_style['is_substyle']
        }

    r = requests.post(API_URLS['coin_style'], data = data)
    coin.coin_style['id'] = ( r.json() )['id']

    if coin.coin_style['is_substyle']:
        parent_style = _find_coin_with_specified_id(coins, coin.coin_style['relative_parent_style_id'])
        parent_style = Coin(parent_style)
        _create_coin(parent_style, coins, mode = "SEARCH")
        coin.coin_style['absolute_parent_style_id'] = parent_style.coin_style['id']
        _send_substyle_connector(coin)


def _send_notes(coin: 'Coin'):
    """
        Loops over all notes that coin has,
        sends them to the seriver using
        'coin_style_id'
        No need to store notes
    """
    for note in coin.notes:
        data = {
            'coin_style':   coin.coin_style['id'],
            'description':  note
        }
        requests.post(API_URLS['note'], data = data)


def _send_coin_side_name(coin_snippet: dict):
    """
        CoinAuthor is either 'Coin Designer', 'Coin Sculptor' or 'Image'
        Sends the single Side name to the server and
        returns its ID
    """
    data = {
        'name': coin_snippet['side_name']
    }

    r = requests.post(API_URLS['side_of_coin'], data = data)
    coin_snippet['side_id'] = ( r.json() )['id']


def _send_designers(coin: 'Coin'):
    """
        Sends designers' names to the server
        Also Handles 'Many-to-Many' relationship

        Process:
            - Sends the 'designer name' and gets its ID
            - Sends the 'side of the coin' and gets its ID
            - Combines all data and sends Many-to-Many table
    """
    for designer in coin.designers:
        _send_designer_name(designer)
        _send_coin_side_name(designer)

        data = {
            'coin_style':   coin.coin_style['id'],
            'side':         designer['side_id'],
            'designer':     designer['id']
        }
        requests.post(API_URLS['coin_designer'], data = data)


def _send_sculptors(coin: 'Coin'):
    """
        Sends sculptors' names to the server
        Also Handles 'Many-to-Many' relationship


        Process:
            - Sends the 'sculptor name' and gets its ID
            - Sends the 'side of the coin' and gets its ID
            - Combines all data and sends Many-to-Many table
    """
    for sculptor in coin.sculptors:
        _send_sculptor_name(sculptor)
        _send_coin_side_name(sculptor)

        data = {
            'coin_style':   coin.coin_style['id'],
            'side':         sculptor['side_id'],
            'sculptor':     sculptor['id']
        }
        requests.post(API_URLS['coin_sculptor'], data = data)


def _send_images(coin: 'Coin'):
    """
        Sends side name and images to the server


        Process:
            - Sends the 'side of the coin' and gets its ID
            - Finds the absolute PATH to image and loads it
            - Combines all data and sends Many-to-Many table
    """
    for image in coin.images:
        _send_coin_side_name(image)

        image_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), IMAGE_PATH)

        data = {
            'coin_style':   coin.coin_style['id'],
            'side':         image['side_id']
        }

        with open( (image_path + image['path_to_image']), 'rb') as fin:
            file = {'image': fin}
            requests.post(API_URLS['image'], data = data, files = file)



def _create_coin(coin: 'Coin', coins: list, mode = None):
    """
        Holds the functions for coin_style creation
        If mode:
            - Search for parent coin
            - No need to get/create things other than 'coin_style'
    """
    _send_region(coin)
    _send_country(coin)
    _send_category(coin)
    _send_collection(coin)

    _send_currency_name(coin)
    _send_country_currency(coin)

    _send_minted_by(coin)

    _send_material(coin)
    _send_quality(coin)
    _send_edge(coin)
    _send_shape(coin)

    _send_coin_family(coin)
    _send_coin_style(coin, coins)

    # If not NULL, then it is a basic search
    if mode:
        return

    _send_notes(coin)
    _send_designers(coin)
    _send_sculptors(coin)
    _send_images(coin)


def main():
    """
        Opens the file, walks over the coins, and
        sends the data to the server
    """
    full_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), PATH_TO_FILE)

    with open(full_path, 'r') as fin:
        coins = json.load(fin)

    for index, coin_style in enumerate(coins, start = 1):
        coin = Coin(coin_style)

        print(f'Currently processing {COLOR.BOLD + COLOR.GREEN}{index} / {len(coins)}{COLOR.END}')

        _create_coin(coin, coins)



if __name__ == '__main__':
    try:
        main()

    except KeyboardInterrupt:
        print('Program is Terminated...')
