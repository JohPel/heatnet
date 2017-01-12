# -*- coding: utf-8 -*-
"""
Created on Fri Aug 19 20:30:03 2016

@author: johannes
"""

import csv
import os
import io
import numpy as np
import time
from datetime import datetime
from datetime import timedelta
from copy import copy
#from dbfread import DBF
#from Dictionaries import Dictionaries
#from TRY_Dictionary import TRY_Dictionary
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib import pyplot as plt
from datetime import datetime
from matplotlib import dates as dates
#from DataIO_Helper import DataIO_Helper

#from dbf import dbf

class DataIO():

    def __init__(self, filepath_import, filepath_export):
        '''
        DataIO for Import and Export of data
        '''
        self.__filepath_import = filepath_import
        self.__filepath_export = filepath_export

    def importCSV(self, filename_import, dtype = None, startrow = 0, delimiter=";", columnofdate=None, dateformat=None):
        '''
        imports CSV and replaces first comma start counting from right
        #######
        return:
            iterable object
        '''
        if os.path.isfile(self.__filepath_import + os.sep + os.path.splitext(filename_import)[0] + "_pointAsDec" + os.path.splitext(filename_import)[1]):
            '''opens file and reads it into memory'''
            start_time = time.clock()
            self.__dataArray = np.genfromtxt(self.__filepath_import + os.sep + os.path.splitext(filename_import)[0] + "_pointAsDec" + os.path.splitext(filename_import)[1],
                                             dtype = dtype,
                                             delimiter = delimiter,
                                             skip_header = startrow,
                                             converters = self.str2date(columnofdate = columnofdate, dateformat = dateformat))
            print(time.clock() - start_time)


        else:
            '''opens file and changes decimal seperator to point, delets all other points or commas: except of date --> saves file into input/<filename>+_pointAsDec'''
            self.__dataArray = ''
            self.__dataArrayHeader = ''
            with open(self.__filepath_import + os.sep + filename_import, encoding = 'utf-8-sig') as csvfile:
                readCSV = csv.reader(csvfile, delimiter = delimiter)

                start_time = time.clock()
                index = 0
                for row in readCSV:
                    '''saves the header of csv-file into self.__dataArrayHeader'''
                    self.__dataArrayHeader = self.__dataArrayHeader + delimiter.join(x for x in row) + '\n'
                    if   startrow - 2 < index:
                        break
                    index += 1


               # print(self.__dataArrayHeader)
                for row0 in readCSV:
                    row1 = []
                    for (index,item) in enumerate(row0):
                        if index == columnofdate:
                            row1.append(item)
                        else:
                            item = item.replace(",", ".")
                            item = item.replace(".","", item.count(".") - 1)
                            row1.append(item)
                    self.__dataArray = self.__dataArray +  delimiter.join(x for x in row1) + '\n'
                print(time.clock() - start_time)
                csvfile.close
                with open(self.__filepath_import + os.sep + os.path.splitext(filename_import)[0] + "_pointAsDec" + os.path.splitext(filename_import)[1], "w") as text_file:
                    text_file.write(self.__dataArrayHeader + self.__dataArray)
                    text_file.close()

                self.__dataArray = np.genfromtxt(io.BytesIO(self.__dataArray.encode('utf-8')),
                                             dtype = dtype,
                                             delimiter = delimiter,
                                             converters = self.str2date(columnofdate = columnofdate, dateformat = dateformat))
        return self.__dataArray

    def importTRY(self, location, year, season, quarterHour, startrow, dtype):
        self.__table =[]
        self.__location = location
        self.__year = year
        self.__season = season
        self.__columnofdate = 2
        self.__dateformat = '%m-%d-%H'
        self.__filename = self.__filepath_import + os.sep + str("TRY" + str(self.__year) + "_" +
                          TRY_Dictionary.TRYDictLocations(self, self.__location) +
                          "_" +
                          TRY_Dictionary.TRYDictLocations(self, self.__season) +
                          ".dat")
        self.__quarterHour = quarterHour
        self.__startrow = startrow
        self.__dtype = dtype

        with open(self.__filename, encoding = 'cp437') as csvfile:
            linereader = csv.reader(csvfile)
            for indexRow, row in enumerate(linereader):
                if indexRow >= self.__startrow:
#                    print(row)
                    for item in row:
#                        print(indexItem)
#                        print(item.split())
                        item = item.split()
                        if self.__quarterHour == False:
                            item[2:5] =  [datetime(int(self.__year), int(item[2]), int(item[3]), int(item[4])-1)]
                            self.__table.append(item)
                        else:
                            item[2:5] = [datetime(int(self.__year), int(item[2]), int(item[3]), int(item[4])-1, 0)]
                            self.__table.append(copy(item))
                            i = 0
                            while i < 3:
                                item[2] += timedelta(minutes = 15)
                                self.__table.append(copy(item))
                                i += 1

#
            self.__table = [tuple(i) for i in self.__table]
            print('Import ' + self.__filename + ' successfully')

            return np.asarray(self.__table, dtype = self.__dtype)

    def exportCSV(self, filename, results, delimiter = ";"):
        '''
        exports results as CSV with "," as decimal seperator
        filename = string without '.csv'
        results = []
        '''
        self.__results = results
        '''opens file and writes into it'''
        with open(self.__filepath_export + os.sep + filename + ".csv", 'w')as pyfile:
            for item0 in self.__results:
                for item1 in item0:
                    if type(item1) == float:
                        item1 = str(item1)
                        item1 = item1.replace(".", ",")
                    pyfile.write(
                                 item1 + delimiter
                                 )

                pyfile.write("\n")
            pyfile.close()


#    def importDBF(self, filename):
#        '''
#        imports a dBASE
#        #######
#        return:
#            iterable object
#        '''
#        self.__dataArraydbf = []
#        for record in DBF(self.__filepath_import + "\\" + filename, encoding = "cp437", load = True):
#             self.__dataArraydbf.append(record)
#
#        return self.__dataArraydbf



    def exportFig(self, filename, fig):
        '''
        exports matplotlib grafik as pdf and png\n
        #######\n
        return:\n
            pp.close()
        '''
        self.__seperator = "\\"
        if self.__filepath_export == "":
            self.__seperator = ""

        fig.savefig(self.__filepath_export + self.__seperator + filename + ".png", bbox_inches = 'tight', dpi = 300)
        print("Saved PNG to: " +str(self.__filepath_export + self.__seperator + filename + ".png"))
        fig.savefig(self.__filepath_export + self.__seperator + filename + ".pdf", filetype = "pdf", bbox_inches = 'tight', dpi = 300)
        print("Saved PDF to: " +str(self.__filepath_export + self.__seperator + filename + ".pdf"))


    def str2date(self, columnofdate = None, dateformat = None):
        if columnofdate == None or dateformat == None:
             print("In def str2date: self.__columnofdate == None or self.__dateformat == None")
             return None
        else:
#            print(self.__columnofdate, self.__dateformat)
             func_str2date = {columnofdate: lambda x: datetime.strptime(x.decode("utf-8"), dateformat)}
             return func_str2date

    def str2num(self,column):
        func_str2num = {column: lambda x : dates.date2num(x.decode("utf-8"), '%d.%m.%Y %H:%M')}
        return func_str2num
    def strpdate2num(self,column):
        func_strpdate2num = {column: dates.strpdate2num('%d.%m.%Y %H:%M')}
        return func_strpdate2num
#    def writeColHeader(self, filepathAndfilename, tableHeadername):
#        self.__filepathAndfilename = filepathAndfilename
#        with open(self.__filepathAndfilename, "r") as text_file:
#            text_old = text_file.read()
#            text_file.close()
#        with open(self.__filepathAndfilename, "w") as text_file:
#            text_file.write(text_old[0:0] + str(Dictionaries("").csvHeader(tableHeadername)) + text_old[:])
#            text_file.close()

