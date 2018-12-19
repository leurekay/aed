#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 09:55:29 2018

@author: ly
"""

import numpy as np
import requests



content={'sn':862151033509082}   
r=requests.get('http://aed.yuwell.com/home/Calibration',params=content)
print (r.url)
print (r.text)