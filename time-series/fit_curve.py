#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 15:42:43 2018

@author: ly
"""

import numpy as np
import pandas as pd
import os
import time
import matplotlib.pyplot as plt
from sklearn import linear_model

merge_dir='data/merge/'
merge_list=os.listdir(merge_dir)

name=merge_list[3]
path=os.path.join(merge_dir,name)
df=pd.read_csv(path)

df['timestamp']=df.apply(lambda x:pd.Timestamp(x.loc['timestamp']),axis=1)

df['mktime']=0
for i in range(df.shape[0]):
    t=df.loc[i,'timestamp']
    strp=time.strptime(str(t),"%Y-%m-%d %H:%M:%S")

    mktime=int(time.mktime(strp))
    df.loc[i,'mktime']=mktime
start_time=df.loc[0,'mktime']
df['time']=df['mktime']-start_time
    

df_rgb=df[['R1','R2','G1','G2','B1','B2']]
df[['R1_ln','R2_ln','G1_ln','G2_ln','B1_ln','B2_ln']]=np.log(df_rgb)
t=df['timestamp']
print ('start ml...')

reg = linear_model.LinearRegression()
reg.fit(np.array(df['time']).reshape(-1,1),df['R1_ln'])
k=reg.coef_[0]
b=reg.intercept_
A=np.exp(b)
def fit(t):
    return A*np.exp(k*t)