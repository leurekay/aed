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
    

comp=re.compile('[1-9]\d*-[1-9]\d*-[1-9]\d*-[1-9]\d*-[1-9]\d*-[1-9]\d*-[1-9]\d*-[1-9]\d*-[1-9]\d*-[1-9]\d*-[1-9]\d*-[1-9]\d*')
box=[]
box_time=[]
for s in txt:  
    timestamp=s.split('[')[-1].split(']')[0]

    data=comp.findall(s)
    if len(data)>0:
        box_time.append(timestamp)
        box.append(data)
    
#box=filter(lambda x : len(x)>0,box)
box=map(lambda x:x[0].split('-'),box)
box=np.array(box,'int')

features=['R1','R1_','R2','R2_','G1','G1_','G2','G2_','B1','B1_','B2','B2_']
df=pd.DataFrame(box,columns=features)
df['timestamp']=box_time
df['timestamp']=df.apply(lambda x:pd.Timestamp(x.loc['timestamp']),axis=1)

g_df=df.groupby(['R1_','R2_','G1_','G2_','B1_','B2_'])
count_df=g_df.count()
count_df.sort_values(by=['R1'],ascending=False,inplace=True)
count_df=count_df[count_df.R1>1000]
unique_calibrations=list(count_df.index)

device_data={}
for cali in unique_calibrations:
    sub_df=df[(df.R1_==cali[0]) & (df.R2_==cali[1]) & (df.G1_==cali[2]) & (df.G2_==cali[3])]
    device_data[cali]=sub_df
    key_str=str(cali[0])+'-'+str(cali[1])+'-'+str(cali[2])+'-'+str(cali[3])+'-'+str(cali[4])+'-'+str(cali[5])

    sub_df.to_csv('data/nohup/'+key_str+'.csv',index=None)

key=unique_calibrations[14]
key_str=str(key[0])+'-'+str(key[1])+'-'+str(key[2])+'-'+str(key[3])+'-'+str(key[4])+'-'+str(key[5])
value=device_data[key]
N=value.shape[0]
index=filter(lambda x: x%10==0,range(N))
value=value.iloc[index]

fig=plt.figure(figsize=[12,12])
plt.subplot(111)
plt.plot(index,value['R1'],'r')
plt.plot(index,value['G1'],'g')
plt.plot(index,value['B1'],'b')

plt.plot(index,value['R2'],'r',linewidth=3)
plt.plot(index,value['G2'],'g',linewidth=3)
plt.plot(index,value['B2'],'b',linewidth=3)
plt.legend(fontsize=20)
plt.xlabel('Time (2 min)',fontsize=15)
plt.title(key_str,fontsize=20)
#plt.legend('ca',fontsize=20)

#plt.subplot(212)
#plt.plot(index,value['R2'])

#plt.subplot(323)
#plt.plot(index,value['G1'])
#plt.subplot(324)
#plt.plot(index,value['G2'])
#plt.subplot(325)
#plt.plot(index,value['B1'])
#plt.subplot(326)
#plt.plot(index,value['B2'])
plt.savefig('series.png')