# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 18:08:42 2019

@author: Bosola Omisore
"""

import json
import radix

filename = open('blacklisted.txt', "r")  # This opens the blacklist
blacklist = []  #creates a list of blacklist
for line in filename:
    blacklist.append(line.strip())
     

black = []
for element in blacklist:
    black.append(element.split(','))

newblack = dict(black)

rtree = radix.Radix()
with open ('list_of_ip.json','r') as t_list:#loads the json file
    d = json.load(t_list)
    for item in d:
        rnode = rtree.add(item['original_block'])



err =[]
for q in newblack:
    err.append(rtree.search_best(q))


print(newblack)#prints transferred addresses in the blacklist
