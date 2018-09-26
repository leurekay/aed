# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 09:19:10 2018

@author: zee
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import pearsonr
import seaborn as sns
from sklearn import svm

from mpl_toolkits.mplot3d import Axes3D

from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import mpl_toolkits.mplot3d as mp3d

excel_path='data.xlsx'
df=pd.read_excel(excel_path)
filter_=((df['AED_ID']==73654011066) | (df['AED_ID']==73154011634)) & (df['Monitor_ID']==8)
df=df[~filter_]

df['R1_delta']=df['R1']-df['R1_']
df['R2_delta']=df['R2']-df['R2_']

df['G1_delta']=df['G1']-df['G1_']
df['G2_delta']=df['G2']-df['G2_']

df['B1_delta']=df['B1']-df['B1_']
df['B2_delta']=df['B2']-df['B2_']

df['C1_delta']=df['C1']-df['C1_']
df['C2_delta']=df['C2']-df['C2_']


df['Battery']=df['Display']%2
df['Meachine']=df['Display']//2

class Classifier():
    def __init__(self,df,features,label):
        
        self.which=label
        self.df_sub=df.loc[:,features+[label]]
        
        self.data=data1=np.array(self.df_sub)[:,:-1]
        self.label=data1=np.array(self.df_sub)[:,-1]

#        
        index0=np.where(self.label==0)
        index1=np.where(self.label==1)
        
        self.data0=self.data[index0]
        self.data1=self.data[index1]
        
        
    def svm(self):
        self.model=model = svm.SVC(kernel='linear',C=0.00000002)
        model.fit(self.data,self.label)
        w,b=model.coef_[0],model.intercept_
        self.w=w
        self.b=b
        self.support=support=model.support_vectors_
        norm=np.linalg.norm(w)
        dist=(np.dot(support,w)+b)/norm
        self.margin_dist=abs(dist[0])
        print ('support vector :')
        print (support)
        print ('margin distance : %d'%abs(dist[0]))
        with open('coef_%s.txt'%self.which,'w') as f:
            for i in w:
                f.write('%.9f\n'%i)
            f.write('%.9f\n'%b[0])
            
            
    def plot(self,isSurface=True):
        data0=self.data0
        data1=self.data1
        ax = plt.figure(figsize=[15,15]).add_subplot(111, projection = '3d')
        
        f1=ax.scatter(data0[:,0], data0[:,1], data0[:,2], s=50,facecolor='w',edgecolors='g',marker='o')
        f2=ax.scatter(data1[:,0], data1[:,1], data1[:,2], s=50,facecolor='w',edgecolors='r',marker='o')
        ax.scatter(self.support[:,0], self.support[:,1], self.support[:,2], s=10,facecolor='k',edgecolors='k',marker='o')
        
        
        ax.legend((f1,f2),
                      ('good','bad'),
                      scatterpoints=1,fontsize=20,loc='Best')
        ax.set_xlabel('R')
        ax.set_ylabel('G')
        ax.set_zlabel('B')
    
        
        
        
        
#        bot = [(1000,1000, 4000),
#               (1000, 3000, 4000),
#               (3000, 3000, 4000),
#               (3000, 1000, 4000),
#               ]
        xy=np.array([[-100,-100],
               [-100,3000],
               [3000,3000],
               [3000,-100],
               ])
        w,b=self.model.coef_[0],self.model.intercept_
        
        z=-(b[0]+np.dot(xy,w[:2]))/w[2]
        xyz=np.concatenate([xy,z.reshape([4,1])],axis=1)     
        face1 = mp3d.art3d.Poly3DCollection([xyz], alpha=0.4, linewidth=1)
        # This is the key step to get transparency working
        alpha = 0.5
        face1.set_facecolor((0, 0, 1, alpha))
        ax.add_collection3d(face1)


        z1=z+1/w[2]
        xyz1=np.concatenate([xy,z1.reshape([4,1])],axis=1)     
        face1 = mp3d.art3d.Poly3DCollection([xyz1], alpha=0.1, linewidth=1)
        # This is the key step to get transparency working
        alpha = 0.5
        face1.set_facecolor((0, 0, 1, alpha))
        ax.add_collection3d(face1)
        
        
        z2=z-1/w[2]
        xyz2=np.concatenate([xy,z2.reshape([4,1])],axis=1)     
        face1 = mp3d.art3d.Poly3DCollection([xyz2], alpha=0.1, linewidth=1)
        # This is the key step to get transparency working
        alpha = 0.5
        face1.set_facecolor((0, 0, 1, alpha))
        ax.add_collection3d(face1)


        plt.title(self.which,fontsize=20)
        plt.show()

    def distance(self,xyz):
        norm=np.linalg.norm(self.w)
        dist=(np.dot(np.array(xyz),self.w)+self.b)/norm
        return dist

battery=Classifier(df,features=['R1_delta','G1_delta','B1_delta'],
                   label='Battery')
battery.svm()
battery.plot()
df['B_dist']=0
df['B_dist']=df.apply(lambda dfx:int(battery.distance([dfx['R1_delta'],dfx['G1_delta'],dfx['B1_delta']])),axis=1)

meachine=Classifier(df,features=['R2_delta','G2_delta','B2_delta'],
                   label='Meachine')
meachine.svm()
meachine.plot()
df['M_dist']=0
df['M_dist']=df.apply(lambda dfx:int(battery.distance([dfx['R2_delta'],dfx['G2_delta'],dfx['B2_delta']])),axis=1)


gg=df[(abs(df['B_dist'])<battery.margin_dist) | (abs(df['M_dist'])<meachine.margin_dist) ]

