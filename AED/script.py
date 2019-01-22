# -*- coding: utf-8 -*-
"""
Created on Thu Aug 09 09:41:25 2018

@author: zee
"""

import os
import csv
import numpy as np
import pandas as pd

N=5 # N entry for each statue of  a device
STEP=3
aed='3_73154011678'
statue='0'


aed_list=os.listdir('./')
aed_list=filter(lambda x: '.' not in x, aed_list)
statue_list=['0','1','2','3']

def oneOperate(aed,statue):
    step=STEP
    path=os.path.join(aed,statue+'.txt')
    f=open(path,'r')
    txt=f.readlines()
#    f.close()
    
    box=[]
    for entry in txt:
        if 'ART Data' in entry:
            entry=entry.split('*B,')[-1].split('&')[0]
            ss=entry.split(',')
            if len(ss)==3:               
                box.append(entry)
            else:
                pass
    
    for entry in box:
        if entry.split(',')[0] != statue:
            print ('%s,%s has error'%(aed,statue))
    
    atLeast=step*(N-1)+1
    if atLeast>len(box):
        print ('we need at least %d datas,but there are %d '%(atLeast,len(box)))
        step-=2
    
    log=[]    
    for i in range(N):
        entry=box[i*step]
        entry=aed.split('_')[-1]+','+statue+','+entry
        log.append(entry)
    return log
    
#b=oneOperate(aed,statue)
box=[]
for aed in aed_list:
    for statue in statue_list:
        try:
            ooxx=oneOperate(aed,statue)
            box.extend(ooxx)
        except IOError as e:
            print ('IOError',e)
        
        
        
writer=open('monitor_log.txt','w')
for line in box:   
    writer.write(line+'\n')
writer.close()

mat=[]
for i in box:
    temp=[]
    ii=i.split(',')
    for j in ii:
        temp.append(int(j))
    mat.append(temp)
mat=np.array(mat)

df =pd.DataFrame(mat,columns=['AED_ID','Display','Statue_monitor','RGB_1','RGB_2'],index=None)
df.to_excel('monitor_data.xlsx')
