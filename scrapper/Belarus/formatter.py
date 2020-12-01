import json


with open('out.json', 'r') as fin:
    data = json.load(fin)

out_items = []

for item in data:
    if (item['category']):
        item['category'] = (item['category']).strip()

    if (item['collection']):
        item['collection'] = (item['collection']).strip()

    if (item['year']):
        item['year'] = (item['year']).strip()

    if (item['material']):
        item['material'] = (item['material']).title()

    if (item['quality']):
        item['quality'] = (item['quality']).title()

    if (item['shape']):
        if (item['shape'] == 'Kruga'):
            item['shape'] = 'Round'

        item['shape'] = (item['shape']).title()

    if (item['edge']):
        if (item['edge'] == 'Riflenaia'):
            item['edge'] = 'Corrugated'

        item['shape'] = (item['shape']).title()

    if (item['denomination_value'] and item['denomination_currency']):
        if (item['denomination_currency'] == 'Ruble' or item['denomination_currency'] == 'Rubles'):
            item['denomination_currency'] = 'BYN'

        item['denomination'] = {
            'value':    item['denomination_value'],
            'currency': item['denomination_currency']
        }

        item.pop('denomination_value')
        item.pop('denomination_currency')

    if (item['authors']):
        item['authors'] = (item['authors']).strip()

        item['authors'] = {
            'Obverse': [item['authors']],
            'Reverse': [item['authors']]
        }

    if not (item['sculptors']):
        item['sculptors'] = []

    if (item['minted_by']):
        item['minted_by'] = (item['minted_by']).strip()

    if not (item['note']):
        item['note'] = []
    else:
        item['note'] = [item['note']]


    out_item = {
        "id":               item['id'],
        "region":           item['region'],
        "country":          item['country'],
        "category":         item['category'],
        "collection":       item['collection'],
        "coin_family":      item['coin_family'],
        "additional_name":  item['additional_name'],
        "year":             item['year'],
        "shape":            item['shape'],
        "quality":          item['quality'],
        "edge":             item['edge'],
        "material":         item['material'],
        "standard":         item['standard'],
        "denomination":     item['denomination'],
        "mintage":          item['mintage'],
        "weight":           item['weight'],
        "length":           item['length'],
        "width":            item['width'],
        "thickness":        item['thickness'],
        "substyle_of":      item['substyle_of'],
        "authors":          item['authors'],
        "sculptors":        item['sculptors'],
        "minted_by":        item['minted_by'],
        "notes":            item['note'],
        "images":           item['image']
    }

    out_items.append(out_item)


with open('formatted_out.json', 'w') as fout:
    json.dump(out_items, fout, indent=4)
