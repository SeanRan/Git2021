#将数据写入excel文件内，需要用到xlwt库
# pip install xlwt
import xlwt

workbook = xlwt.Workbook(encoding = "utf-8")    #创建workbook对象
worksheet = workbook.add_sheet('sheet1')        #创建工作表
worksheet.write(0,0,'helloxlwt')               #写入数据，三个参数分别为行，列，内容
workbook.save('test.xls')                      #保存数据表
# 我新加了这一行注释以供测试git
# 第二次对git的测试