# -*- coding: utf-8 -*-
"""
Created on Tue May  5 09:17:11 2020

@author: Vedat
"""
import schedule
import time
import urllib.request as url 

def job() :
    page = url.urlopen("https://tr.widgets.investing.com/live-currency-cross-rates?theme=lightTheme&cols=bid,changePerc&pairs=66,18")
    text = page.readlines()
    euro_alis = text[59]
    euro_satis = text[60]
    euro_fark = text[66]

    ealis_string=euro_alis.decode("utf-8")
    esatis_string=euro_satis.decode("utf-8")
    efark_string=euro_fark.decode("utf-8")


    euroalis=ealis_string[61:67]
    eurosatis=esatis_string[61:67]
    eurofarkrenk=efark_string[35:38]
    eurofark=efark_string[80:85]

    dolar_alis = text[75]
    dolar_satis = text[76]
    dolar_fark = text[82]


    dalis_string=dolar_alis.decode("utf-8")
    dsatis_string=dolar_satis.decode("utf-8")
    dfark_string=dolar_fark.decode("utf-8")

    dolaralis=dalis_string[61:67]
    dolarsatis=dsatis_string[61:67]
    dolarfarkrenk=dfark_string[35:38]
    dolarfark=dfark_string[80:85]

    if eurofarkrenk in ["red"]:
        eurofark=efark_string[79:85]
    else:
        eurofark=efark_string[81:87]
    
    if dolarfarkrenk in ["red"]:
        dolarfark=dfark_string[79:85]
    else:
        dolarfark=dfark_string[81:87]



    print('USD/TRY Alış: ' + str(dolaralis) + " Satış: " + str(dolarsatis) + " Günlük Fark: " + str(dolarfark)) 
    print('EUR/TRY Alış: ' + str(euroalis) + " Satış: " + str(eurosatis) + " Günlük Fark: " + str(eurofark)) 
schedule.every(0.5).minutes.do(job)
while True:
    schedule.run_pending()
    time.sleep(1)
