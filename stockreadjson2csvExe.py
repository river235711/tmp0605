#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import json
import requests
import stockreadjson2csv
import os.path
import csv
def check_if_exists(x, ls):
    if x in ls:
        return x
dateList=['20210601','20210602']
stockNo=['2409']
#d=len(dateList)
#bigValue =0
print("1. get csv from url ...")
for i in range(len(dateList)):
    if not os.path.isfile("3big_"+dateList[i]+".csv"):
        data=stockreadjson2csv.Get_Stock3big(dateList[i])
        np.savetxt("3big_"+dateList[i]+".csv",data,delimiter =",", fmt ='% s')
        
print("2. show 3big and calc diff ...")
for j in range(len(stockNo)):
    for i in range(len(dateList)):
        with open("3big_"+dateList[i]+".csv", newline='') as f:
            reader = csv.reader(f)
            data = list(reader)
            print(data)
            findOne=check_if_exists(['3481', '-65733146', '群創            '],data)
            print(findOne)
            
