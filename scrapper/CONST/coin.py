'''

	Author: 	Eugene Moshchyn
	Description:
		- To store dimentions, if the coin is round, $_width will be used and $_length
		  will be held empty. Else, both hold propotions
		- If some coin value is unknown, hold "None"

	Comments:	Released

'''


from . import CHAR

class coin:
	def __init__(self,
				 region 				= "None",
				 country 				= "None",
				 category 				= "None",
				 collection 			= "None",
				 coin_name 				= "None",
				 material 				= "None",
				 material_standard 		= "None",
				 mintage 				= "None",
				 denomination 			= "None",
				 weight	  				= "None",
				 weightUnits			= "None",
				 quality 				= "None",
				 shape					= "None",
				 width					= "None",
				 length					= "None",
				 sizeUnits				= "None",
				 author					= "None",
				 minted_by				= "None",
				 year					= "None",
				 notes					= "None",
				 path_to_coin			= "None"
				 ):

		self._region   				= region
		self._country 				= country
		self._category 				= category
		#or Series
		self._collection 			= collection

		#coin characteristics
		self._coinName 				= coin_name
		self._material 				= material
		self._materialStandard 		= material_standard
		self._mintage 				= mintage
		self._denomination 			= denomination
		self._weight  				= weight
		self._weightUnits			= weightUnits
		self._quality 				= quality
		self._shape					= shape
		self._width					= width
		self._length				= length
		self._sizeUnits				= sizeUnits
		self._author				= author
		self._mintedBy				= minted_by
		self._year					= year
		self._notes					= notes
		self._pathToCoin			= [] if not path_to_coin else path_to_coin

	#For DB storage
	@property
	def length(self):
		if (self._length == "None"):
			return -1

		return self._length

	#returns properly formated weight
	@property
	def coinWeight(self):
		return "{0._weight} {0._weightUnits}".format(self)

	#returns dimentions based on shape
	@property
	def dimentions	(self):
		if (self._shape == "Round"):
			return "{1} {0._width} {0._sizeUnits}".format(self, CHAR.DIAMETER_SIGN)
		else:
			return "{0._width} {1} {0._length} {0._sizeUnits}".format(self, CHAR.X_by_Y)

	#used for console Debug
	def __str__(self):
		return ("Region:\t\t\t{0._region}\n"
				"Country:\t\t{0._country}\n"
				"Category:\t\t{0._category}\n"
				"Collection:\t\t{0._collection}\n"
				"Name:\t\t\t{0._coinName}\n"
				"Material:\t\t{0._material}\n"
				"Standard:\t\t{0._materialStandard}\n"
				"Mintage:\t\t{0._mintage:,}\n"
				"Denomination:\t\t{0._denomination}\n"
				"Weight:\t\t\t{0.coinWeight}\n"
				"Quality:\t\t{0._quality}\n"
				"Shape:\t\t\t{0._shape}\n"
				"Dimentions:\t\t{0.dimentions}\n"
				"Designed By:\t\t{0._author}\n"
				"Minted By:\t\t{0._mintedBy}\n"
				"Year:\t\t\t{0._year}\n"
				"Notes:\t\t\t{0._notes}\n"
				"Path:\t\t\t{0._pathToCoin}").format(self)
