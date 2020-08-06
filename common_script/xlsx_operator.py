import xlrd,openpyxl

class Operator:
    def __init__(self,file_address):
        self.file_add = file_address
#获取文件表
    def getSheet(self):
        work_sheet = xlrd.open_workbook(self.file_add)
        sheet_names = work_sheet.sheet_names()
        sheet = None
        try:
            for sheet_name in sheet_names:
                sheet = work_sheet.sheet_by_name(sheet_name)
            return sheet
        except Exception as e:
            print(e)

#获取文件行数
    def get_rows(self):
            sheet = Operator(self.file_add).getSheet()
            rows = sheet.nrows-1
         #   print(rows)

            return rows


#获取文件内所有数据，储存为list
    def get_data(self):
            sheet = Operator(self.file_add).getSheet()
            rows = sheet.nrows
            cols = sheet.ncols
            col_names = sheet.row_values(0)
            list_data = []
            j =1
            for i in list(range(rows-1)):
              try:
                dict_data = {}
                col_value = sheet.row_values(j)
                for x in list(range(cols)):
                    dict_data[col_names[x]] = col_value[x]

                  #  print(col_value)
                list_data.append(dict_data)
                j+=1
            #        all_value.append(int(cell))
              except ValueError as e:
                    print('数值错误:%s' % e)

         #   print(list_data)
            return list_data

#写入数据
    def write_data(self,sheet_name,value,col_name):
        if type(value) is list:  # 获取类型为list的数据长度
            i = len(value)
        else:
            i = 1 #其余类型数据长度默认为1
      #  print(i)
        work_sheet = openpyxl.load_workbook(self.file_add)
        sheet = work_sheet[sheet_name]
        colname_is_exist = Operator(self.file_add).getColumnIndex(columnName=col_name)
        rows = Operator(self.file_add).get_rows()
        cols = sheet.max_column
        try:
            #这里是校验列名是否存在,若不存在则写入
            if colname_is_exist  is not None :
                pass
            else:
                sheet.cell(1,cols+1,value=col_name)#写入列名
            work_sheet.save(self.file_add)
            colnamePostion = Operator(self.file_add).getColumnIndex(columnName=col_name)#获取列位置,下面写入时需要根据该结果获取列位置
            nlist = len(Operator(self.file_add).read_by_indexName(columnName=col_name))#根据列名获取行数长度,下面写入行位置时根据行数长度+2
            if type(value) is list:#类型为list的数据写入方式
                for j in range(0, i):
                    sheet.cell(row=nlist+2+j, column=colnamePostion+1, value=str(value[j]))#根据获取到的数据位置写入excel指定单元格
             #   print('数据%s写入成功' % value[j])
            else:
                sheet.cell(row=nlist+2, column=colnamePostion+1, value=str(value))  # 根据获取到的数据位置写入excel指定单元格
           #     print('数据%s写入成功' % value)
            work_sheet.save(self.file_add)
        except Exception as e:
            print(e)
        finally:
            work_sheet.save(self.file_add)

# 根据列名获取指定列的数据
    def read_by_indexName(self,columnName):
        try:
            columnIndex = None
            sheet = Operator(self.file_add).getSheet()
            list_data = []
            dict_data = {}
            cols = sheet.ncols
       #     print(cols)
            nrows = sheet.nrows
         #   print(nrows)
            #获取列名所在列位置
            for i in range (0,sheet.ncols):
                if (sheet.cell_value(0,i) == columnName):
                    columnIndex = i
             #       print(columnIndex)
                    break
                #    return None
            #获取该列所有数据，返回在list中
            for i in range(1,nrows):
                data = sheet.cell_value(i,columnIndex)
                if data == '':
                    pass
                else:
                    list_data.append(data)
         #   print((len(list_data)))
            return list_data

        except Exception as e:
            print(e)

    def getColumnIndex(self, columnName):
        sheet = Operator(self.file_add).getSheet()
        cols = sheet.ncols
        columnIndex = None
        for i in range(cols):
            if (sheet.cell_value(0, i) == columnName):
                columnIndex = i
         #       print(i)
                break
        return columnIndex

#删除表格内容
    def delete_table(self):
        xls = openpyxl.load_workbook(self.file_add)
        sheet = xls['Sheet1']
        rows =sheet.max_row
        print(rows)
        i = 0
        while i < rows:
            sheet.delete_rows(1)
            i+=1
        xls.save(self.file_add)


if __name__ == '__main__':
    opt = Operator(file_address='D:\测试\测试内容\结算\测试excel数据\出账订单&房单号.xlsx')
 #   testsheet = opt.getSheet()
 #   t= testsheet.cell_value(1,opt.read_by_indexName(columnName='第二列'))
 #   print(opt.get_rows())
 #   opt.write_data('Sheet1',value=['123','213213'],col_name='出账结果2533')
 #   opt.read_by_indexName(columnName='出账结果25')
  #  opt.getColumnIndex('结果')
    opt.delete_table()
