# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 10:34:19 2018

@author: zee
"""



th_r1=1173
th_r2=1007
th_g1=948
th_g2=824
th_b1=1236
th_b2=1173


def good_bad(x,x_,th):
        if (x-x_)<th:
            return 1
        else:
            return -1
        
def statue_vote(r,r_,g,g_,b,b_,th_r,th_g,th_b):
    """
    combine the results of R,G,B by vote
    
    return:
        True: Battery(Meachine) is good
        Fale: Battery(Meachine) is bad
    """
    score=good_bad(r,r_,th_r)+good_bad(g,g_,th_g)+good_bad(b,b_,th_b)
    if score>0:
        return True
    else:
        return False
    
    
def statue(r1,r1_,r2,r2_,g1,g1_,g2,g2_,b1,b1_,b2,b2_):
    battery=statue_vote(r1,r1_,g1,g1_,b1,b1_,th_r1,th_g1,th_b1)
    meachine=statue_vote(r2,r2_,g2,g2_,b2,b2_,th_r2,th_g2,th_b2)
    
    if battery :
        if meachine:
            return 0#both good
        else:
            return 2#only meachine is bad
    else:
        if meachine:
            return 1#only battery is bad
        else:
            return 3#both bad
    