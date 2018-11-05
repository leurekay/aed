#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 15:30:27 2018

@author: dirac
"""

import time
import threading
from  multiprocessing import Pool
from urllib import request
import numpy as np
import random

#url_root='http://192.168.11.89:8000/'
#url_root='http://localhost:8000/'
#url_root='http://47.98.143.170:8000/'
url_root='http://47.99.132.9/'

N=10000

N_process=10

box=[]

def requests(num):
    global box
    for i in range(num):
        print (i)
        data_str=str(random.randint(3000,9000))
        for _ in range(1,12):
     
            data_str+='-'+str(random.randint(3000,9000))
        with request.urlopen(url_root+data_str) as f:
            data = f.read()
            box.append(1)



time_s=time.time()

p=Pool(N_process)
log=p.map(requests,[N//N_process]*N_process)

p.close()
p.join()



time_e=time.time()
time_tot=time_e-time_s
time_avg=time_tot/N
