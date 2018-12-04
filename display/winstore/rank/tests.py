# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import random
from django.db import connection
import os
from django.test import TestCase
# Create your tests here.
import datetime

test = [(datetime.date(2018, 1, 29), 23), (datetime.date(2018, 1, 28), 28),
        (datetime.date(2018, 2, 2), 56), (datetime.date(2018, 1, 27), 78)]

test.sort(key=lambda x: x[0])
print(test[:][0])


#
# regions = ['EN-US', 'ZH-CN']
# charts = ['Best-Selling', 'Free']
# categories = ['Education', 'Photo']
# appNames = ['QQ', 'Chrome', 'Firefox', 'Tim']
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "winstore.settings")
# cursor = connection.cursor()
#
# for day in range(1, 16):
#     for region in regions:
#         for chart in charts:
#             for category in categories:
#                 for appName in appNames:
#                     date = datetime.date(2018, 2, day)
#                     rank = random.randint(20, 50)
#                     sql = 'REPLACE INTO winstore_rank' \
#                           '(region, chart, category, the_date, appName, rank)' \
#                           ' VALUES ' \
#                           '("%s", "%s", "%s", "%s", "%s", %d)' % (region, chart, category, date, appName, rank)
#                     cursor.execute(sql)
