#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 15:05:43 2018

@author: ly
"""

import re
import os
import numpy as np
import pandas as pd
import collections


path='RGB_93.txt'
save_excel_path='data4-5.xlsx'
    

with open(path,'r') as f:
    txt=f.readlines()


def process_line(line):

    line=line.replace(' ',',')
    line=line.replace('R:','')
    line=line.replace('G:','')
    line=line.replace('B:','')
    line=line.replace('C:','')
    line=line.split('&&')[0].split(',')
    if len(line)==16:
        line=map(lambda x:int(x),line)
        return line
    else:
        return []

data=map(lambda x:process_line(x),txt)
data=filter(lambda x:len(x),data)
data=np.array(data)

features=['R1','R1_','R2','R2_','G1','G1_','G2','G2_','B1','B1_','B2','B2_','C1','C1_','C2','C2_']

df=pd.DataFrame(data,columns=features)

df.to_excel(path.replace('txt','xlsx'),index=False)   


