from common_script.xlsx_operator import Operator
import math

class data_order_info:
    def __init__(self,file_add):
        self.file_add = file_add
        self.data = None

    def rows(self):
        xlsx = Operator(file_address=self.file_add)
        rows = xlsx.get_rows()
        return rows

    def read_item(self,count):
        xlsx = Operator(file_address=self.file_add)
        self.data = xlsx.get_data()[count]
        return self.data

    def hotelCode(self):
        try:
             hotelcode = self.data['酒店号']
             if type(hotelcode) is str:
                return hotelcode
             else:
                hotelcode = math.trunc(self.data['酒店号'])
                return hotelcode
        except Exception as e:
             print(e)

    def batchNo(self):
        try:
            batchno = self.data['账期']
            return str(batchno)
        except Exception as e:
            print(e)

    def abId(self):
        try:
            abid = self.data['结算主体ID']
            return int(abid)
        except Exception as e:
            print(e)

    def brandCode(self):
        try:
            brand = self.data['品牌编号']
            if brand == '':
                #    print('品牌为空')
                return None
            else:
                if type(brand) == float:
                    #   print((math.trunc(brand)))
                    return str(math.trunc(brand))
                else:
                    return str(brand)
        except Exception as e:
            print(e)

    def item_code(self):
        try:
            item_code = self.data['记账科目id']
            return item_code
        except Exception as e:
            print(e)






if __name__ == '__main__':
    test = data_order_info(file_add='D:\测试\测试内容\结算\测试excel数据\结算通记账科目出账测试数据.xlsx')
    print(test.rows())
    print(test.read_item(0))
    print(test.item_code())