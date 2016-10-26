# -*- coding:utf-8 -*-

import os
import sys
import glob
import xlrd
#import pdb
import time

start = time.time()

this_path = os.getcwd()
excel_list = glob.glob("*.xls*")
mac_list = set([])


for excel in excel_list:
    print(excel)
    wb = xlrd.open_workbook(excel)
    sheets = wb.sheet_names();
    for sheet in sheets:
        #pdb.set_trace()
        for h in range(0,wb.sheet_by_name(sheet).nrows):
            row = wb.sheet_by_name(sheet).row(h)
            for l in range(0,wb.sheet_by_name(sheet).ncols):
                #pdb.set_trace()
                mac_list.add(wb.sheet_by_name(sheet).cell_value(h,l))
                #print(wb.sheet_by_name(sheet).cell_value(h,l))
end= time.time()
print(end - start)
input("检索完成显示结果吗？")
total_txt_re = open('total.txt','a')
for every in mac_list:
    every = str(every)
    if every.startswith("849681") == True and len(every) == 12:
        total_txt_re.write("%s\n" % every)
        print(every)
total_txt_re.close
