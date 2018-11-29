#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 16:10:21 2018

@author: ly
"""

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

import time
import datetime
import django.utils.timezone as timezone
import os

import lr_pred
import svm_pred
import neural_pred

from models import RGB

@csrf_exempt
def predict(request,param):
    zipdata=param.split('-')
    uids=zipdata[12:]
    zipdata=zipdata[:12]
    zipdata=map(lambda x:int(x),zipdata)
    statue1,statue_battery1,statue_meachine1,confidence_battery1,confidence_meachine1=lr_pred.statue_judge(zipdata)
    statue2,statue_battery2,statue_meachine2,confidence_battery2,confidence_meachine2=svm_pred.statue_judge(zipdata)
    statue3,confidence3=neural_pred.statue_judge(zipdata)
    
    rgb=RGB(Uid=uids[0],Timestamp=int(time.time()),Datetime=timezone.now(),
            R1=zipdata[0],R1C=zipdata[1],R2=zipdata[2],R2C=zipdata[3],
            G1=zipdata[4],G1C=zipdata[5],G2=zipdata[6],G2C=zipdata[7],
            B1=zipdata[8],B1C=zipdata[9],B2=zipdata[10],B2C=zipdata[11],
            Statue1=statue1,Statue2=statue2,Statue3=statue3)
    rgb.save()
    
    return JsonResponse({'input': param, 
                         'statue1':statue1,
                         'confidence1':float(confidence_battery1*confidence_meachine1),
                         'statue_battery1':statue_battery1,
                         'statue_meachine1':statue_meachine1,
                         #'confidence_battery':confidence_battery,
                         #'confidence_meachine':confidence_meachine,
                         'statue2':statue2,
                         'confidence2':float(confidence_battery2*confidence_meachine2),
                         'statue_batterys2':statue_battery2,
                         'statue_meachine2':statue_meachine2,
                         #'confidence_battery':confidence_battery,
                         #'confidence_meachine':confidence_meachine,
                         'statue3':statue3,
                         'confidence3':float(confidence3),
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