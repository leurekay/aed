#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 16:10:21 2018

@author: ly
"""

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

import time
from datetime import datetime

import django.utils.timezone as timezone
import os
import math

import lr_pred
import svm_pred
import neural_pred
import transition_pred

from models import RGB


def timestamp2beijing(t):
    time2 = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(t))
    return time2


def operate_db(kwargs):
    select=RGB.objects.filter(Uid=kwargs['Uid'],R1C=kwargs['R1C'],R2C=kwargs['R2C'],G1C=kwargs['G1C'],G2C=kwargs['G2C'])
    if len(select)==0:
        b_good=[[kwargs['R1C'],kwargs['G1C'],kwargs['B1C']]]
        b_bad=[] 
        m_good=[[kwargs['R2C'],kwargs['G2C'],kwargs['B2C']]]
        m_bad=[]
        return {'b_good':b_good,'b_bad':b_bad,'m_good':m_good,'m_bad':m_bad}
        
        
    select.all().order_by("Datetime")
    select=select.values('R1','R1C','R2','R2C','G1','G1C','G2','G2C','B1','B1C','B2','B2C','Statue2')
    select=list(select)
    select=select[-100:]

    b_good=[]
    b_bad=[] 
    m_good=[]
    m_bad=[]
   
    for dic in select:
        if dic['Statue2']==0 or dic['Statue2']==2:
            b_good.append([dic['R1'],dic['G1'],dic['B1']])
        if dic['Statue2']==1 or dic['Statue2']==3:
            b_bad.append([dic['R1'],dic['G1'],dic['B1']])
        if dic['Statue2']==0 or dic['Statue2']==1:
            m_good.append([dic['R2'],dic['G2'],dic['B2']])
        if dic['Statue2']==2 or dic['Statue2']==3:
            m_bad.append([dic['R2'],dic['G2'],dic['B2']])
#    s=map(lambda x : x['R1'],select)
    return {'b_good':b_good,'b_bad':b_bad,'m_good':m_good,'m_bad':m_bad}

@csrf_exempt
def predict(request,param):
    zipdata=param.split('-')
    uid=zipdata[12]
    zipdata=zipdata[:12]

    zipdata=map(lambda x:int(x),zipdata)
    zipdata_ln=map(lambda x:math.log(x),zipdata)

    keys=['R1','R1C','R2','R2C','G1','G1C','G2','G2C','B1','B1C','B2','B2C','Uid']
    mapping=dict(zip(keys,zipdata+[uid]))
    
    
    
    
    past_data=operate_db(mapping)
    statue2,statue_battery2,statue_meachine2,confidence_battery2,confidence_meachine2=transition_pred.total_judge(zipdata,past_data)
#    print ('=========',s)
    
    statue1,statue_battery1,statue_meachine1,confidence_battery1,confidence_meachine1=lr_pred.statue_judge(zipdata_ln)
#    statue2,statue_battery2,statue_meachine2,confidence_battery2,confidence_meachine2=svm_pred.statue_judge(zipdata)
    statue3,confidence3=neural_pred.statue_judge(zipdata)
    
    t=int(time.time())
    date1=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(t))
    date1=datetime.strptime(date1,"%Y-%m-%d %H:%M:%S")
    rgb=RGB(Uid=uid,Timestamp=int(time.time()),Datetime=date1,
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