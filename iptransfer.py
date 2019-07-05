# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 11:47:37 2019

@author: RILGRAIN
"""
import json

filename = open('blackip.txt', "r")# This opens the blacklist
Blacklist = []#creates an list of blacklist
for line in filename:
    Blacklist.append(line.strip().split('\n'))#removes the \n from the Ip addresses


with open ('list_of_ip.json','r') as t_list:
    d_list = json.load(t_list)

for d in d_list:
    print (d['original_block'])


#print (Blacklist)