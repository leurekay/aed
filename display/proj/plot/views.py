from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.http import HttpResponseRedirect,HttpResponse
from django.views.decorators.csrf import csrf_exempt

import time
import datetime
from datetime import timedelta
import django.utils.timezone as timezone
import os
import pandas as pd
import numpy as np
#from sklearn import linear_model
#import matplotlib.pyplot as plt
#plt.switch_backend('agg')

import sqlite3

from django.conf import settings
from models import AlgorithmRgb
try:
    basedir=settings.BASE_DIR
except:
    basedir='..'
    
    
db_path=os.path.join(basedir,'static/test.sqlite3')
media_dir=os.path.join(basedir,'static/media')

table_name='algorithm_rgb'
id1='868994037706145'
conn = sqlite3.connect(db_path)
#cur = conn.cursor()
#sql_command='SELECT * FROM '+table_name+' WHERE Uid='+id1
#df = pd.read_sql_query(sql_command, conn)


@csrf_exempt
def p(request,param):
    
    return JsonResponse({'input': param, 
                         'statue3':4,
                         })
    
def pp(request):
    
    return JsonResponse({'input': 'fghjk', 
                         'statue3':4,
                         })


def pull_data(uid):
    sql_command='SELECT * FROM '+table_name+' WHERE Uid='+uid
    df = pd.read_sql_query(sql_command, conn)
    return df    
    
def index(request):
    return render(request, 'index.html')

def index2(request):
    return render(request, 'index2.html')

def index3(request):
    return render(request, 'index3.html')
     
def add(request):

    color= request.GET['color']
    uid=request.GET['uid']
    uid=str(uid)
  
    select=AlgorithmRgb.objects.filter(Uid=uid)
    select.all().order_by("Datetime")
    t=map(lambda x:x.Datetime,select)
    y=select.values(color)
    y=map(lambda x : x[color],y)
#    fig=plt.figure(figsize=[18,9])
#    plt.subplot(111)
#    plt.plot(t,y,'r',linewidth=1)
##    plt.legend(fontsize=20)
#    plt.xlabel('Time',fontsize=15)
#    img_path=os.path.join(media_dir,uid+color+'.jpg')
#    plt.savefig(img_path)
#    time.sleep(1)
#    target_name=os.path.join('/static/media/',uid+color+'.jpg')
#    return HttpResponse('<img src="%s" height="1800" width="3600" />  <br/>'%(target_name))
    return HttpResponse('hhhhhhhhhhhhhhhhhhhhhhhhhh')


#def future_pred(past_t,past_y,future_t):
#    past_t=np.array(past_t).reshape(-1,1)
#    past_y=np.array(past_y).reshape(-1,1)
#    past_ln=np.log(past_t)
#    reg = linear_model.LinearRegression()
#    reg.fit(past_t,past_ln)
#    k=reg.coef_[0]
#    b=reg.intercept_
#    A=np.exp(b)
#    print (A,k)
#    def fit(t):
#        return int(A*np.exp(k*t))
#    ret=[fit(x) for x in future_t]
#    return ret


def getData(request):
    max_points=1000
    beginDate = request.GET.get("beginDate", "2018-01-22")
    endDate = request.GET.get("endDate")
    
    endDate_=datetime.datetime.strptime(endDate, "%Y-%m-%d")
    endDate_=endDate_+timedelta(days=1)
    endDate=endDate_
    
    color=request.GET.get("color")
    uid=request.GET.get("uid")

    select=AlgorithmRgb.objects.filter(Uid=uid)
    select=select.filter(Datetime__range=[beginDate, endDate])
    select.all().order_by("Datetime")
#    t=map(lambda x:x.Datetime,select)
    t=map(lambda x:int(1000*x.Timestamp),select)
    y=select.values(color)
    y=map(lambda x : x[color],y)
    
    color_cali=color+'C'
    z=select.values(color_cali)
    z=map(lambda x : x[color_cali],z)
    
    n=len(y)
    if n==0:
        return []
    interval=int(np.ceil(n/float(max_points)))
    indexs=range(0,n,interval)

    print(endDate,color,uid,interval)
    
#    today=t[-1]
#    end=int(1000*time.mktime(endDate_.timetuple()))
#    future_time=range(today,end,24*3600*1000)
#    ret=future_pred(t,y,future_time)
#    tz=[[future_time[i],ret[i]] for i in range(len(future_time))]
    
    ty=[[t[i],y[i]] for i in indexs]
    

    tt=[[1370131200000, 0.7695],
        [1370217600000, 0.7648],
        [1370304000000, 0.7645],
        [1370390400000, 0.7638],
        [1370476800000, 0.7549],
        [1370563200000, 0.7562],
        [1370736000000, 0.7574],
        [1370822400000, 0.7543],
        [1370908800000, 0.751],
        [1370995200000, 0.7498]]
#    appRank = {'value':ty,'calibration':tz}
    appRank = {'value':ty}
    return JsonResponse(appRank)














def getBigData(request):
    max_points=1000
    beginDate = request.GET.get("beginDate", "2018-01-22")
    endDate = request.GET.get("endDate")
    
    color=request.GET.get("color")
    uid=request.GET.get("uid")
    print(endDate,color,uid)

    select=AlgorithmRgb.objects.filter(Uid=uid)
    select=select.filter(Datetime__range=[beginDate, endDate])
    select.all().order_by("Datetime")
    t=map(lambda x:x.Datetime,select)
    y=select.values(color)
    y=map(lambda x : x[color],y)
    
    color_cali=color+'C'
    z=select.values(color_cali)
    z=map(lambda x : x[color_cali],z)
    
    n=len(y)
    if n==0:
        return []
    interval=int(np.ceil(n/float(max_points)))
#    indexs=range(0,n,interval)
    indexs=range(n)
    print(interval)
    
    
    
    ty=[[t[i],y[i]] for i in indexs]
    tz=[[t[i],z[i]] for i in indexs]
#    appRank = {'value':ty,'calibration':tz}
    appRank = {'value':ty}
    return JsonResponse(appRank)


if __name__=='__main__':
    pass
#    df=pull_data(id1)
#    df2=pull_data(id1)