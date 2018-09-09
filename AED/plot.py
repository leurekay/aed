# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 12:13:34 2018

@author: zee
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

excel_path='monitor_data.xlsx'

#df=pd.read_excel(excel_path)
#df['Type']=df['AED_ID']//10000000 #7315,7323
##g=df.gro
#
#y=df['Statue_monitor']
#y=np.array(y,'int')
#
#
#X=df[['RGB_1','RGB_2']]
#X=np.array(X,'int')
#
#def group(statue):
#    index=np.argwhere(y==statue).flatten()
#    y_=y[index]
#    x_=X[index]
#    center=np.mean(x_,axis=0)
#    return x_,y_,center
#
#
#x0,y0,c0=group(0)
#x1,y1,c1=group(1)
#x2,y2,c2=group(2)
#x3,y3,c3=group(3)
#cc=np.concatenate([c0.reshape(1,2),c1.reshape(1,2),c2.reshape(1,2),c3.reshape(1,2)])
#center=np.mean(cc,axis=0)
#
#
#
#
#
#
#def normal2d(mean,sigma):
#    sigma_inv=np.linalg.inv(sigma)
#    sigma_det=np.linalg.det(sigma)
##    exp=np.dot(np.dot()
#
#
#fig=plt.figure(figsize=(10,10))
#f0=plt.scatter(x0[:,0],x0[:,1],s=65,facecolor='w',edgecolors='r',marker='o')
#f1=plt.scatter(x1[:,0],x1[:,1],s=95,facecolor='w',edgecolors='g',marker='*')
#f2=plt.scatter(x2[:,0],x2[:,1],s=65,facecolor='b',edgecolors='b',marker='+')
#f3=plt.scatter(x3[:,0],x3[:,1],s=65,facecolor='w',edgecolors='y',marker='v')
#plt.plot([0,10000],[center[1],center[1]],'c--',linewidth=5)
#plt.plot([center[0],center[0]],[0,10000],'c--',linewidth=5)
#plt.legend((f0,f1,f2,f3),('0','1','2','3'),scatterpoints=10,fontsize=22)
#plt.xlim([3000,6000])
#plt.ylim([2500,5500])
#plt.xlabel('RGB_1(Battery)',fontsize=20)
#plt.ylabel('RGB_2(Meachine)',fontsize=20)
#plt.annotate('(%d,%d)'%(center[0],center[1]),center,center+[200,100],arrowprops=dict(facecolor='black',shrink=0.01),fontsize=30)
#fig.savefig('scatter.jpg')








class Monitor():
    def __init__(self,excel_path):
        df=pd.read_excel(excel_path)
        df['Type']=df['AED_ID']//10000000 #7315,7323,7365
        df=df[df['RGB_1']!=0]
        self.df=df
        
    def group(self,statue,t):
        df=self.df
        cell=df[(df['Statue_monitor']==statue) & (df['Type']==t)]
        return np.array(cell[['RGB_1','RGB_2']],'int')        

m=Monitor(excel_path)
df=m.df
x_min=df[(df['Display']==0) | (df['Display']==2)]['RGB_1'].max()
x_max=df[(df['Display']==1) | (df['Display']==3)]['RGB_1'].min()
x_c=(x_min+x_max)//2  

y_left_min=df[(df['Display']==0)]['RGB_2'].max()
y_left_max=df[(df['Display']==2)]['RGB_2'].min()
y_left_c=(y_left_min+y_left_max)//2

y_right_min=df[(df['Display']==1)]['RGB_2'].max()
y_right_max=df[(df['Display']==3)]['RGB_2'].min()
y_right_c=(y_right_min+y_right_max)//2

statue_list=[0,1,2,3]
type_list=[7315,7323,7365]    

color_list=['r','g','b','y']
marker_list=['o','v','^','s']

box={}
fig=plt.figure(figsize=(10,10))
for  i,statue in enumerate(statue_list):
    for j,t in enumerate(type_list):
        x=m.group(statue,t)
        f=plt.scatter(x[:,0],x[:,1],s=75,facecolor='w',edgecolors=color_list[j],marker=marker_list[i])
        box[(statue,t)]=f
        
        
plt.plot([0,x_c],[y_left_c,y_left_c],'c--',linewidth=5)
plt.plot([x_c,10000],[y_right_c,y_right_c],'c--',linewidth=5)
plt.plot([x_c,x_c],[0,10000],'c--',linewidth=5)
l1=plt.legend((box[2,7315],box[2,7323],box[2,7365]),
              ('AEDtype1','AEDtype2','AEDtype3'),
              scatterpoints=1,fontsize=15,loc='Best',bbox_to_anchor=(0.25, 1))

plt.xlim([2900,5700])
plt.ylim([2600,5400])
plt.xlabel('RGB_1  (Battery)',fontsize=20)
plt.ylabel('RGB_2  (Meachine)',fontsize=20)
#plt.annotate('(%d,%d)'%(center[0],center[1]),center,center+[200,100],arrowprops=dict(facecolor='black',shrink=0.01),fontsize=30)
plt.annotate('%d'%(0),np.array([x_c,(y_left_c+y_right_c)//2])+[-600,-500],fontsize=60)
plt.annotate('%d'%(1),np.array([x_c,(y_left_c+y_right_c)//2])+[400,-500],fontsize=60)
plt.annotate('%d'%(2),np.array([x_c,(y_left_c+y_right_c)//2])+[-600,400],fontsize=60)
plt.annotate('%d'%(3),np.array([x_c,(y_left_c+y_right_c)//2])+[400,400],fontsize=60)
plt.annotate('%d'%(x_c),[x_c,2600],[x_c,2600]+np.array([200,100]),arrowprops=dict(facecolor='black',shrink=0.05),fontsize=20)
plt.annotate('%d'%(y_left_c),[2900,y_left_c],[2900,y_left_c]+np.array([200,100]),arrowprops=dict(facecolor='black',shrink=0.05),fontsize=20)
plt.annotate('%d'%(y_right_c),[5700,y_right_c],[5700,y_right_c]+np.array([-400,-200]),arrowprops=dict(facecolor='black',shrink=0.05),fontsize=20)
fig.savefig('scatter.jpg')