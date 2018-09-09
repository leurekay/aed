# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 03:06:30 2018

@author: zee
"""

import  numpy as np
import matplotlib.pyplot as plt 

f=open('jiaozhun.txt')
tex=f.readlines()
data=[line.split(',') for line in tex]
x=np.array(data,'int')


fig=plt.figure(figsize=(12,12))
plt.subplot(221)
plt.scatter(x[:,0],x[:,1],s=55,facecolor='w',edgecolors='r',marker='o')
plt.title('R',fontsize=20)

plt.subplot(222)
plt.scatter(x[:,2],x[:,3],s=55,facecolor='w',edgecolors='g',marker='o')
plt.title('G',fontsize=20)

plt.subplot(223)
plt.scatter(x[:,4],x[:,5],s=55,facecolor='w',edgecolors='b',marker='o')
plt.title('B',fontsize=20)
plt.savefig('jiaozhun.jpg')