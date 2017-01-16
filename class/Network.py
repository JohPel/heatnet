# -*- coding: utf-8 -*-
"""
Created on Sat Jan 07 16:50:22 2017
@author: jpelda"""


import sys
import inspect
import os
import numpy as np

print((os.path.dirname(os.path.dirname(
                os.path.abspath(inspect.getfile(inspect.currentframe())))) +
                os.sep +
                'class'))
from Pipe import Pipe
from DataIO import DataIO


class Network():


    def __init__(self):
        self.__filepath = os.path.dirname(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))) + os.sep
        
        self._instancesPipe = []

        self.__importPipes()


    def __importPipes(self,
                filename = 'heatnet_pipes.csv',
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
                                'diameter_inner',
                                'diameter_outer',
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


        dataArray = DataIO(self.__filepath + 'input', self.__filepath + 'output').importCSV(filename, dtype, startrow = startrow, columnofdate = columnofdate, dateformat = dateformat)

        for item in dataArray:
            self._instancesPipe.append(Pipe(item['index'],
                                            item['start_x'],
                                            item['start_y'],
                                            item['end_x'],
                                            item['end_y'],
                                            item['start_point'],
                                            item['end_point'],
                                            item['length'],
                                            item['diameter_inner'],
                                            item['diameter_outer'],
                                            item['start_height'],
                                            item['end_height'],
                                            item['heatTransitionCoefficient'],
                                            item['roughness']
                                            ))

    def pipes(self, i = slice(None, None)):
        return self._instancesPipe[i]
