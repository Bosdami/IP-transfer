# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 18:12:49 2019

@author: Bosola Omisore
"""
import json
from ipaddress import ip_network, ip_address
import radix
from datetime import datetime as dt, date

filename = open('blacklisted.txt', "r")  # This opens the blacklist with dates
blacklist = []  #creates a list of blacklist
for line in filename:
    blacklist.append(line.strip())
black = []
for element in blacklist:
    black.append(element.split(','))
newblack = dict(black)
#This changes the date format
for k,v in newblack.items():
    if not isinstance(v,dict):
        newblack[k] = dt.strptime(v, "%Y-%m-%d").strftime("%d/%m/%Y")


#This loads the transfer addresses
with open ('list_of_ip.json','r') as t_list:#loads the json file
    dlist = json.load(t_list)
#removing duplicate data
res = [dict(d, transferred_blocks=ip) for d in dlist for ip in d['transferred_blocks'].split(', ')]#replaces redundant transfers

newd = {d['transferred_blocks']: d['date'] for d in res}

#this applies the radix tree
rtree = radix.Radix()
for k1,v1 in newd.items():
    if not isinstance(v1,dict):
        rnode = rtree.add(k1)
        rnode.data[k1]= (v1)

#This checks for the if the transfer date was before or after
found = {}
for ip_addr in newblack:
    for cidr_block in newd:
        if ip_address(ip_addr) in ip_network(cidr_block):
            newblack_date = date(*map(int,newblack[ip_addr].split("/")[::-1]))
            newd_date = date(*map(int,newd[cidr_block].split("/")[::-1]))            
            if newd_date > newblack_date:
                found[cidr_block] = 'before'
            else:
                found[cidr_block] = 'after'


print (found)




