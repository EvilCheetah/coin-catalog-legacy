import re
import json


def _process_material(coin):
    """
    Matches materials to the list of the materials
    presented on the CBR coin catalog and
    sets the Material, Standard and Notes to
    proper fields
    """
    if (coin['material'] == 'Gold 900/1000'):
        coin['material'] = 'Gold'
        coin['standard'] = 900.0

    elif (coin['material'] == 'Silver 925/1000'):
        coin['material'] = 'Silver'
        coin['standard'] = 925.0

    elif (coin['material'] == 'Nickel plated steel'):
        coin['material'] = 'Steel'
        coin['standard'] = -1.0
        coin['note'].append('Plated with Nickel')

    elif (coin['material'] == 'German silver'):
        coin['material'] = 'German Silver'
        coin['standard'] = -1.0

    elif (coin['material'] == 'cupronickel' or coin['material'] == 'copper, nickel'):
        coin['material'] = 'Copper-Nickel'
        coin['standard'] = -1.0

    elif (coin['material'] == 'Silver 999/1000'):
        coin['material'] = 'Silver'
        coin['standard'] = 999.0

    elif (coin['material'] == 'Silver 925/1000 - Gold 999/1000'):
        coin['material'] = 'Silver'
        coin['standard'] = 925.0
        coin['note'].append('Plated with gold')
        coin['note'].append('Standard of plated elements: Au999')

    elif (coin['material'] == 'Silver 900/1000 - Gold 900/1000' or coin['material'] == 'Gold 900/1000 - Silver 900/1000'):
        coin['material'] = 'Silver'
        coin['standard'] = 900.0
        coin['note'].append('Plated with gold')
        coin['note'].append('Standard of plated elements: Au900')

    elif (coin['material'] == 'Silver 900/1000'):
        coin['material'] = 'Silver'
        coin['standard'] = 900.0

    elif (coin['material'] == 'Brass plated steel'):
        coin['material'] = 'Steel'
        coin['standard'] = -1.0
        coin['note'].append('Plated with Brass')

    elif (coin['material'] == 'brass'):
        coin['material'] = 'Brass'
        coin['standard'] = -1.0

    elif (coin['material'] == 'brass/cupronickel' or coin['material'] == 'Brass/Copper, Nickel'):
        coin['material'] = 'Nickel'
        coin['standard'] = -1.0
        coin['note'].append('Ring material - Brass-Copper')

    elif (coin['material'] == 'Gold 999/1000'):
        coin['material'] = 'Gold'
        coin['standard'] = 999.0

    elif (coin['material'] == 'Cupro-nickel'):
        coin['material'] = 'Copper-Nickel'
        coin['standard'] = -1.0

    elif (coin['material'] == 'silver 925/1000, gilded'):
        coin['material'] = 'Silver'
        coin['standard'] = 925.0
        coin['note'].append('Coin is Gilded')

    elif (coin['material'] == 'Brass plated steel/Nickel plated steel'):
        coin['material'] = 'Steel'
        coin['standard'] = -1.0
        coin['note'].append('Coin is plated with Nickel')
        coin['note'].append('Ring material - Steel')
        coin['note'].append('Ring is plated with Brass')

    elif (coin['material'] == 'Palladium 999/1000'):
        coin['material'] = 'Palladium'
        coin['standard'] = 999.0

    elif (coin['material'] == 'Platinum 999/1000'):
        coin['material'] = 'Platinum'
        coin['standard'] = 999.0

    elif (coin['material'] == 'Silver 500/1000'):
        coin['material'] = 'Silver'
        coin['standard'] = 500.0

    elif (coin['material'] == 'German silver/brass'):
        coin['material'] = 'Brass'
        coin['standard'] = -1.0
        coin['note'].append('Ring material - German Silver')

    elif (coin['material'] == 'Copper, Zinc/Copper, Nickel'):
        coin['material'] = 'Copper-Nickel'
        coin['standard'] = -1.0
        coin['note'].append('Ring material - Copper-Zinc')

    elif (coin['material'] == 'Gold 900/1000 - Silver 925/1000'):
        coin['material'] = 'Silver'
        coin['standard'] = 925.0
        coin['note'].append('Ring material - Gold')
        coin['note'].append('Ring material standard - Au900')

    else:
        with open('errors.log', 'a') as fout:
            fout.write(f'Found an error in coin with id: {coin["id"]}')
            fout.write(f'\tError Message: Material doesn\'t match')
            fout.write('\n\n')

    return coin


def _process_denomination(coin):
    """
    Matches denominations to the values presented on
    CBR coin catalog and sets
    Denomination_Value and Denomination_Currency
    to the proper fields
    """
    if (coin['denomination_currency'] == 'tchervonets'):
        coin['denomination_value']    = 1.0
        coin['denomination_currency'] = 'Tchervonets'

    elif (coin['denomination_currency'] == '1 ruble'):
        coin['denomination_value']    = 1.0
        coin['denomination_currency'] = 'RUB'

    elif (coin['denomination_currency'] == '2 rubles'):
        coin['denomination_value']    = 2.0
        coin['denomination_currency'] = 'RUB'

    elif (coin['denomination_currency'] == '3 rubles'):
        coin['denomination_value']    = 3.0
        coin['denomination_currency'] = 'RUB'

    elif (coin['denomination_currency'] == '5 rubles'):
        coin['denomination_value']    = 5.0
        coin['denomination_currency'] = 'RUB'

    elif (coin['denomination_currency'] == '10 rubles'):
        coin['denomination_value']    = 10.0
        coin['denomination_currency'] = 'RUB'

    elif (coin['denomination_currency'] == '20 rubles'):
        coin['denomination_value']    = 20.0
        coin['denomination_currency'] = 'RUB'

    elif (coin['denomination_currency'] == '25 rubles'):
        coin['denomination_value']    = 25.0
        coin['denomination_currency'] = 'RUB'

    elif (coin['denomination_currency'] == '50 rubles'):
        coin['denomination_value']    = 50.0
        coin['denomination_currency'] = 'RUB'

    elif (coin['denomination_currency'] == '100 rubles'):
        coin['denomination_value']    = 100.0
        coin['denomination_currency'] = 'RUB'

    elif (coin['denomination_currency'] == '150 rubles'):
        coin['denomination_value']    = 150.0
        coin['denomination_currency'] = 'RUB'

    elif (coin['denomination_currency'] == '200 rubles'):
        coin['denomination_value']    = 200.0
        coin['denomination_currency'] = 'RUB'

    elif (coin['denomination_currency'] == '500 rubles'):
        coin['denomination_value']    = 500.0
        coin['denomination_currency'] = 'RUB'

    elif (coin['denomination_currency'] == '1 000 rubles'):
        coin['denomination_value']    = 1000.0
        coin['denomination_currency'] = 'RUB'

    elif (coin['denomination_currency'] == '10 000 rubles'):
        coin['denomination_value']    = 10000.0
        coin['denomination_currency'] = 'RUB'

    elif (coin['denomination_currency'] == '25 000 rubles'):
        coin['denomination_value']    = 25000.0
        coin['denomination_currency'] = 'RUB'

    elif (coin['denomination_currency'] == '50000 rubles'):
        coin['denomination_value']    = 50000.0
        coin['denomination_currency'] = 'RUB'

    else:
        with open('errors.log', 'a') as fout:
            fout.write(f'Found an error in coin with id: {coin["id"]}')
            fout.write(f'\tError Message: Denomination doesn\'t match')
            fout.write('\n\n')

    return coin


def _process_characteristics(coin):
    """
    Processes the Weight, Length, Width, Thickness
        removes the stuff in parenthesis, strips the string
        from the space charactes and converts in to float
    """
    if ( isinstance(coin['weight'], str) ):
        if (coin['weight'] == ''):
            coin['weight'] = -1.0
        else:
            weight = re.sub('\(.*', '', str(coin['weight'])).strip().replace(',', '.')
            coin['weight'] = float(weight)

    if ( isinstance(coin['length'], str) ):
        if (coin['length'] == ''):
            coin['length'] = -1.0

        else:
            length = re.sub('\(.*', '', str(coin['length'])).strip().replace(',', '.')
            coin['length'] = float(length)

    if ( isinstance(coin['width'], str) ):
        if (coin['width'] == ''):
            coin['width'] = -1.0

        else:
            width = re.sub('\(.*', '', str(coin['width'])).strip().replace(',', '.')
            coin['width'] = float(width)

    if ( isinstance(coin['thickness'], str) ):
        if (coin['thickness'] == ''):
            coin['thickness'] = -1.0

        else:
            thickness = re.sub('\(.*', '', str(coin['thickness'])).strip().replace(',', '.')
            coin['thickness'] = float(thickness)

    return coin


def _process_mintage(coin):
    if (coin['mintage'] == ' \u2014 '):
        coin['mintage'] = -1

    else:
        coin['mintage'] = int(coin['mintage'].replace(',', '').replace('up to', '').replace('*', '').strip())

    return coin


def _process_quality(coin):
    if coin['quality']:
        if (coin['quality'] == 'UNC'):
            coin['quality'] = 'Uncirculated'

        elif (coin['quality'] == 'BU'):
            coin['quality'] = 'Brilliant-Uncirculated'

        elif (coin['quality'] == 'Proof-like'):
            coin['quality'] = 'Proof-Like'

    return coin


def _process_creators(coin):
    coin['authors']   = re.sub('.*:', '', str(coin['authors']))
    coin['sculptors'] = re.sub('.*:', '', str(coin['sculptors']))
    coin['minted_by'] = re.sub('.*:', '', str(coin['minted_by']))

    return coin


with open('out.json', 'r') as fin:
    coins = json.load(fin)


out_items = []

for coin in coins:
    coin = _process_material(coin)
    coin = _process_denomination(coin)
    coin = _process_characteristics(coin)
    coin = _process_mintage(coin)
    coin = _process_quality(coin)
    coin = _process_creators(coin)


    coin['denomination'] = {
        'value':    coin['denomination_value'],
        'currency': coin['denomination_currency']
    }

    coin.pop('denomination_value')
    coin.pop('denomination_currency')


    if (coin['authors']):
        coin['authors'] = (coin['authors']).strip()

        coin['authors'] = {
            'Obverse': [coin['authors']],
            'Reverse': [coin['authors']]
        }

    if (coin['sculptors']):
        coin['sculptors'] = (coin['sculptors']).strip()

        coin['sculptors'] = {
            'Obverse': [coin['sculptors']],
            'Reverse': [coin['sculptors']]
        }

    if (coin['minted_by']):
        coin['minted_by'] = (coin['minted_by']).strip()

    if (coin['image']):
        coin['image'] = {
            'Obverse': [coin['image'][0]],
            'Reverse': [coin['image'][-1]]
        }

    out_item = {
        "id":               coin['id'],
        "region":           coin['region'],
        "country":          coin['country'],
        "category":         coin['category'],
        "collection":       coin['collection'],
        "coin_family":      coin['coin_family'],
        "additional_name":  coin['additional_name'],
        "year":             coin['year'],
        "shape":            coin['shape'],
        "quality":          coin['quality'],
        "edge":             coin['edge'],
        "material":         coin['material'],
        "standard":         coin['standard'],
        "denomination":     coin['denomination'],
        "mintage":          coin['mintage'],
        "weight":           coin['weight'],
        "length":           coin['length'],
        "width":            coin['width'],
        "thickness":        coin['thickness'],
        "substyle_of":      coin['substyle_of'],
        "authors":          coin['authors'],
        "sculptors":        coin['sculptors'],
        "minted_by":        coin['minted_by'],
        "notes":            coin['note'],
        "images":           coin['image']
    }

    out_items.append(out_item)


with open('formatted_out.json', 'w') as fout:
    json.dump(out_items, fout, indent=4)
