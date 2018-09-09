# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 15:33:23 2018

@author: zee
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#excel_path='1AED-11Monitors.xlsx'
excel_path='1Monitor.xlsx'
excel_path1='monitor_data.xlsx'


df=pd.read_excel(excel_path)
df=df[['Statue_monitor','RGB_1','RGB_2']]
data=np.array(df,'int')

def group(data,statue):
    x1_index=np.argwhere(data[:,0]==statue).flatten()
    x1=data[x1_index,1:]
    y1=data[x1_index,0]
    return x1,y1

x0,y0=group(data,0)
x1,y1=group(data,1)
x2,y2=group(data,2)
x3,y3=group(data,3)



df1=pd.read_excel(excel_path1)
df1=df1[['Statue_monitor','RGB_1','RGB_2']]
data1=np.array(df1,'int')



xx0,yy0=group(data1,0)
xx1,yy1=group(data1,1)
xx2,yy2=group(data1,2)
xx3,yy3=group(data1,3)



fig=plt.figure(figsize=(10,10))
f0=plt.scatter(x0[:,0],x0[:,1],s=95,facecolor='w',edgecolors='r',marker='o')
f1=plt.scatter(x1[:,0],x1[:,1],s=95,facecolor='w',edgecolors='g',marker='o')
f0=plt.scatter(x2[:,0],x2[:,1],s=95,facecolor='w',edgecolors='c',marker='o')
f3=plt.scatter(x3[:,0],x3[:,1],s=95,facecolor='w',edgecolors='y',marker='o')
#plt.plot([0,20000],[center[1],center[1]],'c--',linewidth=5)
#plt.plot([center[0],center[0]],[0,10000],'c--',linewidth=5)

ff0=plt.scatter(xx0[:,0],xx0[:,1],s=5,color='r',marker='*')
ff1=plt.scatter(xx1[:,0],xx1[:,1],s=5,color='g',marker='*')
ff2=plt.scatter(xx2[:,0],xx2[:,1],s=5,color='c',marker='*')
ff3=plt.scatter(xx3[:,0],xx3[:,1],s=5,color='y',marker='*')

plt.legend((f0,f1,f3),('0','1','3'),scatterpoints=10,fontsize=22,loc='lower right')
plt.xlim([2000,8000])
plt.ylim([2500,7500])
plt.xlabel('RGB_1(Battery)',fontsize=20)
plt.ylabel('RGB_2(Meachine)',fontsize=20)
#plt.annotate('(%d,%d)'%(center[0],center[1]),center,center+[200,100],arrowprops=dict(facecolor='black',shrink=0.01),fontsize=30)
fig.savefig('scatter2.jpg')