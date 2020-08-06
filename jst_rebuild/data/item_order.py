from common_script import  xlsx_operator
from database import mongounit
from datetime import datetime
from database.mysqlunit import MysqlUnit


class item_order:
    def __init__(self,file_add):
        self.file_add = file_add
        self.item = xlsx_operator.Operator(self.file_add).get_data()
        self.itemList = {}

    def itemInfo(self, count):

        self.itemList = self.item[count]
        return self.itemList

    def hotelCode(self):
        hotelCode = self.itemList['酒店号']
        return str(hotelCode)
    def eod(self):
        eod = self.itemList['营业日']
        return eod
    def itemCode(self):
        itemCode = self.itemList['记账科目id']
        return str(itemCode)
    def amount(self):
        amount = self.itemList['金额']
        return int(amount)*100


if __name__ == '__main__':
    t = item_order(file_add='D:\测试\测试内容\结算\测试excel数据\结算通记账科目出账测试数据.xlsx')
    print(t.itemInfo(0))
    print(t.itemCode())