from common_script import  xlsx_operator
from database import mongounit
from datetime import datetime
from database.mysqlunit import MysqlUnit
from dateutil import parser
import math

class gift:
    def __init__(self,file_add,db):
        self.file_add = file_add
        self.dbname = db
        self.order = xlsx_operator.Operator(self.file_add).get_data()
        self.orderList = {}
        self.mysql = MysqlUnit()
    def orderinfo(self,count):
        self.orderList = self.order[count]
     #   print(self.orderList)
        return self.orderList

    def hotelCode(self):
        hotelCode = self.orderList['酒店号']
        if type(hotelCode) is str:
            return str(hotelCode)
        else:
            return str(math.trunc(hotelCode))
    def hotelName(self):
        hotel = self.hotelCode()
        db = self.mysql
        db_link = db.dblink(self.dbname)
        cursor = db_link.cursor()
        try:
            sql = "select wehotel_name from breeze_rules_db.t_hotel_config where wehotel_code = '{hotelcode}'".format(
                hotelcode=hotel)
            cursor.execute(sql)
            result = cursor.fetchone()
            db_link.close()
            # 将tuple转成str
            hotelName = "".join(tuple(result))
            return hotelName
        except Exception as e:
            print('未查询到酒店名！')
            return None
    def brandCode(self):
        hotel = self.hotelCode()
        db = self.mysql
        db_link = db.dblink(self.dbname)
        cursor = db_link.cursor()
        try :
            sql = "select brand_code from breeze_rules_db.t_hotel_config where wehotel_code = '{hotelcode}'".format(hotelcode=hotel)
            cursor.execute(sql)
            result = cursor.fetchone()
            db_link.close()
            #将tuple转成str
            brandCode = "".join(tuple(result))
            return brandCode
        except Exception as e:
            print('未查询到酒店的品牌！\n %s' %e)
            return None
    def enjoytime(self):
        enjoytime ='%s 00:00:00'% self.orderList['售卖时间']
        enjoytime = datetime.strptime(enjoytime,'%Y-%m-%d 00:00:00')
        return enjoytime
    def amount(self):
        amount = self.orderList['礼包金额']
        return int(amount)
    def giftType(self):
        giftType = self.orderList['礼包类型']
        return int(giftType)


if __name__ == '__main__':
    t = gift('../file/订单数据.xlsx',db='breeze_rules_db')
    print(t.orderinfo(5))
  #  print(type(t.payments()))
 #   print(t.enjoytime())
 #   t.hotelCode()




