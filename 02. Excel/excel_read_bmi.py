import openpyxl

workbook = openpyxl.load_workbook("data/bmi.xlsx")
sheet=workbook["Sheet1"]


max_row = sheet.max_row # get number of rows

#loop through every row
for i in range(2, max_row + 1):
    
    #read cell
    name = sheet.cell(row=i, column=1).value
    weight = sheet.cell(row=i, column=2).value
    height = sheet.cell(row=i, column=3).value
    
    print("name:%s \tweight: %d \theight: %f " % (name, weight, height))
    print("name", name, "weight", weight, "height", height)


'''
# hardcoded data for illustration
name = sheet.cell(row=2, column=1).value
weight = sheet.cell(row=2, column=2).value
height = sheet.cell(row=2, column=3).value

print("name:%s \tweight: %d \theight: %f " % (name, weight, height))

'''

