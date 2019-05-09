import readConfig
import os
import xlrd
from datetime import datetime
from xlrd import xldate_as_tuple
from common.Log import Log
proDir = readConfig.proDir
log = Log
class read_xls:
    def __init__(self,xls_name, sheet_name):
        """

        :param xls_name: 文件名
        :param sheet_name: sheet 名字
        """
        self.xls_name=xls_name
        self.sheet_name=sheet_name
        # 获取excel文件路径
        xlsPath = os.path.join(proDir, "testdata", self.xls_name)
        # open xls file
        file = xlrd.open_workbook(xlsPath)
        # get sheet by name
        self.sheet = file.sheet_by_name(self.sheet_name)
        # 获取行数
        self.rows = self.sheet.nrows
        # 获取列数
        self.cols = self.sheet.ncols
        # 获取第一行作为Key
        self.keys = self.sheet.row_values(0)

    """
    按情况处理数据
    返回类型是列表中字典
    """
    def dict_xls(self):
        if self.rows<=0:
            print("总行数小于1")
        else:
            cls = []
            for i in range(1, self.rows):
                s = {}
                for j in range(self.cols):
                    ctype = self.sheet.cell(i, j).ctype
                    cell= self.sheet.cell(i, j).value
                    # 如果是整型
                    if ctype == 2 and cell % 1 == 0:
                        cell = int(cell)
                    # 如果是日期的类型
                    elif ctype == 3:
                        # 转成datetime对象
                        date = datetime(*xldate_as_tuple(cell, 0))
                        cell = date.strftime('%Y/%d/%m %H:%M:%S')
                    # 处理布尔类型的值
                    elif ctype == 4:
                        cell = True if cell == 1 else False
                    s[self.keys[j]]=cell
                cls.append(s)
            return cls
    """
    按情况处理数据
    如果是整数就是整数
    如果是浮点数就是浮点数
    返回列表中的列表
    """
    def list_xls(self):
        cls=[]
        # 去掉头部
        for i in range(1,self.rows):
            row_content = []
            for j in range(self.cols):
                ctype = self.sheet.cell(i, j).ctype
                cell = self.sheet.cell_value(i, j)
                # 如果是整型
                if ctype == 2 and cell % 1 == 0:
                    cell = int(cell)
                # 如果是日期的类型
                elif ctype == 3:
                    # 转成datetime对象
                    date = datetime(*xldate_as_tuple(cell, 0))
                    cell = date.strftime('%Y/%d/%m %H:%M:%S')
                # 处理布尔类型的值
                elif ctype == 4:
                    cell = True if cell == 1 else False
                row_content.append(cell)
            cls.append(row_content)
        return cls