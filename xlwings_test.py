import xlwings as xs
import time


def get_char(number):
	factor,remainder = divmod(number,26)
	modchar = chr(remainder + 65)
	if factor != 0:
		modchar = get_char(factor-1) + modchar
	return modchar


def xlwingsTest(filePath):
	# 指定不显示地打开excel
	app = xs.App(visible=False,add_book=False)

	wb = app.books.open(filePath) # 打开excel文件

	sheet = wb.sheets[0]
	row_data = sheet.range('A1').expand('right').value # 第一行的所有数据
	column_data = sheet.range('A1').expand('down').value # 第一列的所有数据
	print(row_data)
	print(column_data)
	print(sheet.range('A2').value)


	wb.close()
	app.quit()

xlwingsTest('F:\\DeskTop\\test.xlsx')
# print(get_char(26))