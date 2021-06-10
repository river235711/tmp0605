#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#import pandas as pd
#import numpy as np
#import json
#import requests
import stocklist3

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
data=stocklist3.Get_Stock3bigCalcSlope(stockNo,dateList[-4:],slopeVth)
for list in data:
    print("Result: 3big normed slope >",slopeVth)
    print(list)

