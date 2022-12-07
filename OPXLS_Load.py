from openpyxl import load_workbook

wb = load_workbook(filename='format.xlsx')
print(type(wb))
print(dir(wb))
print(id(wb))
print(wb.worksheets)  # premenna objektu wb
# print(wb.views)

ws2 =wb['PANDAS']
print(ws2['A4'])  # cell object
print(ws2['A4'].value)  # obsah bunky  London
ws2['A4'] = 'Dudince'
print(ws2['A4'].value)  # obsah bunky sa zmenil na Dudince

wb.save('format.xlsx')
print('DONE')
