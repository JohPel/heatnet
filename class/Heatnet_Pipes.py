# -*- coding: utf-8 -*-
"""
Created on Sat Jan 07 16:50:22 2017
@author: jpelda"""
import os
from DataIO import DataIO
import numpy as np

class Heatnet_Pipes():

    def __init__(self,
                filename = os.getcwd() + os.sep + 'heatnet_pipes.csv',
                startrow = 1,
                dtype = {'names':(
                                'index',
                                'start_x',
                                'start_y',
                                'end_x',
                                'end_y',
                                'start_point',
                                'end_point',
                                'length',
                                'inner_diameter',
                                'outer_diameter',
                                'start_height',
                                'end_height',
                                'heatTransitionCoefficient',
                                'roughness',
                                ),
                        'formats':(
                                'i',
                                'U30',
                                'U30',
                                'U30',
                                'U30',
                                'i',
                                'i',
                                'f',
                                'f',
                                'f',
                                'f',
                                'U30',
                                'f',
                                'f',
                                )},
                columnofdate = None,
                dateformat = 'None'):

        self.__filename = filename
        self.__startrow = startrow
        self.__columnofdate = columnofdate
        self.__dateformat = dateformat

        self.__dataArray = DataIO(os.getcwd() + os.sep + 'input', os.getcwd() + os.sep + 'output').importCSV('heatnet_pipes.csv', dtype, startrow = startrow, columnofdate = columnofdate, dateformat = dateformat)

        self.__heatflow=np.zeros([36000,len(self.__dataArray)+1])

    def index(self, i = slice(None,None)):
              return self.__dataArray['index'][i]
    def start_x(self, i = slice(None,None)):
              return self.__dataArray['start_x'][i]
    def start_y(self, i = slice(None,None)):
              return self.__dataArray['start_y'][i]
    def end_x(self, i = slice(None,None)):
              return self.__dataArray['end_x'][i]
    def end_y(self, i = slice(None,None)):
              return self.__dataArray['end_y'][i]
    def start_point(self, i = slice(None,None)):
              return self.__dataArray['start_point'][i]
    def end_point(self, i = slice(None,None)):
              return self.__dataArray['end_point'][i]
    def length(self, i = slice(None,None)):
              return self.__dataArray['length'][i]
    def inner_diameter(self, i = slice(None,None)):
              return self.__dataArray['inner_diameter'][i]
    def outer_diameter(self, i = slice(None,None)):
              return self.__dataArray['outer_diameter'][i]
    def start_height(self, i = slice(None,None)):
              return self.__dataArray['start_height'][i]
    def end_height(self, i = slice(None,None)):
              return self.__dataArray['end_height'][i]
    def heatTransitionCoefficient(self, i = slice(None,None)):
              return self.__dataArray['heatTransitionCoefficient'][i]
    def roughness(self, i = slice(None,None)):
              return self.__dataArray['roughness'][i]



    def setHeatflow(self,i, pipeIndex, heatFlow):
        print('********i: '+str(i)+' pipeIndex: ' +str(pipeIndex)+' heatFlow: '+str(heatFlow))
        self.__heatflow[i][pipeIndex]+=heatFlow

    def getHeatflow(self,i,pipeIndex):
        return self.__heatflow[i][pipeIndex]
