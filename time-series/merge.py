#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 11:06:36 2018

@author: ly
"""

import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt


nohup='data/nohup'
database='data/database'
features=['R1','R1_','R2','R2_','G1','G1_','G2','G2_','B1','B1_','B2','B2_','C1','C1_','C2','C2_']

nohup_list=os.listdir(nohup)
database_list=os.listdir(database)
intersection=set.intersection(set(nohup_list),set(database_list))
intersection=list(intersection)
for csv in intersection:
    df1=pd.read_csv(os.path.join(database,csv))
    df2=pd.read_csv(os.path.join(nohup,csv))
    df1_last_time=df1.loc[df1.shape[0]-1,'timestamp']
    
    ptr=0
    while df1_last_time>=df2.loc[ptr,'timestamp']:
        ptr+=1
    merge=pd.concat([df1,df2[ptr:]],ignore_index=True)
    merge=merge[features+['timestamp']]
    merge.to_csv(os.path.join('data/merge',csv))
    
