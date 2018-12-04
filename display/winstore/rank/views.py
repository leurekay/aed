# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import JsonResponse
from models import *
import datetime


def index(request):
    """
    绑定网站首页
    """
    return render(request, 'rank.html')


def getWinstoreRegions(request):
    """
    根据接收到的GET请求返回region的取值集合
    """
    # 构造SQL语句
    sql = 'SELECT DISTINCT region FROM winstore_rank'
    # 默认regions的key和value相同
    regions = {}
    try:
        result = getDataFromSQL(sql)
        result = [r[0] for r in result]
        for key in result:
            regions[key] = key
    except Exception as e:
        print('getWinstoreRegions ERROR: ' + str(e))
        regions['EN-US'] = 'EN-US'
    return JsonResponse(regions)


def getWinstoreCharts(request):
    """
    根据接收到的GET请求返回chart的取值集合
    """
    # 构造SQL语句
    sql = 'SELECT DISTINCT chart FROM winstore_rank'
    # 默认charts的key和value相同
    charts = {}
    try:
        result = getDataFromSQL(sql)
        result = [r[0] for r in result]
        for key in result:
            charts[key] = key
    except Exception as e:
        print('getWinstoreCharts ERROR: ' + str(e))
        charts['Free'] = 'Free'
    return JsonResponse(charts)


def getWinstoreCategories(request):
    """
    根据接收到的GET请求返回category的取值集合
    """
    # 构造SQL语句
    sql = 'SELECT DISTINCT category FROM winstore_rank'
    # 默认categories的key和value相同
    categories = {}
    try:
        result = getDataFromSQL(sql)
        result = [r[0] for r in result]
        for key in result:
            categories[key] = key
    except Exception as e:
        print('getWinstoreCategories ERROR: ' + str(e))
        categories['Education'] = 'Education'
    return JsonResponse(categories)


def getWinstoreApps(request):
    """
    根据接收到的GET请求返回app的取值集合
    """
    # 构造SQL语句
    sql = 'SELECT DISTINCT appName FROM winstore_rank'
    # 默认appNames的key和value相同
    appNames = {}
    try:
        result = getDataFromSQL(sql)
        result = [r[0] for r in result]
        for key in result:
            appNames[key] = key
    except Exception as e:
        print('getWinstoreApps ERROR: ' + str(e))
        appNames['QQ'] = 'QQ'
    return JsonResponse(appNames)


def getWinstoreRank(request):
    """
    根据接收到的GET请求返回对应app的排名数据
    """
    # 从GET请求中获取参数
    region = request.GET.get("region", "EN-US")
    chart = request.GET.get("chart", "Free")
    category = request.GET.get("category", "Education")
    beginDate = request.GET.get("beginDate", "2018-01-22")
    endDate = request.GET.get("endDate", "2018-02-02")
    appNames = request.GET.get("appNames", "QQ").split("@")
    # 构造SQL语句
    sqlTemp = 'SELECT the_date, rank FROM winstore_rank WHERE ' \
              'region="%s" AND chart="%s" AND category="%s" AND ' \
              'the_date BETWEEN "%s" AND "%s" AND ' \
              'appName=' % (region, chart, category, beginDate, endDate)

    # 以每个appName作为key，对应的排名数据列表作为value
    appRank = {}
    for appName in appNames:
        sql = sqlTemp + '"' + appName + '"'
        try:
            result = getDataFromSQL(sql)
            # 根据数据库返回的结果将缺少rank数据的日期补0
            result = addZeroToRank(beginDate, endDate, result)
            appRank[appName] = result
        except Exception as e:
            print('getWinstoreRank ERROR: ' + str(e))
    return JsonResponse(appRank)


def addZeroToRank(beginDate, endDate, result):
    """
    以beginDate和endDate为日期的起始，将result中缺少的日期补全，同时设定排名为0
    Param：
        beginDate: 开始日期字符串，“2018-01-23”
        endDate: 结束日期字符串， “2018-02-02”
        result: 形如[(date, 23L), (date, 12L), [date, 3L]......]
    Return：
        按照日期顺序排列的排名数据，缺省排名为0
    """
    # 将日期字符串转变为date类型数据，方便日期加减
    y, m, d = [int(i) for i in beginDate.split("-")]
    begin = datetime.date(y, m, d)
    y, m, d = [int(i) for i in endDate.split("-")]
    end = datetime.date(y, m, d)
    current = begin
    # 获取result中的日期，方便进行判断
    resultTemp = [r[0] for r in result]
    while current <= end:
        if not (current in resultTemp):
            result.append((current, 0))
        current += datetime.timedelta(days=1)
    result.sort(key=lambda x: x[0])
    return [int(r[1]) for r in result]
