'''
    Author:     Eugene Moshchyn
    Description:
        - This file is used to hold necessary data
          for scraping or other data in order to scrape

'''

#Browser header to go around bot check
USER_HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36 OPR/72.0.3815.320'}


#Belarus
BY_BANK = 'http://www.nbrb.by/engl/'
BY_CATALOG_URL = 'http://www.nbrb.by/engl/coinsbanknotes/coins/commemorative/catalog'

#Russia
RU_IMAGE_ROOT_URL = 'http://cbr.ru/'
RU_CATALOG_URL    = 'http://cbr.ru/eng/cash_circulation/memorable_coins/'
RU_COIN_BASE_URL  = 'http://cbr.ru/eng/cash_circulation/memorable_coins/coins_base/'

#United States
US_CATALOG_URL = 'https://www.usmint.gov/'

#Poland
#Look Further
PO_CATALOG_URL = 'https://www.nbp.pl/homen.aspx?f=/en/banknoty/banknoty_i_monety.html'
