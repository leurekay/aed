# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 16:09:23 2018

@author: zee
"""

import time
from  multiprocessing import Pool

base_time=time.time()

def queen(L=9):
    s=time.time()-base_time
    box=[]
    def dfs(a,L):
        if len(a)==L:
            box.append(a)
        else:
            tt=[x for x in range(L) if x not in a]
            for i in tt:
                count=len(a)
                for k in range(len(a)):
                    if abs(i-a[k])!=abs(len(a)-k):
                        count-=1
                if count==0:
                    
                    dfs(a+[i],L)
    
    dfs([],L)
    e=time.time()-base_time
    print ('%.3f--%.3f'%(s,e))
    return box

aa=queen(1)

p=Pool(4)
for i in range(5):
    p.apply_async(queen, args=(8,))
print('Waiting for all subprocesses done...')
p.close()
p.join()
