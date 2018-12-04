# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.db import connection


def getDataFromSQL(sql):
    """
    根据sql语句获取数据库的返回数据
    """
    cursor = connection.cursor()
    cursor.execute(sql)
    return list(cursor.fetchall())
