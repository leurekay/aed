# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 10:45:53 2018

@author: zee
"""

from distutils.core import setup
from Cython.Build import cythonize


# python setup.py build_ext --inplace
setup(
    ext_modules = cythonize("helloworld.pyx")
)