import openpyxl

workbook = openpyxl.load_workbook("data/bmi.xlsx")
sheet=workbook["Sheet1"]

max_row = sheet.max_row # get number of rows

# add a column header for bmi
sheet.cell(row=1, column=4).value = "bmi"
 
#loop through every row
for i in range(2, max_row + 1):
    
    #read cell
    name = sheet.cell(row=i, column=1).value
    weight = sheet.cell(row=i, column=2).value
    height = sheet.cell(row=i, column=3).value
    
    bmi = weight / (height * height)
    
    sheet.cell(row=i, column=4).value = bmi

    print("name:%s \tBMI: %f" % (name, bmi))
    
#save the file
workbook.save("data/bmi_update.xlsx")

    
print("Completed")