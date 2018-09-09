# -*- coding: utf-8 -*-
"""
Python 2.7.14
"""



def rgb2statue(rgb1,rgb2):
    """
    rgb1:int
    rgb2:int
    """
    th1=4328
    th2=4012
    if rgb1==0 and rgb2==0:
        return 4 #monitor location error
    
    if rgb1<th1:
        if rgb2<th2:
            return 0#good
        else:
            return 2#only AED error
    else:
        if rgb2<th2:
            return 1#only Battery error
        else:
            return 3#both error