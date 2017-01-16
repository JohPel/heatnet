#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 16:22:28 2017

@author: johannes
"""

import sys
import os

import numpy as np
import time as time

sys.path.append(os.getcwd() + os.sep + 'class')
from DataIO import DataIO
from Network import Network
from HeatSink import HeatSink
from Heatnet_Consumptionprofiles import Heatnet_Consumptionprofiles

metaData=DataIO(os.getcwd()+os.sep+'meta',os.getcwd()+os.sep+'meta')

network = Network()
print(network.pipes())
print(network.pipes(0).start_point)

heatsink = HeatSink()
print(heatsink.consumer(1))
print(heatsink.consumer(1))
#HeatExchanger=Heatnet_Heatexchanger()
#
##if not os.path.isfile(orderOfPipes.csv):
#for item in enumerate(HeatExchanger.index()):
#
#        start_point=HeatExchanger.start_point(item[0])
#        end_point=HeatExchanger.end_point(item[0])
#
#        supplyFlow=[]
#        returnFlow=[]
#
#        index=0
#        while index <= len(Pipes.index()):
#            for pipe_end_point, pipe_start_point, pipe_index in zip(Pipes.end_point(), Pipes.start_point(), Pipes.index()):
#                if start_point == pipe_end_point:
#                    start_point=pipe_start_point
#                    print('SF: '+str(pipe_index))
#                    supplyFlow.append(pipe_index)
#                    break
#            index=index+1
#
#        index=0
#        while index <=len(Pipes.index()):
#            for pipe_end_point, pipe_start_point, pipe_index in zip(Pipes.end_point(), Pipes.start_point(), Pipes.index()):
#               if end_point == pipe_start_point:
#                   end_point=pipe_end_point
#                   print('RF: '+str(pipe_index))
#                   returnFlow.append(pipe_index)
#                   break
#            index=index+1
#        HeatExchanger.supplyFlow_setPath(item[0],supplyFlow)
#        HeatExchanger.returnFlow_setPath(item[0],returnFlow)
#
#        print('SF'+str(HeatExchanger.supplyFlow_getPath(item[0])))
#        print('RF'+str(HeatExchanger.returnFlow_getPath(item[0])))
#
#
#startTime=time.clock()
#'''calculates the heat flow in each pipe'''
#start=0
#End=Heatnet_Consumptionprofiles()
##while Start < len(End.date()):
#while start < 10:
#    print('###############Date: ' +End.date(start).strftime('%d.%m.%y %H:%M'))
##    print('###############Time: ' +str(start))
#    for index, heatExchangerProfile in enumerate(HeatExchanger.heat_consumptionProfiles()):
#        for pipeNumber in HeatExchanger.supplyFlow_getPath(index):
#            print('HeatConsumption: ' +str(HeatExchanger.heat_consumption(heatExchangerProfile,start)))
#            Pipes.setHeatflow(start,pipeNumber,HeatExchanger.heat_consumption(heatExchangerProfile,start))
#            print('SUMMEHeatConsumption: '+'time: ' +str(start)+' pipeNumber: '+str(pipeNumber)+' HeatFlow: ' +str(Pipes.getHeatflow(start,pipeNumber)))
#
#
#
#    start=start+1
#
#endTime=time.clock()
#
#print(endTime-startTime)
