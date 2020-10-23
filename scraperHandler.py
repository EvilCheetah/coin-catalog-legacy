'''

	Author:		Eugene Moshchyn
	Description:
		- This class is used to handle:
			* Creating DB
			* Insertion into DB
			* Handling errors and doublicates

	Comments: Done with Init

'''

import mysql.connector
import CONST.SERVER


class coinConnector():
	def __init__(self):
		self._coinList 	= []
		self.mydb     	= mysql.connector.connect(
								host = CONST.SERVER.HOST,
								user = CONST.SERVER.USERNAME,
								passwd = CONST.SERVER.PASSWORD,
								database = CONST.SERVER.DATABASE
						  )
		self.mycursor	= self.mydb.cursor()

		self.initalizeTable()

	#function that creates all necessary tables
	def initalizeTable(self):
		self.mycursor.execute("""CREATE TABLE IF NOT EXISTS region
								(
									id 		SMALLINT UNSIGNED NOT NULL,
									name 	VARCHAR(255)	  NOT NULL,

									PRIMARY KEY (id),
									UNIQUE (name)
								)""")

		self.mycursor.execute("""CREATE TABLE IF NOT EXISTS country
								(
									id 			SMALLINT UNSIGNED NOT NULL,
									regionID 	SMALLINT UNSIGNED NOT NULL,
									name 		VARCHAR(255)	  NOT NULL,

									PRIMARY KEY (id),
									FOREIGN KEY (regionID) REFERENCES region(id),
									UNIQUE (regionID, name)
								)""")

		self.mycursor.execute("""CREATE TABLE IF NOT EXISTS category
								(
									id 			BIGINT 	 UNSIGNED NOT NULL,
									countryID	SMALLINT UNSIGNED NOT NULL,
									name 		VARCHAR(255)	  NOT NULL,

									PRIMARY KEY (id),
									FOREIGN KEY (countryID) REFERENCES country(id),
									UNIQUE (countryID, name)
								)""")

		self.mycursor.execute("""CREATE TABLE IF NOT EXISTS collection
								(
									id 			BIGINT UNSIGNED NOT NULL,
									categoryID 	BIGINT UNSIGNED NOT NULL,
									name 		VARCHAR(255)	NOT NULL,

									PRIMARY KEY (id),
									FOREIGN KEY (categoryID) REFERENCES category(id),
									UNIQUE (categoryID, name)
							   	)""")

		self.mycursor.execute("""CREATE TABLE IF NOT EXISTS material
								(
									id 		INT UNSIGNED NOT NULL,
									name 	VARCHAR(255),

									PRIMARY KEY (id),
									UNIQUE (name)
								)""")

		self.mycursor.execute("""CREATE TABLE IF NOT EXISTS mintedBy
								(
									id 		BIGINT UNSIGNED NOT NULL,
									name 	VARCHAR(255),

									PRIMARY KEY (id),
									UNIQUE (name)
								)""")

		self.mycursor.execute("""CREATE TABLE IF NOT EXISTS author
								(
									id 		BIGINT UNSIGNED NOT NULL,
									names 	VARCHAR(255),

									PRIMARY KEY (id),
									UNIQUE (names)
								)""")

		self.mycursor.execute("""CREATE TABLE IF NOT EXISTS quality
								(
									id		INT UNSIGNED NOT NULL,
									name 	VARCHAR(255),

									PRIMARY KEY (id),
									UNIQUE (name)
								)""")

		self.mycursor.execute("""CREATE TABLE IF NOT EXISTS weightUnits
								(
								  	id 		SMALLINT UNSIGNED NOT NULL,
									name 	VARCHAR(255),

									PRIMARY KEY (id),
									UNIQUE (name)
							 	)""")

		self.mycursor.execute("""CREATE TABLE IF NOT EXISTS shape
								(
									id 		SMALLINT UNSIGNED NOT NULL,
									name	VARCHAR(255),

									PRIMARY KEY (id),
									UNIQUE (name)
								)""")

		self.mycursor.execute("""CREATE TABLE IF NOT EXISTS sizeUnits
								(
									id 		SMALLINT UNSIGNED NOT NULL,
									name	VARCHAR(255),

									PRIMARY KEY (id),
									UNIQUE (name)
								)""")

		self.mycursor.execute("""CREATE TABLE IF NOT EXISTS notes
								(
									id 				BIGINT UNSIGNED NOT NULL,
									description 	VARCHAR(255),

									PRIMARY KEY (id),
									UNIQUE(description)
								)""")

		self.mycursor.execute("""CREATE TABLE IF NOT EXISTS coin
								(
									id 					BIGINT UNSIGNED NOT NULL,
									collectionID 		BIGINT UNSIGNED NOT NULL,
									name 				VARCHAR(255) 	NOT NULL,

									year 				INT,
									authorID 			BIGINT UNSIGNED NOT NULL,
									mintedByID 			BIGINT UNSIGNED NOT NULL,

									PRIMARY KEY (id),

									FOREIGN KEY (collectionID)  REFERENCES collection(id),
									FOREIGN KEY (authorID)		REFERENCES author(id),
									FOREIGN KEY (mintedByID)	REFERENCES mintedBy(id),

									UNIQUE
									(
										collectionID,
										name,
										year
									)
								)""")

		self.mycursor.execute("""CREATE TABLE IF NOT EXISTS style
								 (
								 	id					BIGINT UNSIGNED NOT NULL,
									coinID				BIGINT UNSIGNED NOT NULL,

									materialID			INT UNSIGNED NOT NULL,
									materialStandard	VARCHAR(255),
									mintage				INT,
									denomination		VARCHAR(255),

									weight				DOUBLE,
									weightUnitsID		SMALLINT UNSIGNED,

									qualityID			INT UNSIGNED NOT NULL,
									shapeID				SMALLINT UNSIGNED NOT NULL,

									width				DOUBLE,
									length				DOUBLE,
									sizeUnitsID			SMALLINT UNSIGNED,

									notesID				BIGINT UNSIGNED,

									PRIMARY KEY (id),

									FOREIGN KEY (coinID) 		REFERENCES coin(id),
									FOREIGN KEY (materialID)	REFERENCES material(id),
									FOREIGN KEY (weightUnitsID)	REFERENCES weightUnits(id),
									FOREIGN KEY (qualityID)		REFERENCES quality(id),
									FOREIGN KEY (shapeID)		REFERENCES shape(id),
									FOREIGN KEY (sizeUnitsID)	REFERENCES sizeUnits(id),
									FOREIGN KEY (notesID)		REFERENCES notes(id)

									UNIQUE
									(
										coinID,
										materialID,
										materialStandard,
										denomination,
										shapeID,
										qualityID
									)
								 )""")

		self.mycursor.execute("""CREATE TABLE IF NOT EXISTS image
								(
									styleID 	BIGINT UNSIGNED NOT NULL,
									path		VARCHAR(255),

									FOREIGN KEY (styleID) REFERENCES style(id),
									UNIQUE (sty, path)
								)""")

	def updateList(self):
		#self._coinList = BY_Scraper().getCoins()
		pass

	def processCoins(self):
		while ( self._coinList ):
			continue

	def main():
		while( True ):
			if not self._coinList:
				self.updateList()

			else:
				self.processCoins()
