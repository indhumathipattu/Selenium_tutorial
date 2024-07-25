import openpyxl


wb = openpyxl.load_workbook("C:\\Users\\mathi\\Desktop\\Book1.xlsx")
sh=wb["Sheet3"]


for i in range(1,6):
    for j in range(1,4):
        sh.cell(row=i,column=j).value="python"
        
wb.save("C:\\Users\\mathi\\Desktop\\Book1.xlsx")





