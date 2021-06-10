#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 09:58:08 2021

@author: will
"""
from statistics import mean
import numpy as np
from scipy.stats import linregress
def best_fit_slope(xs,ys):
    m = (((mean(xs)*mean(ys)) - mean(xs*ys)) /
         ((mean(xs)**2) - mean(xs**2)))
    return m

if __name__ == '__main__':
    xs = np.array([1,2,3,4,5], dtype=np.float64)
    ys = np.array([5,4,6,5,6], dtype=np.float64)
    m = best_fit_slope(xs,ys)
    print(m)
    print("%.3f" %m)
    slope, intercept, r_value, p_value, std_err = linregress(xs,ys)
    print(slope,intercept)

    



