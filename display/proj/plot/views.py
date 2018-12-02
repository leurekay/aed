from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.http import HttpResponseRedirect,HttpResponse
from django.views.decorators.csrf import csrf_exempt

import time
import django.utils.timezone as timezone
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')

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

     
def add(request):

    color= request.GET['color']
    uid=request.GET['uid']
    uid=str(uid)
  
    select=AlgorithmRgb.objects.filter(Uid=uid)
    select.all().order_by("Datetime")
    t=map(lambda x:x.Datetime,select)
    y=select.values(color)
    y=map(lambda x : x[color],y)
    fig=plt.figure(figsize=[18,9])
    plt.subplot(111)
    plt.plot(t,y,'r',linewidth=1)
#    plt.legend(fontsize=20)
    plt.xlabel('Time',fontsize=15)
    img_path=os.path.join(media_dir,uid+color+'.jpg')
    plt.savefig(img_path)
    time.sleep(1)
    target_name=os.path.join('/static/media/',uid+color+'.jpg')
    return HttpResponse('<img src="%s" height="1800" width="3600" />  <br/>'%(target_name))

if __name__=='__main__':
    pass
#    df=pull_data(id1)
#    df2=pull_data(id1)