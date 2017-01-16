# -*- coding: utf-8 -*-
"""
Created on Sat Jan 07 17:04:27 2017
@author: jpelda"""

"""these values may not been sorted, the pathWays will not be sorted too!"""
import os
from DataIO import DataIO
from Heatnet_Consumptionprofiles import Heatnet_Consumptionprofiles

class Consumer():
    def __init__(self, index,
                 heat_exchangerModel,
                 start_point,
                 end_point,
                 start_x,
                 start_y,
                 end_x,
                 end_y,
                 heat_consumptionProfile,
                 heat_consumptionAverage):


        self.index = index
        self.heat_exchangerModel = heat_exchangerModel
        self.start_point = start_point
        self.end_point = end_point
        self.start_x = start_x
        self.start_y  = start_y
        self.end_x = end_x
        self.end_y = end_y
        self.heat_consumptionProfile = heat_consumptionProfile
        self.heat_consumptionAverage = heat_consumptionAverage


    def index(self, i = slice(None,None)):
              return self.__dataArray['index'][i]
    def heat_exchangerModel(self, i = slice(None,None)):
              return self.__dataArray['heat_exchangerModel'][i]
    def start_point(self, i = slice(None,None)):
              return self.__dataArray['start_point'][i]
    def end_point(self, i = slice(None,None)):
              return self.__dataArray['end_point'][i]
    def start_x(self, i = slice(None,None)):
              return self.__dataArray['start_x'][i]
    def start_y(self, i = slice(None,None)):
              return self.__dataArray['start_y'][i]
    def end_x(self, i = slice(None,None)):
              return self.__dataArray['end_x'][i]
    def end_y(self, i = slice(None,None)):
              return self.__dataArray['end_y'][i]
    def heat_consumptionProfiles(self, i=slice(None,None)):
        return self.__dataArray['heat_consumptionProfile'][i]

    def heat_consumption(self, heatExProfile, i = slice(None,None)):
        heat_consumption=self.__heat_consumption.consumptionProfile(heatExProfile,i)
        return heat_consumption

    def heat_consumptionAverage(self, i = slice(None,None)):
              return self.__dataArray['heat_consumptionAverage'][i]

    def supplyFlow_setPath(self, i, knotNumbers):
        self.__supplyFlow_path.append([i, knotNumbers])
    def supplyFlow_getPath(self, i):
        return self.__supplyFlow_path[i][1]
    def returnFlow_setPath(self,i,knotNumbers):
        self.__returnFlow_path.append([i,knotNumbers])
    def returnFlow_getPath(self,i):
        return self.__returnFlow_path[i][1]