# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 11:55:49 2017

@author: jpelda
"""

import numpy as np

a = np.array([[3,1], [1,2]])
b = np.array([9,8])
x = np.linalg.solve(a, b)
print(x)

a = np.array([[-1,1,0,0,0,0,0,0,0,0],
              [0,-1,0,0,0,0,1,0,0,0],
              [0,0,0,0,1,0,0,-1,0,0],
              [0,-1,1,0,0,0,0,0,0,0],
              [0,0,-1,0,0,0,0,0,0,1],
              [0,0,0,1,0,0,0,0,-1,0],
              [0,0,0,-1,1,0,0,0,0,0],
              [0,0,0,0,-1,1,0,0,0,0]])

b = np.array([10,10,20,10,20,20,20,10])
q = np.array([10,10,20,10,20,20,20,10])
print("again")
print("hello")
x = np.linalg.solve(a,b)
print(x)