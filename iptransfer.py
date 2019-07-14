# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 11:47:37 2019

@author: Bosola Omisore
"""
import json
import radix
import pandas as pd
filename = open('blackip.txt', "r")  # This opens the blacklist
blacklist = []  #creates a list of blacklist
for line in filename:
    blacklist.append(line.strip())

rtree = radix.Radix()
with open ('list_of_ip.json','r') as t_list:#loads the json file
    d = json.load(t_list)
    for item in d:
        rnode = rtree.add(item['original_block'])

err =[]
for q in blacklist:
    err.append(rtree.search_best(q))
print(err)


