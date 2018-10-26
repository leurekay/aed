# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import time
import threading
from urllib import request

import numpy as np
url_root='http://47.99.132.9/'
N=1000

N_thread=10

def requests(num):
    
  
    data=np.random.randint(3000,8000,[12])
    data_str=str(data[0])
    for j in range(1,12):
 
        data_str+='-'+str(data[j])
    with request.urlopen(url_root+data_str) as f:
        data = f.read()

time_s=time.time()

thread_list = []
for i in range(N):
    t = threading.Thread(target=requests,args=(1,))
    thread_list.append(t)

for t in thread_list:
    t.start()
    t.join()



time_e=time.time()
time_tot=time_e-time_s
time_avg=time_tot/N
