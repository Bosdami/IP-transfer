# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 11:47:37 2019

@author: Bosola Omisore
"""
import json
import radix
import pandas as pd
filename = open('blackip.txt', "r")# This opens the blacklist
Blacklist = []#creates a list of blacklist
for line in filename:
    Blacklist.append(line.strip().split('\n'))#removes the \n from the Ip addresses

blist = [(x) for [x] in Blacklist]#converting it to a list

with open ('list_of_ip.json','r') as t_list:#loads the json file
    d = json.load(t_list)



address1 = [item['original_block'] for item in d]#selecting an item in the transfer
address = set(address1)


rtree = radix.Radix()
rnode = []

for a in address:
    rnode.append(rtree.add(a))
err =[]
for q in blist:

    err.append(rtree.search_best(q))
print(err)


