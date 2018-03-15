import pandas as pd
import time

def getCryptoData(currency, start_date, end_date):
    importUrl = "https://coinmarketcap.com/currencies/{currency}/historical-data/?start={start}&end={end}".format(
        currency=currency,
        start=start_date,
        end=end_date
    )

    print(importUrl)


    time.strftime("%Y%m%d")
