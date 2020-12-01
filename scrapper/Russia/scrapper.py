import json
import filetype
import time

import requests
from bs4 import BeautifulSoup

from scrapper import URL
from scrapper.coin import coin as coin_class


def _make_a_request(specified_url):
    try:
        r = requests.get(specified_url, headers = URL.USER_HEADERS)
        return r

    except requests.exceptions.ConnectionError:
        time.sleep(5)
        return _make_a_request(specified_url)


def _are_words_in_string(words: list, sentence: str) -> bool:
    """
    Function checks if the 'sentence' has any of the specified 'words'
    """
    for word in words:
        if word in sentence:
            return True

    return False


def _record_images(ID, images):
    """
    Function records the images based on image block and ID
    """
    image_path_list = []

    for index, image in enumerate(images, start = 1):
        r = _make_a_request(URL.RU_IMAGE_ROOT_URL + image['src'])

        extension = filetype.guess(r.content).extension
        coin_path = f'img/{ID}__{index}.{extension}'

        with open('out/' + coin_path, 'wb') as fout:
            fout.write(r.content)

        image_path_list.append(coin_path)

    return image_path_list


def _process_single_line_of_characteristics(coin, key, value):
    key   = key.text
    value = value.text

    if ( _are_words_in_string(
            ['copper, nickel', 'Platinum 999/1000', 'Nickel plated steel', 'German silver', 'Copper, Zinc/Copper, Nickel', 'Silver 925/1000 - Gold 999/1000', 'Brass/Copper, Nickel', 'Cupro-nickel', 'Brass/Copper, Nickel', 'Silver 900/1000 - Gold 900/1000', 'Brass plated steel', 'Silver 900/1000', 'Silver 900/1000 - Gold 900/1000', 'brass', 'Silver 500/1000', 'Gold 900/1000 - Silver 900/1000', 'Gold 999/1000', 'Silver 925/1000', 'Silver 925/1000 - Gold 999/1000', 'Gold   900/1000', 'Palladium 999/1000', 'Gold 900/1000 - Silver 925/1000', 'brass/cupronickel', 'Silver 999/1000', 'Copper, Zinc/Copper, Nickel', 'cupronickel', 'German silver/brass', 'brass/German silver', 'silver 925/1000, gilded ', 'Brass plated steel/Nickel plated steel', 'Gold 900/1000'],
            value
         )
       ):
        coin.material = value

    elif ( _are_words_in_string(
            ['tchervonets', '1 ruble', '2 rubles', '3 rubles', '5 rubles',
             '10 rubles', '20 rubles', '25 rubles', '50 rubles', '100 rubles',
             '150 rubles', '200 rubles', '500 rubles', '1 000 rubles', '10 000 rubles', 
             '25 000 rubles', '50 000 rubles'],
            value
           )
         ):
        if (value == 'tchervonets'):
            coin.denomination_value = 1.0
            coin.denomination_currency = 'tchervonets'
        else:
            coin.denomination_currency = value

    elif ( _are_words_in_string(['Quality', 'quality'], key) ):
        coin.quality = value

    elif ( _are_words_in_string(['weight', 'Weight'], key) ):
        coin.weight = value

    elif ( _are_words_in_string(['metal content'], key) ):
        coin.notes.append(key + ': ' + value)

    elif ( _are_words_in_string(['ring', 'disk'], key) ):
        coin.notes.append(key)

    elif ( _are_words_in_string(['Diameter', 'diameter'], key) ):
        coin.shape  = 'Round'
        coin.length = value

    elif ( _are_words_in_string(['Length', 'length'], key) ):
        coin.shape  = 'Rectangular'
        coin.length = value

    elif ( _are_words_in_string(['Width', 'width'], key) ):
        coin.shape = 'Rectangular'
        coin.length = value

    elif ( _are_words_in_string(['Thickness', 'thickness'], key) ):
        coin.thickness = value

    elif ( _are_words_in_string(['Mintage', 'mintage'], key) ):
        coin.mintage = value

    else:
        with open('out/notes.txt', 'a') as fout:
            fout.write('Found the exception for characteristics block:\n')
            fout.write(f'\tCoin ID: {coin.id}\n')
            fout.write('\tMessage:\n')
            fout.write(f'\t\t{key} - {value}\n\n')

    return coin


def _process_coin_characteristics(coin, characteristics_block):
    rows = characteristics_block.find_all('div', {'class': 'commemor-coin_info_characteristic'})

    for row in rows:
        key   = row.find('div', {'class': 'characteristic_denomenation'})
        value = row.find('div', {'class': 'characteristic_value'})

        coin = _process_single_line_of_characteristics(coin, key, value)

    return coin


def _get_authors_block(coin_body):
    """
    Gets the specific paragraph tag that holds
    information about authors, sculptors, minted_by and edge
    out of all <p> on the page
    """
    paragraphs = coin_body.find_all('p')

    for paragraph in paragraphs:
        if ( _are_words_in_string(
                 ['Designers', 'Sculptors', 'Mint', 'Edge'],
                 paragraph.text
             )
           ):
            return paragraph

    return None


def _process_single_line_from_authors_description(coin, information_line):
    """
    Gets the single line from the "Authors" block
    records Authors/Sculptors/MintedBy/Edge based on the presence
    particular words
    """
    if ( _are_words_in_string(
                ['artist and sculptor', 'artists and sculptors', 'artists and sculptor', 'artist and sculptors'],
                information_line
         )
       ):
       coin.authors   = information_line
       coin.sculptors = information_line

    #Matches for designers
    elif ( _are_words_in_string(
                ['Designers', 'Designer', 'Artist', 'artiat', 'artist', 'artists'],
                information_line
         )
       ):
         coin.authors = information_line

    #Matches for sculptors
    elif ( _are_words_in_string(
                ['sculptors', 'Sculptor', 'sculptor', 'Sculptors', 'Sculptural', 'Sculptos', 'sculpter', 'culptor'],
                information_line
           )
         ):
         coin.sculptors = information_line

    #Matches for mint
    elif ( _are_words_in_string(
                ['mints', 'Mint', 'mint'],
                information_line
           )
         ):
         coin.minted_by = information_line

    elif ( _are_words_in_string(
                ['edge', 'Edge', 'adge'],
                information_line
           )
         ):
        coin.edge = information_line

    else:
        with open('out/notes.txt', 'a') as fout:
            fout.write(f'{coin.id} has an exception for information line\n')
            fout.write(f'\t{information_line}')
            fout.write('\n\n')

    return coin


def _record_authors_information(coin, information_block):
    if not information_block:
        coin.authors   = []
        coin.sculptors = []
        coin.minted_by = None
        coin.edge      = None

        return coin

    #Block -> STR -> Array(based on <br/>)
    information_lines = str(information_block).replace('<p>', '').replace('</p>', '').split('<br/>')

    for line in information_lines:
        coin = _process_single_line_from_authors_description(coin, line)

    return coin


def main():
    start_time = time.monotonic()

    coin_counter = 1

    with open('scrapper/Russia/in.html', 'r') as fin:
        coin_table = BeautifulSoup(fin, 'html.parser')

    coin_styles = coin_table.find_all('div', {'class': 'coins-tile_item'})

    for coin_style in coin_styles:
        COIN = coin_class()

        #Base Information
        COIN.id       = coin_counter
        COIN.region   = 'Europe'
        COIN.country  = 'Russia'
        COIN.category = 'Russian Federation'


        r    = _make_a_request(URL.RU_COIN_BASE_URL + coin_style.a['href'])
        soup = BeautifulSoup(r.content, 'html.parser')

        intro_header = soup.find('div', {'class': 'commemor-coin_intro'})
        collection = intro_header.find('div', {'class': 'commemor-coin_intro_text'})

        #Recording Collection
        if collection.text == '':
            COIN.collection = None
        else:
            COIN.collection = collection.text

        #Recording Coin Family
        COIN.coin_family = soup.find('span', {'class': 'referenceable'}).text
        print("Currently Processing: ", COIN.coin_family)

        #Recording Year
        year = intro_header.find('div', {'class': 'money_option'}).find_all('div')
        if year:
            year = year[-1].text
        else:
            year = -1

        COIN.year = year

        #Get the Coin Description
        #   Dimentions, weight, mintage, material, standard
        characteristics_block = soup.find('div', {'class': 'commemor-coin_info_characteristics'})
        COIN = _process_coin_characteristics(COIN, characteristics_block)

        #Get Authors, Sculptors, Edge and Minted_by
        description_block = soup.find('div', {'class': 'row commemor-coin'})
        authors_block = _get_authors_block(description_block)
        COIN = _record_authors_information(COIN, authors_block)

        #Recording Images
        images_block = soup.find('div', {'class': 'commemor-coin_images row'})
        images = images_block.find_all('img')
        COIN.images = _record_images(coin_counter, images)

        #Increase coin_counter to represent other coin
        coin_counter += 1

        #Append the Coin to the Output file
        with open('out/out.json', 'a') as fout:
            json.dump(COIN.to_dict(), fout, indent = 4)
            fout.write(',\n')

    print(f'Elapsed time: {time.monotonic() - start_time}')
