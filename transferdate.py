# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 21:25:47 2019

@author: Bosola Omisore
"""
import json

from datetime import datetime as dt
filename = open('blackip.txt', "r")  # This opens the blacklist
blacklist = []  #creates a list of blacklist
for line in filename:
    blacklist.append(line.strip())


with open ('list_of_ip.json','r') as t_list:#loads the json file
    d = json.load(t_list)
cd = "23/06/2019"
cd = dt.strptime(cd, "%d/%m/%Y")
date_list =[]
for date in d:
    date_list.append(date['date'])


for s in date_list:
    j = dt.strptime(s, "%d/%m/%Y")
    if j > cd:
        print ('t')#this is for dates after the blacklist dates
    else:
        print('f')#this is for dates before the blacklist dates
    
    


    






