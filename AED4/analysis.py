# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 02:34:12 2018

@author: zee
"""


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import pearsonr
import seaborn as sns


excel_path='data2.xlsx'
df=pd.read_excel(excel_path)

df['R1_delta']=df['R1']-df['R1_']
df['R2_delta']=df['R2']-df['R2_']

df['G1_delta']=df['G1']-df['G1_']
df['G2_delta']=df['G2']-df['G2_']

df['B1_delta']=df['B1']-df['B1_']
df['B2_delta']=df['B2']-df['B2_']

df['C1_delta']=df['C1']-df['C1_']
df['C2_delta']=df['C2']-df['C2_']

cor=pearsonr(df['G2_delta'],df['B2_delta'])

df_delta=df.loc[:,['R1_delta','R2_delta','G1_delta','G2_delta','B1_delta','B2_delta']]
statue_monitor=df['Statue_monitor']
statue_monitor=statue_monitor.T

matrix_delta=np.array(df_delta)
cov=np.cov(matrix_delta.T)



class Utils():
    def __init__(self,df,col1,col2,labels):
        self.df=df
        self.col1=col1
        self.col2=col2
        self.x=np.array(df[col1])
        self.y=np.array(df[col2])
        self.labels=np.array(df[labels])
        
        self.boxes={}
        for label in [0,1,2,3]:
            xy=df[df[labels]==label]
            xy=xy.loc[:,[col1,col2]]
            xy=np.array(xy)
            self.boxes[label]=xy
        self.statistic=[]
        for label in [0,1,2,3]:
            xy=self.boxes[label] 
            xy_min=xy.min(axis=0)
            xy_max=xy.max(axis=0)
            xy_center=xy.mean(axis=0)
            self.statistic.append(np.concatenate([xy_min,xy_max,xy_center]))
        self.statistic=np.array(self.statistic)
        
        ss=self.statistic
        
        self.xmid=max((ss[0,2],ss[2,2])+min(ss[1,0],ss[3,0]))/2
        self.ymid=max((ss[0,3],ss[1,3])+min(ss[2,1],ss[3,1]))/2
        self.xmid=int(self.xmid)
        self.ymid=int(self.ymid)
        self.lim=np.array([ss.min(axis=0)[0]-100,ss.min(axis=0)[1]-100,ss.max(axis=0)[2]+100,ss.max(axis=0)[3]+100])
        
    def plot(self,fig):
        box=self.boxes      
        f0=plt.scatter(box[0][:,0],box[0][:,1],s=55,facecolor='w',edgecolors='r',marker='o')
        f1=plt.scatter(box[1][:,0],box[1][:,1],s=55,facecolor='w',edgecolors='g',marker='o')
        f2=plt.scatter(box[2][:,0],box[2][:,1],s=55,facecolor='w',edgecolors='b',marker='o')
        f3=plt.scatter(box[3][:,0],box[3][:,1],s=55,facecolor='w',edgecolors='y',marker='o')
        plt.plot([self.xmid,self.xmid],[-10000,10000],'c--',linewidth=5)
        plt.plot([-10000,10000],[self.ymid,self.ymid],'m--',linewidth=5)
        plt.annotate('(%d,%d)'%(self.xmid,self.ymid),np.array([self.xmid,self.ymid]),np.array([self.xmid,self.ymid])+[300,200],fontsize=20,arrowprops=dict(facecolor='black',shrink=0.05))
        plt.title(self.col1[0],fontsize=20)
        plt.xlim([self.lim[0],self.lim[2]])
        plt.ylim([self.lim[1],self.lim[3]])
        

color_list=['r','g','b','y']
marker_list=['o','v','^','s']


fig=plt.figure(figsize=(12,12))

R=Utils(df,'R1_delta','R2_delta','Display')
plt.subplot(221)
R.plot(fig)

G=Utils(df,'G1_delta','G2_delta','Display')
plt.subplot(222)
G.plot(fig)

B=Utils(df,'B1_delta','B2_delta','Display')
plt.subplot(223)
B.plot(fig)

plt.subplot(224)

colormap = sns.diverging_palette(220, 10, as_cmap = True)
_ = sns.heatmap(
        df_delta.corr(), 
        cmap = colormap,
        square=True, 
        cbar_kws={'shrink':.9 }, 
#        ax=ax,
        annot=True, 
        linewidths=0.1,vmax=1.0, linecolor='white',
        annot_kws={'fontsize':12 }
    )
plt.title('Correlation Matrix', size=18)


fig.savefig('scatter.jpg')


#f0=plt.scatter(box[0][:,0],box[0][:,1],s=55,facecolor='w',edgecolors='r',marker='o')
#f0=plt.scatter(box[1][:,0],box[1][:,1],s=55,facecolor='w',edgecolors='g',marker='o')
#f0=plt.scatter(box[2][:,0],box[2][:,1],s=55,facecolor='w',edgecolors='b',marker='o')
#f0=plt.scatter(box[3][:,0],box[3][:,1],s=55,facecolor='w',edgecolors='y',marker='o')
       




