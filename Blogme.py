#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  8 16:34:46 2024

@author: saumytripathi
"""

import pandas as pd 
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

#Reading xlxx file 

data = pd.read_excel('articles.xlsx')


#Summary of data 
data.describe()
 
#Summary of columns 
data.info()

#Counting the number of articles by source 
#format of groupby:
    


data.groupby(['source_id'])['article_id'].count()

#Number of reactions by publisher 

data.groupby(['source_id'])['engagement_reaction_count'].sum()

#   Dropping a column 

data = data.drop('engagement_comment_plugin_count', axis =1 )

#Functions in python 

def thisfunction ():
    print ('This is a new function')
    
thisfunction()

#This is a function variable 
def aboutme(Name, Surname, Location):
    print ('This is ' + Name + 'Mu surname is ' + Surname + 'Iam fron ' + Location)
    return Name, Surname, Location

a= aboutme('Saumy', 'Tripathi', 'New Delhi')

#Using for loops in functions 

def favfoods (food):
    for x in food:
        print ('the food is '+ x)
    

fastfood = ('tofu', 'salad', 'chia')
favfoods (fastfood)

    
#Creating a keyword flag

keyword = 'crash'
#Forr Loop to isolate each title 
# length = len(data)
# keyword_flag = []
# for x in range (0,length):
#     heading = data['title'][x]
   
#     if keyword in heading:
#         flag = 1
#     else:
#         flag = 0
#     keyword_flag.append(flag)
    
#Creating a function 
def keywordflag(keyword):
    length = len(data)
    keyword_flag = []
    for x in range (0,length):
        heading = data['title'][x]
        try:
            if keyword in heading:
                flag = 1
            else:
                flag = 0
        except:
            flag = 0
        keyword_flag.append(flag)
    return keyword_flag    
    
keywordflag = keywordflag ('murder')
    
    
#Create a new data column in main dataframe 

data ['keyword_flag'] = pd.Series(keywordflag)

#Command for SentimentIntensityAnalyzer

sent_int = SentimentIntensityAnalyzer()

text = data ['title'][16]
sent = sent_int.polarity_scores(text)
    
    
neg = sent ['neg']
pos = sent ['pos']
neu = sent ['neu']

    
#Adding a for loop to extract sentiment per title 

title_neg_sentiment = []
title_pos_sentiment = []
title_neu_sentiment = []
length = len(data)
for x in range (0, length):
    try:
        text = data ['title'][x]
        sent_int = SentimentIntensityAnalyzer()
        sent = sent_int.polarity_scores(text)
        neg = sent ['neg']
        pos = sent ['pos']
        neu = sent ['neu'] 
    except:
        neg = 0
        pos = 0
        neu = 0
    title_neg_sentiment.append(neg)
    title_pos_sentiment.append(pos)
    title_neu_sentiment.append(neu)

title_neg_sentiment = pd.Series(title_neg_sentiment)
title_pos_sentiment = pd.Series(title_pos_sentiment)
title_neu_sentiment = pd.Series(title_neu_sentiment)

# A new data column 

data['title_neg_sentiment'] = title_neg_sentiment 
data['title_pos_sentiment'] = title_pos_sentiment
data['title_neu_sentiment'] = title_neu_sentiment




#Wirting the data 


data.to_excel('bolge_me_clean.xlsx', sheet_name = 'blog_me_data', index = False)

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    



























