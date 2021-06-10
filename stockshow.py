#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import json
import requests
import stocktmp2
listx=stocktmp2.Get_Stock3big('2436','20210603')
listy=stocktmp2.Get_Stock3big('2436','20210604')
#stocktmp2.Get_Stock3big('2436','20210604')
#stocktmp2.Get_Stock3big('2436','20210603')
a=float(listx['sum3big'])
b=float(listy['sum3big'])
print(a+b)
