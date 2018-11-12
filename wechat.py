#!/usr/bin/python
# -*- coding: UTF-8 -*-

from openpyxl import Workbook
from openpyxl import load_workbook
import re

def replace_rule(text):
    
    text = re.sub(r"上下班打卡_日报","Punch in/out report ",text)
    text = re.sub(r"明细"," details",text)
    text = re.sub(r"时间异常","Abnormal time ",text)
    text = re.sub(r"校准状态","Status details ",text)
    text = re.sub(r"打卡类型","Punch in/out ",text)
    text = re.sub(r"打卡时间","Punch time ",text)
    text = re.sub(r"统计时间","Punch time ",text)
    text = re.sub(r"制表时间","Table generate time ",text)
    text = re.sub(r"时间","Time ",text)
    text = re.sub(r"姓名","Name ",text)
    text = re.sub(r"帐号","Account ",text)
    text = re.sub(r"部门","Department ",text)
    text = re.sub(r"所属规则","Punch rule ",text)
    text = re.sub(r"打卡次数","Punch times ",text)
    text = re.sub(r"工作时长","Working hours ",text)
    text = re.sub(r"审批单","Approval form ",text)
    text = re.sub(r"原始状态","Status ",text)
    text = re.sub(r"打卡状态","Punch status ",text)
    text = re.sub(r"状态","Status ",text)
    text = re.sub(r"小时"," hour(s) ",text)
    text = re.sub(r"缺卡","Not punch ",text)
    text = re.sub(r"正常","Normal ",text)
    text = re.sub(r"wifi打卡异常","wifi location error",text)
    text = re.sub(r"分钟"," minute(s) ",text)
    text = re.sub(r"旷工","Absent for ",text)
    text = re.sub(r"迟到","Late for ",text)
    text = re.sub(r"上班打卡","Punch in ",text)
    text = re.sub(r"未打卡","Not punch ",text)
    text = re.sub(r"地点异常","Location error ",text)
    text = re.sub(r"下班打卡","Punch out ",text)
    text = re.sub(r"日期","Date ",text)
    text = re.sub(r"打卡地点","Punch wifi ",text)
    text = re.sub(r"备注","Remarks ",text)
    
    return text
    

def_filename = "file/punch_report_20181105-20181110.xlsx"

wb = load_workbook(def_filename) #read the excel

ws1 = wb['上下班打卡_日报'] #read the specific excel sheet

for row in ws1.rows:
    for cell in row:
        #print(type(str(cell.value)))
        cell.value = replace_rule(str(cell.value))
        #print(cell.value)

ws2 = wb['上下班打卡_日报明细']

for row in ws2.rows:
    for cell in row:
        #print(type(str(cell.value)))
        cell.value = replace_rule(str(cell.value))
        #print(cell.value)



wb.save("file/translated_punch_report_20181105-20181110.xlsx")
        

