#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 16:10:21 2018

@author: ly
"""

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

import time
import os

import lr_pred
import svm_pred



@csrf_exempt
def predict(request,param):
    zipdata=param.split('-')
    zipdata=map(lambda x:int(x),zipdata)
    statue1,statue_battery1,statue_meachine1,confidence_battery1,confidence_meachine1=lr_pred.statue_judge(zipdata)
    statue2,statue_battery2,statue_meachine2,confidence_battery2,confidence_meachine2=svm_pred.statue_judge(zipdata)
    return JsonResponse({'input': param, 
                         'statue1':statue1,
                         'statue_battery1':statue_battery1,
                         'statue_meachine1':statue_meachine1,
                         #'confidence_battery':confidence_battery,
                         #'confidence_meachine':confidence_meachine,
                         'statue2':statue2,
                         'statue_battery2':statue_battery2,
                         'statue_meachine2':statue_meachine2,
                         #'confidence_battery':confidence_battery,
                         #'confidence_meachine':confidence_meachine
                         })



@csrf_exempt
def lr(request,param):
    zipdata=param.split('-')
    zipdata=map(lambda x:int(x),zipdata)
    statue,statue_battery,statue_meachine,confidence_battery,confidence_meachine=lr_pred.statue_judge(zipdata)
    
    return JsonResponse({'input': param, 
                         'statue':statue,
                         'statue_battery':statue_battery,
                         'statue_meachine':statue_meachine,
                         #'confidence_battery':confidence_battery,
                         #'confidence_meachine':confidence_meachine
                         })


    
    
@csrf_exempt
def svm(request,param):
    zipdata=param.split('-')
    zipdata=map(lambda x:int(x),zipdata)
    statue,statue_battery,statue_meachine,confidence_battery,confidence_meachine=svm_pred.statue_judge(zipdata)
    
    return JsonResponse({"input": param, 
                         "statue":statue,
                         'statue_battery':statue_battery,
                         'statue_meachine':statue_meachine,
                         #'confidence_battery':confidence_battery,
                         #'confidence_meachine':confidence_meachine
                         })