#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#import pandas as pd
#import numpy as np
#import json
#import requests
import stocktmp3
from scipy.stats import linregress
from sklearn.preprocessing import normalize



def Get_Stock3bigCalcSlope(stockNo,dateList,slopeVth):
    d=len(dateList)
    re_listy=[]
    print("Day of 3big number slope and intercept:\n", dateList)
    for j in range(len(stockNo)):
        print("stock:",stockNo[j])
        regXList=[]
        regYList=[]
        regXListNorm=[]
        regYListNorm=[]
        listx=[]
        listy=[]
        for i in range(len(dateList)):
                if len(dateList)==i+1:
                    regYList.append(b)
                    regXList.append(i)
                    regYListNorm=normalize([regYList])
                    regXListNorm=normalize([regXList])
                    slope, intercept, r_value, p_value, std_err = linregress(regXList,regYListNorm)
                    slope=("%.5f" %slope)
                    slope=float(slope)
                    intercept=("%.5f" %intercept)
                    intercept=float(intercept)
                    print("slope:",slope,"intercept:",intercept)
                    break
                a=0
                b=0
                listx,StockNoAll=stocktmp3.Get_Stock3big(stockNo[j],dateList[i])
                listy,StockNoAll=stocktmp3.Get_Stock3big(stockNo[j],dateList[i+1])
                a=float(listx['sum3big'])
                b=float(listy['sum3big'])
                #print(">>",a,"(",dateList[i],"3big value )")
                #print(">>",b,"(",dateList[i+1],"3big value )")
                #print(">>",('%.2f' %(b/a)),"(= "+str(b)+"/"+str(a)+")")
                regYList.append(a)
                regXList.append(i)
                #print(i)
        if slope>slopeVth:
            re_listy.append(listy)
            re_listy.append(slope)
    return re_listy

if __name__ == '__main__':
    #dateList=['20210601','20210602','20210603','20210604','20210607','20210608','20210609','20210610']
    dateList=['20210603','20210604','20210607','20210608','20210609','20210610']
    stockNo=['0050','2330','006208','2609','2603']
    slopeVth=0
    #listtmp, stockNoAll=stocktmp3.Get_Stock3big('2330',dateList[0])
    #stockNoAllList=stockNoAll.values.tolist()
    data=Get_Stock3bigCalcSlope(stockNo,dateList,slopeVth)
    for list in data:
        print("Result: 3big normed slope >",slopeVth)
        print(list)

