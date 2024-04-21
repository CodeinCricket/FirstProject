#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 18:51:13 2024

@author: saumytripathi
"""

import pandas as pd

#file_name = pd.read_csv('file.csv')- Format

data = pd.read_csv('transaction.csv')

data = pd.read_csv('transaction.csv', sep= ';')

#Summary of the data

data.info()

#Variables

CostPerItem = 11.73
SellingPricePerItem = 21.11
NumberOfItemsPurchased = 6

#Mathmetical Operator
ProfitPerTransaction = ProfitPerItem * NumberOfItemsPurchased
CostPerTransaction = CostPerItem * NumberOfItemsPurchased
SellingPricePerTransaction = SellingPricePerItem * NumberOfItemsPurchased


#Cost per transaction calculations 
#CostperTransaction = CostperItem * NumberofItemsPurchased

CostperItem = data['CostPerItem']
NumberOfItemsPurchased = data['NumberOfItemsPurchased']
CostPerTransaction = CostPerItem * NumberOfItemsPurchased

#Adding New Column in a Data Frame 

data['CostPerTransaction'] = CostPerTransaction

#SalesPerTransaction

data ['SellingPricePerTransaction'] = data ['SellingPricePerItem'] * data['NumberOfItemsPurchased']


#Profit and Markup

data ['ProfitPerTransaction'] = data ['SellingPricePerTransaction'] - data ['CostPerTransaction']

#Markup = Slaes - Cost/Cost

data ['Markup'] = (data ['SellingPricePerTransaction'] - data ['CostPerTransaction'] ) / data ['CostPerTransaction']

#Rounding Number 
roundMarkup = round (data['Markup'], 2)

data ['Markup'] = round (data ['Markup'], 2)      

#Merging two or more columns in data sets 

day = data['Day'].astype(str)
year = data['Year'].astype (str)
print (year.dtype)
my_data = day +'-'+data['Month']      
my_data = day +'-'+data['Month']+'-' +year

data['date'] = my_data

#Using IUloc to view specific columns 

data.iloc[3, :]

#Split Function 

split_column = data['ClientKeywords'].str.split(',' , expand = True)

data ['Clinetwords'] = split_column

#Adding new columns in the main dataframe 

data ['Client Age'] = split_column [0]
data ['Client Tyoe'] = split_column [1]
data ['Contract Length'] = split_column [2]

#Removing the brackets 

data ['Client Age'] = data ['Client Age'].str.replace('[', '')
data ['Contract Length'] = data['Contract Length'].str.replace(']', '')

#Lower Function 

data ['ItemDescription'] = data ['ItemDescription'].str.lower()


#Merging Files 

seasons = pd.read_csv('value_inc_seasons.csv', sep= ';')


data = pd.merge (data, seasons, on = 'Month')

#Dropping Columns 

data = data.drop ('ClientKeywords', axis = 1)


data = data.drop ('Day', axis = 1)
data = data.drop(['Year', 'Month'], axis = 1)

#Export
data.to_csv('Value_Inc_cleaned.csv', index = False)

      
      
      
      
      
      
      




