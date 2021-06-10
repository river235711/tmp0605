#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#import pandas as pd
#import numpy as np
#import json
#import requests
import stocklist3
#import sys

dateList=['20210601',
          '20210602',
          '20210603',
          '20210604',
          '20210607',
          '20210608',
          '20210609',
          '20210610']
    
stockNo=['2330',
         '0050',
         '006208',
         '2454',
         '2603',
         '2609',
         '1101',
         '2002',
         '2610',
         '2618']
slopeVth=0
    #listtmp, stockNoAll=stocktmp3.Get_Stock3big('2330',dateList[0])
    #stockNoAllList=stockNoAll.values.tolist()
dateListIn=dateList[-6:]
data=stocklist3.Get_Stock3bigCalcSlope(stockNo,dateListIn,slopeVth)
for list in data:
    print("Result: 3big normed slope >",slopeVth)
    print(list)
with open("stocktmp3.output/"+str(int(dateList[-1:][0]))+"latest"+str(len(dateListIn))+".txt", 'w') as f:
    print(data, file=f) 
#f = open("stocktmp3.output/"+str(int(dateList[-1:][0]))+".txt", 'w')
#sys.stdout = f
#print(data)
#f.close()