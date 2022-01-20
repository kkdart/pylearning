#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 15:46:31 2019

@author: berkunis
"""
##############################################01_02_PythonLibraries#####################################################
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
import matplotlib.pyplot as plt 

#import data
data = pd.read_csv("../Datasets/insurance.csv")
#data = pd.read_csv("/Users/kyryl/Documents/GitHub/pylearning/Predictive Analytics/Datasets/insurance.csv")


#see the first 15 lines of data
print(data.head(15))

############################################01_03_HandlingMissingValues###################################################

#check how many values are missing (NaN) before we apply the methods below 
print(data.info())

count_nan = data.isnull().sum()
print(count_nan[count_nan>0])

#fill in the missing values (there are so many other methods out there)
data['bmi'].fillna(data['bmi'].mean(), inplace = True)

count_nan = data.isnull().sum()
print(count_nan[count_nan>0])
#check how many values are missing (NaN) - after we filled in the NaN


############################################Vizualization################################################################