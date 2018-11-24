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
import datetime
import matplotlib.pyplot as plt
from sklearn import linear_model

days=100
seconds=[3600*24*i for i in range(days)]

merge_dir='data/merge/'
merge_list=os.listdir(merge_dir)

name=merge_list[1]
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
def fit(t,A,k):
    return int(A*np.exp(k*t))


df_inference=pd.DataFrame(columns=df.columns)
df_inference['time']=seconds
df_inference['mktime']=df_inference['time']+start_time

df_inference['timestamp']=df_inference.apply(lambda x:datetime.datetime.fromtimestamp(float(x.loc['mktime'])),axis=1)
for channel in ['R1','R2','G1','G2','B1','B2']:

    reg = linear_model.LinearRegression()
    reg.fit(np.array(df['time']).reshape(-1,1),df[channel+'_ln'])
    k=reg.coef_[0]
    b=reg.intercept_
    A=np.exp(b)
    df_inference[channel]=df_inference.apply(lambda x:fit(x.loc['time'],A,k),axis=1)
    print (A,k)
    
fig=plt.figure(figsize=[20,25])    
plt.subplot(321)
plt.plot(df['timestamp'],df['R1'],'r',linewidth=3)
plt.plot(df_inference['timestamp'],df_inference['R1'],'b',linewidth=2)

plt.subplot(322)
plt.plot(df['timestamp'],df['R2'],'r',linewidth=3)
plt.plot(df_inference['timestamp'],df_inference['R2'],'b',linewidth=2)

plt.subplot(323)
plt.plot(df['timestamp'],df['G1'],'r',linewidth=3)
plt.plot(df_inference['timestamp'],df_inference['G1'],'b',linewidth=2)

plt.subplot(324)
plt.plot(df['timestamp'],df['G2'],'r',linewidth=3)
plt.plot(df_inference['timestamp'],df_inference['G2'],'b',linewidth=2)

plt.subplot(325)
plt.plot(df['timestamp'],df['B1'],'r',linewidth=3)
plt.plot(df_inference['timestamp'],df_inference['B1'],'b',linewidth=2)

plt.subplot(326)
plt.plot(df['timestamp'],df['B2'],'r',linewidth=3)
plt.plot(df_inference['timestamp'],df_inference['B2'],'b',linewidth=2)

plt.legend(fontsize=20)
plt.xlabel('Time',fontsize=15)

plt.savefig('inference-'+name.replace('csv','jpg'))