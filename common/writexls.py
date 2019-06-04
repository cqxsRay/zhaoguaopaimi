"""
将需要生成的数据写入到excel中
"""

import xlwt
import os
from common import generator as g
class wtxls:
    def __init__(self):
        global book,sheet1,path
        #创建工作簿
        book = xlwt.Workbook()
        #创建表单
        sheet1 = book.add_sheet('sheet1',cell_overwrite_ok=True)
        # 保存的文件路径
        path=os.path.join(os.path.dirname(os.getcwd()),'testfile/case','userinfo.xls')
    """
    只有一列数据的情况
    """
    def onecol(self,n):
        # n 表示行数
        # 写表头
        row0 = ['phone']
        sheet1.write(0,0, row0)
        for i in range(1,n):
            colum = g.createPhone()
            # 括号里依次是行，列，值
            sheet1.write(i, 0, colum)

        book.save(path)
    """
    有多列多行数据的情况
    """
    def manyrow(self,n):
        # 写表头
        row= ['phone','cardid','bankid','name']
        for t in range(0, len(row)):
            sheet1.write(0, t, row[t])
        # 写表数据
        for i in range(1,n):
            colum = [g.createPhone(), g.createidcard(), g.createbankid(),g.name()]
            for j in range(0, len(colum)):
                # i行j列的数据
                sheet1.write(i,j,colum[j])
        book.save(path)
if __name__=='__main__':
    s=wtxls()
    s.manyrow(7)
# s.onecol(2)