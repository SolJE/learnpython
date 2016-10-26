import os
import sys
import glob
import xlrd
import re

this_path=os.getcwd()
#listfile = os.listdir(this_path)
listfile = glob.glob("*.xls*")
print(listfile)

the_excel = listfile[0]
wb = xlrd.open_workbook(the_excel)
wst1 = wb.sheet_by_index(0)
print(wb.sheets)
cellsA1 = wst1.cell(1,4)
print(cellsA1)
#showexcel(self)

#def showexcel(self):
    #workbook=xlrd.open_workbook(self)
sheets=wb.sheet_names();
    #多个sheet时，采用下面的写法打印
    #for sname in sheets:
        #print(sname)
worksheet=wb.sheet_by_name(sheets[0])
    #nrows=worksheet.nrows
    #nclows=worksheet.ncols
for i in range(0,worksheet.nrows):
    row=worksheet.row(i)

    for j in range(0,worksheet.ncols):
        print(worksheet.cell_value(i,j),"\t",end="")

    print()