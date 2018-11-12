#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 10:47:10 2018

@author: ly
"""

import re
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


path='log.out'

with open(path,'r') as f:
    txt=f.readlines()
    
s=txt[6]

comp=re.compile('[1-9]\d*-[1-9]\d*-[1-9]\d*-[1-9]\d*-[1-9]\d*-[1-9]\d*-[1-9]\d*-[1-9]\d*-[1-9]\d*-[1-9]\d*-[1-9]\d*-[1-9]\d*')
box=[]
for s in txt:  
    data=comp.findall(s)
    box.append(data)
    
box=filter(lambda x : len(x)>0,box)
box=map(lambda x:x[0].split('-'),box)
box=np.array(box,'int')

features=['R1','R1_','R2','R2_','G1','G1_','G2','G2_','B1','B1_','B2','B2_']
df=pd.DataFrame(box,columns=features)

g_df=df.groupby(['R1_','R2_','G1_','G2_','B1_','B2_'])
count_df=g_df.count()
count_df.sort_values(by=['R1'],ascending=False,inplace=True)
count_df=count_df[count_df.R1>1000]
unique_calibrations=list(count_df.index)

device_data={}
for cali in unique_calibrations:
    sub_df=df[(df.R1_==cali[0]) & (df.R2_==cali[1]) & (df.G1_==cali[2]) & (df.G2_==cali[3])]
    device_data[cali]=sub_df

key=unique_calibrations[6]
value=device_data[key]
N=value.shape[0]
index=filter(lambda x: x%10==0,range(N))
value=value.iloc[index]
fig=plt.figure(figsize=[12,12])
plt.subplot(211)
plt.plot(index,value['R1'],'r')
#plt.annotate('(%d)'%(key[0]),[300,4000],[300,4001],fontsize=20,arrowprops=dict(facecolor='black',shrink=0.05))
#plt.legend('ca',fontsize=20)

plt.subplot(212)
plt.plot(index,value['R2'])
#plt.subplot(323)
#plt.plot(index,value['G1'])
#plt.subplot(324)
#plt.plot(index,value['G2'])
#plt.subplot(325)
#plt.plot(index,value['B1'])
#plt.subplot(326)
#plt.plot(index,value['B2'])
plt.savefig('series.png')