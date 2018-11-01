#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 16:42:57 2018

@author: ly
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from keras.layers import Input, Dense,Dropout,Multiply,Lambda
from keras.models import Model,load_model

from keras.utils import to_categorical



model_path='model/neural.h5'
model=load_model(model_path)
box=[]
for layer in model.layers:
    box.append(layer.get_weights())
