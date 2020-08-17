'''

	Author:		Eugene Moshchyn
	Description:
		- int main()

'''

from scraperHandler import DB_Handler
#from scrapers.BY import BY_Scraper

if __name__ == '__main__':
	try:
		DB_Handler()
		#BY_Scraper().getCoins()

	except KeyboardInterrupt:
		print("Program Terminated")
