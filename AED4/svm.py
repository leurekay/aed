# -*- coding: utf-8 -*-
"""
Created on Fri Sep 07 18:07:29 2018

@author: zee
"""



import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import pearsonr
import seaborn as sns
from sklearn import svm

from mpl_toolkits.mplot3d import Axes3D


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


df['Battery']=df['Display']%2
df['Meachine']=df['Display']//2

df1_delta=df.loc[:,['R1_delta','G1_delta','B1_delta','Battery']]
data1=np.array(df1_delta)
x1=data1[:,0]
y1=data1[:,1]
z1=data1[:,2]
X1=data1[:,:3]
label1=data1[:,3]

index1_n=np.where(label1==0)
index1_p=np.where(label1==1)

x1_n=data1[index1_n,0]
y1_n=data1[index1_n,1]
z1_n=data1[index1_n,2]

x1_p=data1[index1_p,0]
y1_p=data1[index1_p,1]
z1_p=data1[index1_p,2]


ax = plt.figure(figsize=[15,20]).add_subplot(111, projection = '3d')



ax.scatter(x1_n, y1_n, z1_n, s=50,facecolor='w',edgecolors='r',marker='o')
ax.scatter(x1_p, y1_p, z1_p, s=50,facecolor='w',edgecolors='g',marker='o')
 

#设置坐标轴

ax.set_xlabel('X Label')

ax.set_ylabel('Y Label')

ax.set_zlabel('Z Label')

 






model = svm.SVC(kernel='linear')
model.fit(X1,label1)


#def plot_svc_decision_function(clf, ax):
#    """Plot the decision function for a 2D SVC"""
x = np.linspace(-1000, 3000, 150)
y = np.linspace(-1000, 3000, 150)
z = np.linspace(-1000, 3000, 150)
X,Y,Z=np.meshgrid(x,y,z)
P = np.zeros_like(X)
for i, xi in enumerate(x):
    for j, yj in enumerate(y):
        for k, zk in enumerate(z):
            P[i, j,k] = model.decision_function(np.array([xi, yj,zk]).reshape([1,3]))
            if P[i, j,k]<0.05 and P[i, j,k]>-0.05:
                ax.scatter(xi, yj,zk, s=20,color='b',marker='o')

                
#    print (P)
#    # plot the margins
#ax.contour3D(X, Y,Z, P, colors='k',
#           levels=[-1, 0, 1], alpha=0.5,extend3d=True)
    
#plot_svc_decision_function(model, ax=ax)



def plot_contours(ax, clf, xx, yy, **params):
    """Plot the decision boundaries for a classifier.

    Parameters
    ----------
    ax: matplotlib axes object
    clf: a classifier
    xx: meshgrid ndarray
    yy: meshgrid ndarray
    params: dictionary of params to pass to contourf, optional
    """
    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    out = ax.contourf(xx, yy, Z, **params)
    return out



plt.show()