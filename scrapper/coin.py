'''

	Author: 	Eugene Moshchyn
	Description:
		- To store dimentions, if the coin is round, $_width will be used and $_length
		  will be held empty. Else, both hold propotions
		- If some coin value is unknown, hold "None"

	Comments:	Released

'''
from unidecode import unidecode


def _normalize(object):
	if object:
		if isinstance(object, str):
			return object.strip()

		else:
			return object

	return None


def _unicode(string: str):
	if string:
		return unidecode(string.strip())

	return None


def _normalize_notes(notes: list):
	formatted_list = []
	for note in notes:
		formatted_list.append( _unicode(note) )

	return formatted_list



class coin:
	def __init__(self):
		self.id						= 0
		self.region   				= ""
		self.country 				= ""
		self.category 				= ""
		self.collection 			= ""
		self.coin_family 			= ""

		#coin characteristics
		self.additional_name		= ""
		self.substyle_of			= None
		self.year					= -1

		self.material 				= ""
		self.standard		 		= -1.0
		self.mintage 				= -1
		self.quality 				= ""
		self.shape					= ""
		self.edge					= ""

		self.denomination_value 	= -1.0
		self.denomination_currency  = ""

		self.weight  				= -1.0
		self.length					= -1.0
		self.width					= -1.0
		self.thickness				= -1.0

		self.authors				= ""
		self.sculptors				= ""
		self.minted_by				= ""
		self.notes					= []
		self.images					= []

	def to_dict(self):
		return {
			"id":					 int(self.id),
			"region": 				 _unicode(self.region),
			"country": 				 _unicode(self.country),
			"category": 			 _unicode(self.category),
			"collection": 			 _unicode(self.collection),
			"coin_family": 			 _unicode(self.coin_family),

			"additional_name": 		 _unicode(self.additional_name),
			"substyle_of":			 self.substyle_of,
			"year":					 _unicode(self.year),


			"material": 			 _unicode(self.material),
			"standard": 			 float(self.standard),
			"mintage":  			 self.mintage,
			"quality":				 _unicode(self.quality),
			"shape":				 _unicode(self.shape),
			"edge":					 _unicode(self.edge),

			"denomination_value": 	 self.denomination_value,
			"denomination_currency": _unicode(self.denomination_currency),

			"weight": 				 _normalize(self.weight),
			"length": 				 _normalize(self.length),
			"width":				 _normalize(self.width),
			"thickness": 			 _normalize(self.thickness),

			"authors": 				 _unicode(self.authors),
			"sculptors": 			 _unicode(self.sculptors),
			"minted_by": 			 _unicode(self.minted_by),
			"note": 	 			 _normalize_notes(self.notes),
			"image": 				 self.images
		}
