'''
    Author:     Eugene Moshchyn
    Description:
        - Temporary file to handle insertion into DB

    Comments:
        - Will be migrated from SQLite to MySQL
        - Need to get rid of the SELECT in INSERT
          by moving SELECT into separate function

'''

#
import testMain

import CONST.SERVER
import mysql.connector

mydb        = mysql.connector.connect(
                host   = CONST.SERVER.HOST,
                user   = CONST.SERVER.USERNAME,
                passwd = CONST.SERVER.PASSWORD
              )
mycursor    = mydb.cursor()

#mycursor.execute("CREATE DATABASE IF NOT EXISTS CoinCatalog")

userList    = testMain.populateList()

for coin in userList:
    #Inserting Region
    mycursor.execute("""INSERT INTO region (name)
                        VALUES (:name)
                        """, {"name": coin._region}
                    )

    #Inserting Country
    mycursor.execute("""INSERT INTO country (regionID, name)
                        VALUES
                        (
                            (SELECT id FROM region WHERE region.name = (:regionName)),
                            (:countryName)
                        )""", {"regionName":  coin._region,
                               "countryName": coin._country}
                    )

    #Inserting Category
    mycursor.execute("""INSERT INTO category (countryID, name)
                        VALUES
                        (
                            (SELECT id FROM country WHERE country.name = (:countryName)),
                            (:categoryName)
                        )""", {"countryName":  coin._country,
                               "categoryName": coin._category}
                    )

    #Inserting Collection
    mycursor.execute("""INSERT INTO collection (categoryID, name)
                        VALUES
                        (
                            (SELECT id FROM category WHERE category.name = (:categoryName)),
                            (:collectionName)
                        )""", {"categoryName":   coin._category,
                               "collectionName": coin._collection}
                     )

    #Inserting Material
    mycursor.execute("""INSERT INTO material (name)
                        VALUES (:name)
                        """, {"name": coin._material}
                    )

    #Inserting Minted By
    mycursor.execute("""INSERT INTO mintedBy (name)
                        VALUES (:name)
                        """, {"name": coin._mintedBy}
                    )


    #Inserting Author
    mycursor.execute("""INSERT INTO author (names)
                        VALUES (:name)
                        """, {"name": coin._author}
             )

    #Inserting Coin Quality
    mycursor.execute("""INSERT INTO quality (name)
                        VALUES (:name)
                        """, {"name": coin._quality}
                    )

    #Inserting Weight Units
    mycursor.execute("""INSERT INTO weightUnits (name)
                        VALUES (:name)
                        """, {"name": coin._weightUnits}
                    )

    #Inserting Coin Shape
    mycursor.execute("""INSERT INTO shape (name)
                        VALUES (:name)
                        """, {"name": coin._shape}
                    )

    #Inserting Size Units
    mycursor.execute("""INSERT INTO sizeUnits (name)
                        VALUES (:name)
                        """, {"name": coin._sizeUnits}
                    )

    mycursor.execute("""INSERT INTO notes (description)
                        VALUES (:description)
                        """, {"description": coin._notes}
                    )

    #SELECT FROM
    #RE-WORK
    #IF -- ELSE
    try:
        mycursor.execute("""INSERT INTO information (collectionID,
                                              name,
                                              materialID,
                                              materialStandard,
                                              mintage,
                                              denomination,
                                              weight,
                                              weightUnitsID,
                                              qualityID,
                                              shapeID,
                                              width,
                                              length,
                                              sizeUnitsID,
                                              year,
                                              authorID,
                                              mintedByID,
                                              notesID)
                     VALUES
                     (
                        (SELECT id FROM collection  WHERE collection.name   = (:collectionName)),
                        (:coinName),
                        (SELECT id FROM material    WHERE material.name     = (:materialName)),
                        (:materialStandard),
                        (:mintage),
                        (:denomination),
                        (:weight),
                        (SELECT id FROM weightUnits WHERE weightUnits.name  = (:weightUnitsName)),
                        (SELECT id FROM quality     WHERE quality.name      = (:qualityName)),
                        (SELECT id FROM shape       WHERE shape.name        = (:shapeName)),
                        (:width),
                        (:length),
                        (SELECT id FROM sizeUnits   WHERE sizeUnits.name    = (:sizeUnitsName)),
                        (:year),
                        (SELECT id FROM author      WHERE author.names      = (:authorName)),
                        (SELECT id FROM mintedBy    WHERE mintedBy.name     = (:mintedByName)),
                        (SELECT id from notes       WHERE notes.description = (:coinNotes))
                     )""", {"collectionName":       coin._collection,
                            "coinName":             coin._coinName,
                            "materialName":         coin._material,
                            "materialStandard":     coin._materialStandard,
                            "mintage":              coin._mintage,
                            "denomination":         coin._denomination,
                            "weight":               coin._weight,
                            "weightUnitsName":      coin._weightUnits,
                            "qualityName":          coin._quality,
                            "shapeName":            coin._shape,
                            "width":                coin._width,
                            "length":                coin.length,
                            "sizeUnitsName":        coin._sizeUnits,
                            "year":                 coin._year,
                            "authorName":           coin._author,
                            "mintedByName":         coin._mintedBy,
                            "coinNotes":            coin._notes
                           }
                 )

    except sqlite3.IntegrityError:
        print("Error Occured")
        '''
        mycursor.execute("""UPDATE information
                     SET
                     (
                        mintage             = (:mintage),
                        denomination        = (:denomination),
                        weight              = (:weight),
                        weightUnitsID       =
                        (
                            SELECT id FROM weightUnits  WHERE weightUnits.name =    (:weightUnits)
                        ),
                        qualityID           =
                        (
                            SELECT id FROM quality      WHERE quality.name =        (:quality)
                        ),
                        width               = (:width),
                        length              = (:length),
                        sizeUnitsID         =
                        (
                            SELECT id FROM sizeUnits    WHERE sizeUnits.name =      (:sizeUnits)
                        ),
                        authorID            =
                        (
                            SELECT id FROM author       WHERE author.names =        (:author)
                        ),
                        mintedByID          =
                        (
                            SELECT id FROM mintedBy     WHERE mintedBy.name =       (:mintedBy)
                        ),
                        notesID             =
                        (
                            SELECT id FROM notes        WHERE notes.description =   (:notes)
                        )
                     )
                     WHERE
                     (
                        collectionID        =
                        (
                            SELECT id FROM collection   WHERE collection.name =     (:collection)
                        ),
                        name                = (:coinName),
                        materialID          =
                        (
                            SELECT id FROM material     WHERE material.name =       (:material)
                        ),
                        materialStandard    = (:materialStandard),
                        shapeID             =
                        (
                            SELECT id FROM shape        WHERE shape.name =          (:shape)
                        ),
                        year                = (:year)
                     )
                 """, {"mintage":           coin._mintage,
                       "denomination":      coin._denomination,
                       "weight":            coin._weight,
                       "weightUnits":       coin._weightUnits,
                       "quality":           coin._quality,
                       "width":             coin._width,
                       "length":            coin.length,
                       "sizeUnits":         coin._sizeUnits,
                       "author":            coin._author,
                       "mintedBy":          coin._mintedBy,
                       "notes":             coin._notes,
                       "collection":        coin._collection,
                       "coinName":          coin._coinName,
                       "material":          coin._material,
                       "materialStandard":  coin._materialStandard,
                       "shape":             coin._shape,
                       "year":              coin._year
                      }
                 )
        '''
    #END OF INSERTION INTO information BLOCK

    #SELECT id of last processed element
    mycursor.execute("""SELECT id FROM information
                 WHERE
                 (
                    collectionID        =
                    (
                        SELECT id FROM collection   WHERE collection.name = (:collection)
                    ) AND
                    name                = (:coinName) AND
                    materialID          =
                    (
                        SELECT id FROM material     WHERE material.name = (:material)
                    ) AND
                    materialStandard    = (:materialStandard) AND
                    shapeID             =
                    (
                        SELECT id FROM shape        WHERE shape.name    = (:shape)
                    ) AND
                    year                = (:year)
                 )""", {"collection":       coin._collection,
                        "coinName":         coin._coinName,
                        "material":         coin._material,
                        "materialStandard": coin._materialStandard,
                        "shape":            coin._shape,
                        "year":             coin._year
                       }
             )

    lastProcessedCoinID = c.fetchone()

    for image in coin._pathToCoin:
        mycursor.execute("""INSERT INTO image (coinID, path)
                            VALUES ((:id), (:imagePath))
                            """, {"id":         lastProcessedCoinID,
                                  "imagePath":  image
                                 }
                        )
