# -*- coding: utf-8 -*-


from django.conf.urls import url
import views
urlpatterns = [
    url(r'^$', views.pp),
    url(r'^index/$', views.index),
    url(r'^index2/$', views.index2),
    url(r'^add/$', views.add),
]
