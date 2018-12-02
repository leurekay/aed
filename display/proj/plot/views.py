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
import sqlite3

from django.conf import settings
from models import AlgorithmRgb
try:
    basedir=settings.BASE_DIR
except:
    basedir='..'
    
    
db_path=os.path.join(basedir,'static/test.sqlite3')

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
  
    s=AlgorithmRgb.objects.filter(uid=id1)
    print(s[0])
#    df=pull_data(uid)
#    a=df.loc[0,'R1']

    return HttpResponse('222')

if __name__=='__main__':
    pass
#    df=pull_data(id1)
#    df2=pull_data(id1)