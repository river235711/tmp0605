#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import json
import requests
import stocktmp3
mylist=[]
dateList=['20210601','20210602','20210603','20210604','20210607']
stockNo=['2409','2002','2330']
#dateList=['20210603','20210604','20210607']
#stockNo=['8044']
#listx=stocktmp3.Get_Stock3big('2436',dateList[0])

#c=range(len(dateList))
d=len(dateList)
print("3big number diff")
for j in range(len(stockNo)):
    print("stock:",stockNo[j])
    for i in range(len(dateList)):
            if d==i+1:
                break
            a=0
            b=0
            listx=stocktmp3.Get_Stock3big(stockNo[j],dateList[i])
            listy=stocktmp3.Get_Stock3big(stockNo[j],dateList[i+1])
            #print(listx)
            a=float(listx['sum3big'])
            b=float(listy['sum3big'])
            print(">>",a,"(",dateList[i],"3big value )")
            print(">>",b,"(",dateList[i+1],"3big value )")
            print(">>",('%.2f' %(b/a)),"(= "+str(b)+"/"+str(a)+")")
            #print(i)

    
#a=float(listx['sum3big'])
#b=float(listy['sum3big'])
#print(a+b)
#
#mylist.append(a)
#mylist.append(b)
#
#print(mylist)
#
#for i in range(len(mylist)):
#    print(mylist[i])
