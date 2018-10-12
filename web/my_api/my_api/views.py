#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 16:10:21 2018

@author: ly
"""

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import time

@csrf_exempt
def test_api(request,param):
    param=param.split('-')
    time.sleep(0.2)
    return JsonResponse({"input": param, "out_statue":int(param[0])%4})

