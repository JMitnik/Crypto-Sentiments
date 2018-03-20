import CreateDataService
import BitcoinService
import re
import time

START_DATE = "2017-09-01T22:10:00.000Z"
END_DATE = "2017-12-10T23:20:00.000Z"
REGEX_DAY_PATTERN = '(.*)T'
NR_TWEETS=8000
SOURCE = "lg"

CreateDataService.createData(START_DATE, END_DATE, NR_TWEETS, SOURCE)
(btc_start_date, btc_end_date) = BitcoinService.get_coinmarketcap_date_range(START_DATE, END_DATE)
btc = BitcoinService.get_bitcoin_values(btc_start_date, btc_end_date)
CreateDataService.createBitcoinData(btc, SOURCE)
