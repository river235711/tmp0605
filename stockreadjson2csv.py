#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import json
import requests

def Get_Stock3big(Date):

    url = f'https://www.twse.com.tw/fund/T86?response=json&date={Date}&selectType=ALL&'
    data = requests.get(url).text
    json_data = json.loads(data)
    Stock_data = json_data['data']
    StockPrice = pd.DataFrame(Stock_data, columns = ['stockNo','stockName','buyWL','sellWL','sumWL','buyW','sellW','sumW','buyT','sellT','sumT','sumZ','buyZZ','sellZZ','sumZZ','buyZB','sellZB','sumZB','sum3big'])
    StockPrice['stockNo'] = StockPrice['stockNo'].str.replace('','').astype(str)
    #StockPrice['Date'] = pd.to_datetime(StockPrice['Date'].astype(str))
    StockPrice['stockName'] = StockPrice['stockName'].str.replace('','').astype(str)
    StockPrice['buyWL'] = StockPrice['buyWL'].str.replace(',','').astype(int)
    StockPrice['sellWL'] = StockPrice['sellWL'].str.replace(',','').astype(int)
    StockPrice['sumWL'] = StockPrice['sumWL'].str.replace(',','').astype(int)
    StockPrice['buyW'] = StockPrice['buyW'].str.replace(',','').astype(int)
    StockPrice['sellW'] = StockPrice['sellW'].str.replace(',','').astype(int)
    StockPrice['sumW'] = StockPrice['sumW'].str.replace(',','').astype(int)
    StockPrice['buyT'] = StockPrice['buyT'].str.replace(',','').astype(int)
    StockPrice['sellT'] = StockPrice['sellT'].str.replace(',','').astype(int)
    StockPrice['sumT'] = StockPrice['sumT'].str.replace(',','').astype(int)
    StockPrice['sumZ'] = StockPrice['sumZ'].str.replace(',','').astype(int)
    StockPrice['buyZZ'] = StockPrice['buyZZ'].str.replace(',','').astype(int)
    StockPrice['sellZZ'] = StockPrice['sellZZ'].str.replace(',','').astype(int)
    StockPrice['sumZZ'] = StockPrice['sumZZ'].str.replace(',','').astype(int)
    StockPrice['buyZB'] = StockPrice['buyZB'].str.replace(',','').astype(int)
    StockPrice['sellZB'] = StockPrice['sellZB'].str.replace(',','').astype(int)
    StockPrice['sumZB'] = StockPrice['sumZB'].str.replace(',','').astype(int)
    StockPrice['sum3big'] = StockPrice['sum3big'].str.replace(',','').astype(int)
    
    #StockPriceSomeA = StockPrice[StockPrice['stockNo'].str.match(pat=stockNoFind+'$', case=True)]
    #StockPriceSomeValueA = StockPriceSomeA['sum3big'].astype(float)
    #print(StockPriceSomeValueA)
    
    #StockPrice = StockPrice.set_index('stockName', drop = False)


    StockPrice = StockPrice[['stockNo','sum3big','stockName']]
    #print(StockPrice)
    #return StockPrice
    #stockNoFind='2002'
    #StockPriceSome = StockPrice[StockPrice['stockNo'].str.match(pat=stockNoFind+'$', case=True)]
    #StockPriceSomeValue = StockPriceSomeA['sum3big'].astype(float)
    #print(Date)
    #print(StockPriceSome)
    return StockPrice
if __name__ == '__main__':
    datePrint='20210602'
    data = Get_Stock3big(datePrint)
    np.savetxt("3big_"+datePrint+".csv",data,delimiter =",", fmt ='% s')

