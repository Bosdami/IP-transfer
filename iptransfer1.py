# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 18:08:42 2019

@author: Bosola Omisore
"""

import gzip
import json
import radix
from datetime import datetime
from datetime import timedelta

rtree = radix.Radix()
with open ('list_of_ip.json','r') as t_list:#loads the json file
    d = json.load(t_list)
    for item in d:
        for ip in item['transferred_blocks'].split(","):
            rnode = rtree.add(ip.strip())
            rnode.data['date'] = item['date']

with gzip.open('blacklisted_ips_dates.txt.gz', "rt") as fin:
    blacklist = set()  # creates a list of blacklist
    for line in fin:
        lf = line.strip().split(",")
        if len(lf) > 1:
            ip = lf[0]
            # blacklist.append(ip)
            rnode = rtree.search_best(ip)
            if rnode is not None:
                transfer_dt = datetime.strptime(rnode.data['date'], '%d/%m/%Y')
                blacklist_dt = datetime.strptime(lf[1], '%Y-%m-%d')
                elapsed_time = abs((transfer_dt - blacklist_dt).total_seconds() / 3600) # Elapsed time in hours
                print(ip, elapsed_time)

