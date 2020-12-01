import re
import filetype
import json
import time
from unidecode import unidecode

import requests
from bs4 import BeautifulSoup

from scrapper import URL
from scrapper.coin import coin


def _search_a_string_for_pattern(patternToMatch, userString):
	patternFound = re.search(patternToMatch, str(userString))

	if not patternFound:
		return None

	return patternFound.group(1)


def _replaceLast(source_string, replace_what, replace_with):
	"""
	Replaces the last matched item in the string
	"""
	head, _sep, tail = source_string.rpartition(replace_what)
	return head + replace_with + tail


def _get_categories(catalog):
	"""
	This function gets the content of div block, splits catalog
	into categories and returns a list of categories
	"""
	#Removing <div>
	catalog = str(catalog)
	catalog = catalog.replace("<div id=\"result\">\n", "")
	catalog = _replaceLast(catalog, "\n<hr/>\n</div>", "")
	catalog = catalog.replace("\n", "").replace("  ", ' ')
	catalog = catalog.replace("<br/>", ' ')

	#Splitting into categories
	catalog = catalog.split("<hr/>")

	return catalog


def _get_coin_shape(sentence):
	return _search_a_string_for_pattern(
				"(round|square|rectangular|oval|круга)",
				sentence
			).title()


def _get_coin_edge(sentence):
	return _search_a_string_for_pattern(
				"(grained|reeded|corrugated|plain|inscription|рифленая|ribbed)",
				sentence
			).title()


def _get_coin_header_information(coin, description):
	coin.year = description.p.span.text

	description.p.decompose()
	spans = description.find_all("span")

	#removing the <strong>
	for span in spans:
		span.strong.replace_with("")

	coin.authors	= str(spans[0].text.replace('\n', "")).lstrip()
	coin.sculptors  = None
	coin.minted_by	= str(spans[1].text.replace('\n', "")).lstrip()

	return coin


def _get_coin_style_description(coin, description):
	coin_content = str(description)

	coin.material = str(_search_a_string_for_pattern("<strong>(.*)</strong>", coin_content))

	#look for Standard
	standard      = _search_a_string_for_pattern("Alloy standard.*\: (.*)<", coin_content)
	coin.standard = float(standard) if standard else -1.0

	denomination = _search_a_string_for_pattern("Denomination: (.*)<", coin_content).title()
	coin.denomination_value, coin.denomination_currency = denomination.split()

	#Generalizing the weight of the coin
	#In case of Oz units appearing
	coin.weight	= float(_search_a_string_for_pattern("Weight.*: (.*)<", coin_content))

	#Title() for Capitalization
	coin.quality = str(_search_a_string_for_pattern("Quality: \"(.*?)\"", coin_content).title())

	#print(re.search("Mintage,.*\: (\d+|\d{1,3}(,\d{3})*)(\.\d+)?",  coin_content).group(2 	))
	coin.mintage = int(_search_a_string_for_pattern("Mintage.*? (\d{1,3}(,\d{3})*)", coin_content).replace(',', ''))

	return coin


def _get_coin_dimentions(coin, body_block, small_block):
	if ( coin.shape == "Round"):

		diameter = _search_a_string_for_pattern("Diameter.*: (.*)<", str(body_block))
		coin.length = float(diameter)
		coin.width  = -1.0
		coin.thickness = -1.0

	else:
		dimentions = _search_a_string_for_pattern("([0-9]*[.][0-9]+.*[0-9]*[.][0-9]+)", str(small_block))

		if dimentions:
			#Convert to ASCII
			dimentions = unidecode(dimentions)
			#Split into Length and Width by ' x '
			dimentions = dimentions.split(' x ')

			#If didn't split => 'kh'(Russ. 'Х') used
			if len(dimentions) == 1:
				dimentions = ( dimentions[0] ).split('kh')

			length = dimentions[0]
			width  = dimentions[-1]

			coin.length = float(length)
			coin.width  = float(width)

		else:
			coin.length, coin.width = -1.0, -1.0

	coin.thickness = -1.0

	return coin


def _find_footer_description(main_body_block):
	p_blocks = main_body_block.find_all('p')
	for block in p_blocks:
		if ( ('round'  		in str(block)) or
			 ('square' 		in str(block)) or
			 ('rectangular' in str(block)) or
			 ('oval' 		in str(block)) or
			 ('круга'		in str(block))
		   ):

			 return block

	return None

def _get_coin_notes(smallSpanBlock):
	if smallSpanBlock:
		return smallSpanBlock.text

	return None


def _record_coin_images(imageBlock, descriptionBlock, coinID):
	#To keep track of the images
	#The flaw in design that dublicates
	#the same pics
	imageWritten = []

	#To keep the track of paths
	pathToCoins  = []

	images = imageBlock.find_all("img")

	if descriptionBlock:
		with open("additionalStyles.txt", 'a') as f:
			f.write(str(coinID) + '\n')
			for i in descriptionBlock:
				f.write('\t' + i["src"] + '\n')

		images = images + descriptionBlock

	for index, image in enumerate(images, start=1):

		if image["src"] not in imageWritten:
			imageWritten.append(image["src"])

			r = requests.get("http://www.nbrb.by/" + image["src"])
			extension = filetype.guess(r.content).extension

			coinPath = "img/{0}__{1}.{2}".format(coinID, index, extension)

			with open(coinPath, "wb") as f:
				f.write(r.content)

			pathToCoins.append(coinPath)

	return pathToCoins


def main():
	"""
	This Function gets the list of all coins listed on the website
	"""

	start_time = time.monotonic()

	COIN = coin()

	#Sets Region and Country
	COIN.region  = "Europe"
	COIN.country = "Belarus"

	#Array for all the coins in catalog
	COIN_LIST = []

	#Used for storing the images and for JSON File
	#Used for substyle
	coin_counter = 1

	#Get the webpage
	r    = requests.get(URL.BY_CATALOG_URL, headers=URL.USER_HEADERS)
	soup = BeautifulSoup(r.content, "html.parser")

	#Obtain the block with coins
	#Block has 'id'='result'
	CoinCatalog = soup.find("div", {"id": "result"})

	#Get the list of categories
	categories = _get_categories( CoinCatalog )

	#Removes "My Country Belarus" Category
	categories.pop()

	for category in categories:
		#Create soup Object for a single Category
		soup = BeautifulSoup(category, "html.parser")

		#Category is equal to <h2> Block
		COIN.category = soup.h2.text

		#"user-section" = Coin Collection
		collections = soup.find_all("div", {"class": "user-section"})

		#loop for every collection to obtain info
		for collection in collections:
			#If Coin Collection == <h2> Block
			#	Then Collection = NULL
			#Else
			#	Collection is Previous block
			if (collection.previous_element == COIN.category):
				COIN.collection = None
			else:
				COIN.collection = collection.previous_element

			#Coins are <a> Blocks
			coin_families = collection.find_all("a")

			for coin_family in coin_families:
				COIN.coin_family = coin_family.text
				print('Currently Processing: ', COIN.coin_family)

				#Get a Single Coin
				r    = requests.get(URL.BY_BANK + coin_family["href"])
				soup = BeautifulSoup(r.content, "html.parser")

				#Get Top Description Block
				#Has the Information about:
				#	Year, Authors/Sculptors and Minted_By
				coin_header_description = soup.find("div", {"class": "description-list"})

				#Get Middle Description Block
				#Has the Information about:
				#	Material, Denomination, Weight and etc.
				#AKA coins
				coin_styles = soup.find("div", {"class": "user-section"}).find_all('div', {'class': 'coin-memory__item subject-card'})

				#Get Footer Description Block
				#Has the Information about:
				#	Shape and Edge Style
				#Get the <main> block and then finds the <p> with
				#sentence with "edge"-word in it
				#coin_footer_description = soup.find('main').find(text=re.compile("(?i)([^.]*?edge[^.]*)")).string

				main_body = soup.find('main')

				coin_footer_description = _find_footer_description(main_body)

				#Get the Shape and Edge
				COIN.shape = _get_coin_shape(coin_footer_description)
				COIN.edge  = _get_coin_edge(coin_footer_description)

				COIN = _get_coin_header_information(COIN, coin_header_description)

				for coin_style in coin_styles:
					COIN.id     = coin_counter
					COIN        = _get_coin_style_description(COIN, coin_style.find('div', {'class': 'subject-card__widget'}))
					COIN.images = _record_coin_images(imageBlock	   = coin_style.find("div", {"class": "subject-card__visual"}),
				   		  			  			      descriptionBlock = coin_style.find("div", {"class": "subject-card__content"}).find_all("img"),
				   		  			  			      coinID		   = coin_counter)
					COIN = _get_coin_dimentions(COIN, coin_style.find('div', {'class': 'subject-card__widget'}), coin_style.find("span", {"class": "small"}))
					COIN.notes  = _get_coin_notes(coin_style.find("span", {"class": "small"}))

					COIN_LIST.append(COIN)

					coin_counter += 1

					with open("out.json", 'a') as fout:
						json.dump(COIN.to_dict(), fout)
						fout.write(',\n')


	print(f'Time elapsed: {time.monotonic() - start_time}')

	return COIN_LIST



if __name__ == '__main__':
	try:
		main()

	except KeyboardInterrupt:
		print("Program got terminated!")
