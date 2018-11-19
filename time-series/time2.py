#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 15:14:33 2018

@author: ly
"""


import re
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

#path='data/124.xlsx'
#path='data/133.xlsx'
#path='data/150.xlsx'
path='data/231.xlsx'
df=pd.read_excel(path)
df.sort_values(by='OperateTime',inplace=True)
df=df[['Args','OperateTime']]

features=['R1','R1_','R2','R2_','G1','G1_','G2','G2_','B1','B1_','B2','B2_','C1','C1_','C2','C2_']


def parse(series):
    Args=series.loc['Args']
    s=str(Args)
    loc_R=s.find('R:')
    s=s[loc_R:]
    comp=re.compile('[1-9]\d*')
    digitals= comp.findall(s)
    digitals=map(lambda x:int(x),digitals)
    if digitals==[]:
        digitals=[0]*16
    return pd.Series(digitals)

df_rgb=df.apply(parse,axis=1)
df_rgb.columns=features
df_rgb['timestamp']=df['OperateTime']

R1_=df_rgb['R1_']
cc=dict(Counter(R1_))
most_frequence=cc.keys()[0]
for key in cc.keys():
    if cc[key]>cc[most_frequence]:
        most_frequence=key
df_rgb=df_rgb[df_rgb['R1_']==most_frequence]

cali_value=df_rgb.loc[1,['R1_','R2_','G1_','G2_','B1_','B2_']]
cali_value=np.array(cali_value,'int')

df_rgb=df_rgb[df_rgb.index%1==0]
n_data=df_rgb.shape[0]
index=range(n_data)
fig=plt.figure(figsize=[12,12])
plt.subplot(111)
plt.plot(df_rgb['timestamp'],df_rgb['R1'],'r')
plt.plot(df_rgb['timestamp'],df_rgb['G1'],'g')
plt.plot(df_rgb['timestamp'],df_rgb['B1'],'b')

plt.plot(df_rgb['timestamp'],df_rgb['R2'],'r',linewidth=3)
plt.plot(df_rgb['timestamp'],df_rgb['G2'],'g',linewidth=3)
plt.plot(df_rgb['timestamp'],df_rgb['B2'],'b',linewidth=3)
plt.legend(fontsize=20)
plt.xlabel('Time (2 min)',fontsize=15)
plt.title(str(cali_value[0])+'-'+str(cali_value[1])+'-'+str(cali_value[2])+'-'+str(cali_value[3])+'-'+str(cali_value[4])+'-'+str(cali_value[5]),fontsize=20)

plt.savefig(path.replace('xlsx','png'))