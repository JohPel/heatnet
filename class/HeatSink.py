#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 15 12:41:52 2017

@author: johannes
"""
import os
import inspect
from DataIO import DataIO
from Consumer import Consumer

class HeatSink():
    def __init__(self):
        self.__filepath = os.path.dirname(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))) + os.sep

        self._instancesConsumer = []

        self.__importConsumer()

    def __importConsumer(self,
                filename = 'consumer.csv',
                startrow = 1,
                dtype = {'names':(
                                'index',
                                'heat_exchangerModel',
                                'start_point',
                                'end_point',
                                'start_x',
                                'start_y',
                                'end_x',
                                'end_y',
                                'heat_consumptionProfile',
                                'heat_consumptionAverage',
                                ),
                        'formats':(
                                'i',
                                'U30',
                                'i',
                                'i',
                                'U30',
                                'U30',
                                'U30',
                                'U30',
                                'U30',
                                'U30',
                                )},
                columnofdate = None,
                dateformat = 'None'):

        print(self.__filepath)
        dataArray = DataIO(self.__filepath + 'input', self.__filepath + 'output').importCSV(filename, dtype, startrow = startrow, columnofdate = columnofdate, dateformat = dateformat)

        for item in dataArray:
            self._instancesConsumer.append(Consumer(item['index'],
                                                    item['heat_exchangerModel'],
                                                    item['start_point'],
                                                    item['end_point'],
                                                    item['start_x'],
                                                    item['start_y'],
                                                    item['end_x'],
                                                    item['end_y'],
                                                    item['heat_consumptionProfile'],
                                                    item['heat_consumptionAverage']))


    def consumer(self, i = slice(None,None)):
        return self._instancesConsumer[i]

    def __consumerProfile(self):
        pass
