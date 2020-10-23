import re
import filetype

import requests
from bs4 import BeautifulSoup

import CONST.URL
from CONST.coin import coin

import os


class BY_Scraper:
	def __init__(self):
		#to hold a SingleCoin
		self._coin = coin(region="Europe", country="Belarus")

		#creating a list to later store into DB
		self._coinList = []

	def _reSearch(self, patternToMatch, userString):
		patternFound = re.search(patternToMatch, str(userString))

		if not patternFound:
			return "NaN"

		return patternFound.group(1)

	def _replaceLast(self, source_string, replace_what, replace_with):
		head, _sep, tail = source_string.rpartition(replace_what)
		return head + replace_with + tail

	def _removeExcessiveContent(self, catalog):
		#getting rid of the unessessary stuff that causes the problems
		catalog = str(catalog)
		catalog = catalog.replace("<div id=\"result\">\n", "")
		catalog = self._replaceLast(catalog, "\n<hr/>\n</div>", "")
		catalog = catalog.replace("\n", "").replace("  ", ' ')
		catalog = catalog.replace("<br/>", ' ')

		#split into categories
		catalog = catalog.split("<hr/>")

		return catalog

	def _processCoinDescription(self, description):
		self._coin._year = ( description.p.span.text.split() )[-1]

		description.p.decompose()
		spans = description.find_all("span")

		#removing the <strong>
		for span in spans:
			span.strong.replace_with("")

		self._coin._author	   	= spans[0].text.replace('\n', "").lstrip()
		self._coin._mintedBy	= spans[1].text.replace('\n', "").lstrip()

	def _processShape(self, pBlock):
		self._coin._shape = self._reSearch(
											"(round|square|rectangular|oval)",
											pBlock
										  ).title()

	def _processCoinCharacterisitcs(self, description):
		coinContent = str(description)

		self._coin._material = self._reSearch("<strong>(.*)</strong>", coinContent)

		#look for Standard
		standard = self._reSearch("Alloy standard.*\: (.*)<", coinContent)
		self._coin._materialStandard = float(standard) if standard else None

		self._coin._denomination     = self._reSearch("Denomination: (.*)<", coinContent).title()

		#Generalizing the weight of the coin
		#In case of Oz units appearing
		mass 		          = float(self._reSearch("Weight.*: (.*)<",     coinContent))
		massUnits             = self._reSearch("Weight.*, (.*):",     coinContent)
		self._coin._mass      = mass
		self._coin._massUnits = massUnits

		#Title() for Capitalization
		self._coin._quality          = self._reSearch("Quality: \"(.*?)\"", coinContent).title()

		#print(re.search("Mintage,.*\: (\d+|\d{1,3}(,\d{3})*)(\.\d+)?",  coinContent).group(2 	))
		self._coin._mintage          = int(self._reSearch("Mintage.*? (\d{1,3}(,\d{3})*)", coinContent).replace(',', ''))


		if ( self._coin._shape == "Round"):
			diameter = self._reSearch("Diameter.*: (.*)<", coinContent)
			self._coin._dimentions = CONST.DIAMETER_SIGN + diameter

		else:
			dimentions = self._reSearch("([0-9]*[.][0-9]+.*[0-9]*[.][0-9]+)", coinCounter)
			self._coin._dimentions = dimentions

		self._coin._dimentionUnits = "mm"
		#smallSpan = card.find("span", {"class": "small"})
		#if smallSpan:
		#	print()

	def _processNotes(self, smallSpanBlock):
		if not smallSpanBlock:
			self._coin._notes = None
			return

		smallSpanBlock = smallSpanBlock.text


	def _printStatus(self, coinName, coinsProcessed):
		os.system("cls")
		print("Currently Processing:\t",  coinName)
		print("Total Coins Processed:\t", coinsProcessed)

	def _recordTheImages(self, imageBlock, descriptionBlock, coinID):
		#imageRootURL + img["scr"] = path to file
		imageRootURL = "http://www.nbrb.by/"

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

		if ( len(images) > 2 ):
			print(self._coin._coinName)
		'''
		for index, image in enumerate(images, start=1):

			if image["src"] not in imageWritten:
				imageWritten.append(image["src"])

				r = requests.get(imageRootURL + image["src"])
				extension = filetype.guess(r.content).extension

				coinPath = "img/{0}__{1}.{2}".format(coinID, index, extension)

				with open(coinPath, "wb") as f:
					f.write(r.content)

				pathToCoins.append(coinPath)
		'''
		self._coin._pathToCoin = pathToCoins

	def getCoins(self):
		#making the requests
		r    = requests.get(CONST.URL.BY_CATALOG_URL, headers=CONST.URL.USER_HEADERS)
		soup = BeautifulSoup(r.content, "html.parser")

		#find the Content of the table
		resultTable = soup.find("div", {"id": "result"})

		#get contents inbetween first <div ...>(.*)</div>
		listOfCategories = self._removeExcessiveContent( resultTable )

		#remove "My Country Belarus" Category
		listOfCategories.pop()

		#Keep track of the total coins
		#Also for image storing
		coinCounter = 0

		#loop for every category in the list
		for category in listOfCategories:
			#create a soup var for each one of them
			soup = BeautifulSoup(category, "html.parser")

			#coin Category
			self._coin._category = soup.h2.text

			#separate by collection
			collections = soup.find_all("div", {"class": "user-section"})

			coinCollection = soup.h2.text

			#loop for every collection to obtain info
			for collection in collections:

				#If the Collection Name == Category
				#Then its collection == None
				if (collection.previous_element != coinCollection):
					self._coin._collection = collection.previous_element

				#Get all <a> tags for the collection
				coins = collection.find_all("a")

				#for every coin in the block
				for coin in coins:
					self._coin._coinName = coin.text

					#make a request
					#link == href in <a>
					#coin["href"]
					r    = requests.get(CONST.URL.BY_BANK + coin["href"])
					soup = BeautifulSoup(r.content, "html.parser")

					#description = soup.find("div", {"class": "description-list"})


					#Shape and Description are the same for all Coins on Page
					#gets a particular <p> that contains coin(case-insensitive)
					#self._processShape( soup.main.find(text=re.compile("(?i)coin.*?is|are")) )

					#self._processCoinDescription(description)

					cards = soup.find_all("div", {"class": "coin-memory__item subject-card"})

					for card in cards:
						#self._processCoinCharacterisitcs(card.find("div", {"class": "subject-card__content"}))
						self._recordTheImages(imageBlock		= card.find("div", {"class": "subject-card__visual"}),
											  descriptionBlock  = card.find("div", {"class": "subject-card__content"}).find_all("img"),
											  coinID			= coinCounter)
						#self._processNotes(card.find("span", {"class": "small"}))

						#self._coinList.append(self._coin)

						coinCounter += 1
						
						#Output the Status
						#DEBUGGING PURPOSES ONLY
						#self._printStatus(self._coin._coinName, coinCounter)

						#print(self._coin)
						#print()

		return self._coinList
