#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 14:46:56 2024

@author: saumytripathi
"""

import json
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

#Method 1 to read json data 

json_file = open ('loan_data_json.json')

data= json.load (json_file)

#Method 2 to load json 

with open ('loan_data_json.json') as json_file :
    data = json.load(json_file)
    print (data)
    
#Transforming Data

loandata = pd.DataFrame(data)

#Finding unique values

loandata['purpose'].unique()

#Describe the data 

loandata.describe()

#Decribe specific data column

loandata['pub.rec'].describe()
loandata['fico'].describe()
loandata['dti'].describe()

#Using EXP to get annual income 

income = np.exp(loandata['log.annual.inc'])
loandata['annual income'] = income

#Working with array 
arr = np.array (['1,2,3,4'])

#0D Array 
arr = np.array (32)

#2D Array 

arr = np.array ([[1,2,3], [4,5,6]])

#IF statement 

a = 50
b = 432
if b>a:
    print ('b i greater than a')

#Let's add more condition 

a = 40
b = 500
c = 1500

if b > a and b < c:
    print ('b is greater than a but less than c ')


# What if a condition is not met 

a = 40
b = 300
c = 70
if b > a and b < c:
    print ('b is greater than a but less than c ')
else:
    print ('No conditions met')
    
    
#Another condition different metrics

a = 40
b = 0
c = 30

if b > a and b < c:
    print ('b is greater than a but less than c')
elif b > a and b > c:
    print ('b is greater than a and c')
else: 
    print ('No conditions met')



a = 40
b = 500
c = 30

if b > a or b < c:
    print ('b is greater than a but less than c')
else: 
    print ('No conditions met')





#FICO Score

# FICO RANGE
# fico >= 300 and < 400: 'Very Poor'
# fico >= 400 and ficoscore < 600: 'Poor'
# fico >= 601 and ficoscore < 660: 'Fair'
# fico >= 660 and ficoscore < 780: 'Good'
# fico >=780: 'Excellent'

fico = 250

if fico >= 300 and fico< 400:
    ficocat = 'Very Poor'
elif fico >= 400 and fico< 600:
    ficocat = 'Poor'
elif fico >= 600 and fico< 650:
    ficocat = 'Fair'
elif fico >= 600 and fico< 780:
    ficocat = "Good"
elif fico > 780:
    ficocat = 'Excellent'
else:
    ficocat = 'Not Found'
print (ficocat)

#fOR lOOP

fruit = ['apple', 'pear', 'mango', 'banana']
for x in fruit:
    print (x)
    y = x + 'fruit'
    print (y)
   
for x in range (0,3):
    y = fruit[x] + ' for sale '
    print (y)

#Laondata 
length = len (loandata)
ficocat =[]
for x in range (0, length):
    category = loandata['fico'][x]
        
    if category >= 300 and category < 400:
        cat= ('Very Poor')
    elif category >= 400 and category < 600:
        cat = 'Poor'
    elif category >= 601 and category <660:
        cat = 'Fair'
    elif category >= 660 and category <700:
        cat = 'Good'
    elif category > 700:
        cat = 'Excellent'
    else:
        cat = 'Unkown'
    ficocat.append (cat)
    
ficocat = pd.Series(ficocat)
loandata ['fico.category'] = ficocat

#While Loop

i = 1
while i<10:
    print (i)
    i= i +1
    
# Tdf.oc
loandata.loc[loandata['int.rate'] > 0.12, 'int.rate.type'] = 'High'
loandata.loc[loandata['int.rate']<0.12, 'int.rate.type'] = 'Low'


#Number of loans/rows by fico category 


catplot = loandata.groupby(['fico.category']).size()
catplot.plot.bar(color= 'Purple', width = 0.6)
plt.show()

#Test Case 

catplot1 = loandata.groupby (['purpose']).size()
catplot1.plot.bar(color = 'Purple', width = 0.3)
plt.show()

    
#Scatter Graph 
x= loandata ['dti']
y= loandata ['annual income']
plt.scatter (x,y, color = '#4ca50a')
plt.show()
    
    
    
#Writing to csv 

loandata.to_csv('loan_data_cleaned.csv', index = True)
    
    
    
    
    
    
    
    
    
    
    
    

























