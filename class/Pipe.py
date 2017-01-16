#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 14 12:43:40 2017

@author: johannes
"""


class Pipe():
    def __init__(self, index,
                 start_x,
                 start_y,
                 end_x,
                 end_y,
                 start_point,
                 end_point,
                 length,
                 diameter_inner,
                 diameter_outer,
                 start_height,
                 end_height,
                 heatTransitionCoefficient,
                 roughness
                 ):
        self.index = index
        self.start_x = start_x
        self.start_y = start_y
        self.end_x = end_x
        self.end_y = end_y
        self.start_point = start_point
        self.end_point = end_point
        self.length = length
        self.diameter_inner = diameter_inner
        self.diameter_outer = diameter_outer
        self.start_height = start_height
        self.end_height = end_height
        self.heatTransitionCoefficient = heatTransitionCoefficient
        self.roughness = roughness

    def setHeatflow(self, i, heatFlow):
        print('********i: ' + str(i) + ' pipeIndex: ' + str(self.index) +
              ' heatFlow: ' + str(heatFlow))
        self.__heatflow += heatFlow

    def getHeatflow(self):
        return self.__heatflow


#    def index(self, i = slice(None,None)):
#        return self.__dataArray['index'][i]
#    def start_x(self, i = slice(None,None)):
#        return self.__dataArray['start_x'][i]
#    def start_y(self, i = slice(None,None)):
#        return self.__dataArray['start_y'][i]
#    def end_x(self, i = slice(None,None)):
#        return self.__dataArray['end_x'][i]
#    def end_y(self, i = slice(None,None)):
#        return self.__dataArray['end_y'][i]
#    def start_point(self, i = slice(None,None)):
#        return self.__dataArray['start_point'][i]
#    def end_point(self, i = slice(None,None)):
#        return self.__dataArray['end_point'][i]
#    def length(self, i = slice(None,None)):
#        return self.__dataArray['length'][i]
#    def inner_diameter(self, i = slice(None,None)):
#        return self.__dataArray['inner_diameter'][i]
#    def outer_diameter(self, i = slice(None,None)):
#        return self.__dataArray['outer_diameter'][i]
#    def start_height(self, i = slice(None,None)):
#        return self.__dataArray['start_height'][i]
#    def end_height(self, i = slice(None,None)):
#        return self.__dataArray['end_height'][i]
#    def heatTransitionCoefficient(self, i = slice(None,None)):
#        return self.__dataArray['heatTransitionCoefficient'][i]
#    def roughness(self, i = slice(None,None)):
#        return self.__dataArray['roughness'][i]
