#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 13:39:13 2018

@author: ly
"""

import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt

merge_dir='data/merge/'
merge_list=os.listdir(merge_dir)

name=merge_list[0]
path=os.path.join(merge_dir,name)
df=pd.read_csv(path)
df['timestamp']=df.apply(lambda x:pd.Timestamp(x.loc['timestamp']),axis=1)
df_rgb=df[df.index%1==0]
n_data=df_rgb.shape[0]
index=range(n_data)
fig=plt.figure(figsize=[12,12])
plt.subplot(111)
plt.plot(df_rgb['timestamp'],df_rgb['R1'],'r',linewidth=1)
plt.plot(df_rgb['timestamp'],df_rgb['G1'],'g',linewidth=1)
plt.plot(df_rgb['timestamp'],df_rgb['B1'],'b',linewidth=1)

plt.plot(df_rgb['timestamp'],df_rgb['R2'],'r',linewidth=4)
plt.plot(df_rgb['timestamp'],df_rgb['G2'],'g',linewidth=4)
plt.plot(df_rgb['timestamp'],df_rgb['B2'],'b',linewidth=4)
plt.legend(fontsize=20)
plt.xlabel('Time',fontsize=15)
plt.savefig(name.replace('csv','jpg'))
