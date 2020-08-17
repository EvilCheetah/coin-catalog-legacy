'''
	Author:		Eugene Moshchyn
	Description:
		- File holds templates of the coins

	Comments: To Be Deleted
'''


from essentials.coin import coin

def populateList():
	coinList = []
	coinList.append(coin(region 					= "Europe",
							country 				= "Belarus",
							category 				= "Belarus and the World Community",
							collection 				= "NaN",
							coin_name 				= "50th Anniversary of UN",
							material 				= "Gold",
							material_standard 		= "916.7",
							mintage 				= 5000,
							denomination 			= "1 ruble",
							weight	  				= 8.71,
							weightUnits				= "g",
							quality 				= "Proof",
							shape					= "Round",
							width					= 105.0,
							sizeUnits				= "mm",
							author					= "A.Zimenko, D.Belitsky (Belarus)",
							minted_by				= "The Royal Mint, London,Great Britain",
							year					= 1996,
							path_to_coin			= ['img/0__1.gif', 'img/0__2.gif']
					))

	coinList.append(coin(region 					= "Europe",
							country 				= "Belarus",
							category 				= "Belarus and the World Community",
							coin_name 				= "50th Anniversary of UN",
							material 				= "Gold",
							material_standard 		= "916.7",
							mintage 				= 3000,
							denomination 			= "1 ruble",
							weight	  				= 8.71,
							weightUnits				= "g",
							quality 				= "Proof",
							shape					= "Round",
							width					= 105.0,
							sizeUnits				= "mm",
							author					= "A.Zimenko, D.Belitsky (Belarus)",
							minted_by				= "The Royal Mint, London,Great Britain",
							year					= 1996,
							path_to_coin			= ['img/0__1.gif', 'img/0__2.gif']
					))

	coinList.append(coin(region 			    = "Europe",
							country 				= "Belarus",
							category 				= "Belarus and the World Community",
							coin_name 				= "50th Anniversary of UN",
							material 				= "Silver",
							material_standard 		= "925.0",
							mintage 				= 20000,
							denomination 			= "1 ruble",
							weight	  				= 30.57,
							weightUnits				= "g",
							quality 				= "Proof",
							shape					= "Square",
							width				 	= 35.0,
							length					= 35.0,
							sizeUnits			 	= "mm",
							author					= "A.Zimenko, D.Belitsky (Belarus)",
							minted_by				= "The Royal Mint, London,Great Britain",
							year					= 1996,
							path_to_coin			= ['img/0__1.gif', 'img/0__2.gif']
					))

	coinList.append(coin(region 			= "Europe",
							country 				= "Belarus",
							category 				= "Belarus and the World Community",
							collection 				= "NaN",
							coin_name 				= "50th Anniversary of UN",
							material 				= "Copper–Nickel",
							mintage 				= 40000,
							denomination 			= "1 ruble",
							weight	 				= 28.28,
							weightUnits				= "g",
							quality 				= "Brilliant–Uncirculated",
							shape					= "Round",
							width					= 38.61,
							sizeUnits				= "mm",
							author					= "A.Zimenko, D.Belitsky (Belarus)",
							minted_by				= "The Royal Mint, London,Great Britain",
							year					= 1996,
							path_to_coin			= ['img/2__1.gif', 'img/2__2.gif']
					))

	return coinList
