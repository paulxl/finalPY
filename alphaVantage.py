#!/usr/bin/env python3
from time import strftime

import requests
import os

from datetime import date
import datetime
from datetime import timedelta


from dotenv import load_dotenv
load_dotenv()
tokenAV = os.environ.get("ALPHA_KEY")

STOCK = "AMZN"

def main():
    global STOCK

    today = datetime.date.today()
    print(today, "  today")
    aYearAgo = today - timedelta(366)

    print(aYearAgo," a year ago")
    todayMod = today.strftime("%Y-%m-%d")
    agoMod = aYearAgo.strftime("%Y-%m-%d")
    print(agoMod, "  agoMod")
    print(todayMod, "  todayMod")


    #req1 = requests.get(f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={STOCK}&apikey={tokenAV}").json()

    print(f"""
    {STOCK} closing bell prices:
    """)

   # a = (req2['Time Series (Daily)'])

   # print("   Date   ","     Closed  $ ", "    Volume")

   #for key in a.keys():
    #for key in a.keys():
        #print(type(key))
        #print (key,"    ", a[key]["4. close"], "    ", a[key]["5. volume"])

    req2 = requests.get(
        f"https://www.alphavantage.co/query?function=TIME_SERIES_Daily&symbol={STOCK}&outputsize=full&apikey={tokenAV}").json()


    b= (req2['Time Series (Daily)'])
    zKeys = []
    for key in b.keys():
        zKeys.append(key)

    todayClose = float(req2['Time Series (Daily)'][zKeys[0]]['4. close'])
    yearAgoClose = float(req2['Time Series (Daily)'][agoMod]['4. close'])
    difference = round((todayClose - yearAgoClose), 2)
    percentChange = round((yearAgoClose/todayClose)*100, 2)

    print("Last Open Market Closing ", req2['Time Series (Daily)'][zKeys[0]]['4. close'])
    print("Closed a year ago ", req2['Time Series (Daily)'][agoMod]['4. close'])
    print("Difference : ", difference," which means:  ", percentChange,"% change")





if __name__ == "__main__":
    main()