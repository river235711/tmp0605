#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import json
import requests
import os.path
#test#
def Get_Stock3big(stockNoFind,Date):
    if not os.path.isfile("./stocktmp3.rawdata/3big_"+Date+".txt"):
        url = f'https://www.twse.com.tw/fund/T86?response=json&date={Date}&selectType=ALL&'
        data = requests.get(url).text
        with open("./stocktmp3.rawdata/3big_"+Date+".txt", 'w') as outfile:
            json.dump(data, outfile)
    else:
        with open("./stocktmp3.rawdata/3big_"+Date+".txt") as json_file:
            data = json.load(json_file)
    json_data = json.loads(data)
    Stock_data = json_data['data']
    StockPrice = pd.DataFrame(Stock_data, columns = ['stockNo','stockName','buyWL','sellWL','sumWL','buyW','sellW','sumW','buyT','sellT','sumT','sumZ','buyZZ','sellZZ','sumZZ','buyZB','sellZB','sumZB','sum3big'])
    StockPrice['stockNo'] = StockPrice['stockNo'].str.replace('','').astype(str)
    StockPrice['stockName'] = StockPrice['stockName'].str.replace('','').astype(str)
    StockPrice['buyWL'] = StockPrice['buyWL'].str.replace(',','').astype(float)
    StockPrice['sellWL'] = StockPrice['sellWL'].str.replace(',','').astype(float)
    StockPrice['sumWL'] = StockPrice['sumWL'].str.replace(',','').astype(float)
    StockPrice['buyW'] = StockPrice['buyW'].str.replace(',','').astype(float)
    StockPrice['sellW'] = StockPrice['sellW'].str.replace(',','').astype(float)
    StockPrice['sumW'] = StockPrice['sumW'].str.replace(',','').astype(float)
    StockPrice['buyT'] = StockPrice['buyT'].str.replace(',','').astype(float)
    StockPrice['sellT'] = StockPrice['sellT'].str.replace(',','').astype(float)
    StockPrice['sumT'] = StockPrice['sumT'].str.replace(',','').astype(float)
    StockPrice['sumZ'] = StockPrice['sumZ'].str.replace(',','').astype(float)
    StockPrice['buyZZ'] = StockPrice['buyZZ'].str.replace(',','').astype(float)
    StockPrice['sellZZ'] = StockPrice['sellZZ'].str.replace(',','').astype(float)
    StockPrice['sumZZ'] = StockPrice['sumZZ'].str.replace(',','').astype(float)
    StockPrice['buyZB'] = StockPrice['buyZB'].str.replace(',','').astype(float)
    StockPrice['sellZB'] = StockPrice['sellZB'].str.replace(',','').astype(float)
    StockPrice['sumZB'] = StockPrice['sumZB'].str.replace(',','').astype(float)
    StockPrice['sum3big'] = StockPrice['sum3big'].str.replace(',','').astype(float)
    StockPrice = StockPrice[['stockNo','sum3big']]
    StockPriceSome = StockPrice[StockPrice['stockNo'].str.match(pat=stockNoFind+'$', case=True)]
    return StockPriceSome
if __name__ == '__main__':
    stockNoFindprint='2330'
    datePrint='20210602'
    data = Get_Stock3big(stockNoFindprint,datePrint)
    #print(data)
