# 版权归邓生凤所有
import xlrd
import xlwt
bookA = xlrd.open_workbook("X:\\0931Xu\\Study\\STLT\\Python\\A.xlsx")
sheetA1 = bookA.sheets()[0]
bookB = xlwt.Workbook()
sheetB1 = bookB.add_sheet("Sheet1")
print('54mI5p2D5b2S6YKT55Sf5Yek5omA5pyJ')
print('A中表格内容如下：')
for i in range(0,sheetA1.nrows):
    rate = sheetA1.cell(i,1).value / sheetA1.cell(i,0).value
#    rate = round(rate,2)
    print(sheetA1.row_values(i),"\t纺织率为 ",rate)
    sheetB1.write(i,0,str(sheetA1.cell(i,0)).strip("number:"))
    sheetB1.write(i,1,str(sheetA1.cell(i,1)).strip("number:"))
    sheetB1.write(i,2,rate)
bookB.save("X:\\0931Xu\\Study\\STLT\\Python\\B.xls")