import openpyxl, os

workbook = openpyxl.load_workbook("example.xlsx")
type(workbook)
## <class 'openpyxl.workbook.workbook.Workbook'>

sheet = workbook.get_sheet_by_name("Sheet1")
type(sheet)
## <class 'openpyxl.worksheet.worksheet.Worksheet'>

# get sheet names
workbook.get_sheet_names()

# get sheet cell
cell = sheet["A1"]

# get cell value
print(cell.value)
print(sheet["B1"].value)
print(sheet.cell(row=1,column=2).value)

# pass cell value to str function to format it e.g. a date
print(str(cell.value))
