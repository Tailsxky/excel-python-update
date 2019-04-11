#!/usr/bin/python
# -*- coding: UTF-8 -*-

from openpyxl import Workbook
from openpyxl import load_workbook
import re
import os
import wechat as wechat

def_filename = wechat.filename('file/')[1] #"file/上下班打卡_日报_20181116-20181122.xlsx"

#print(new_def_filename)

wb = load_workbook(def_filename) #read the excel

ws1 = wb['上下班打卡_日报'] #read the specific excel sheet

ws1.delete_cols(4,2)
ws1.delete_cols(6,3)
ws1.delete_cols(8)
ws1.delete_cols(10)


wb.save(def_filename)
        

