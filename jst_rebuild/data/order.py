from common_script import  xlsx_operator
from database import mongounit
from datetime import datetime
from database.mysqlunit import MysqlUnit
from dateutil import parser
import math

class order:
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

    def sourceType(self):
        sourceType = self.orderList['来源渠道']
        return str(sourceType)
    def orderStatus(self):
        orderStatus = self.orderList['订单状态']
        return  int(orderStatus)
    def bookDate(self):
        bookDate ='%s 00:00:00'% self.orderList['预订时间']
        bookDate = datetime.strptime(bookDate,'%Y-%m-%d 00:00:00')
        return bookDate
    def arrDate(self):
        arr ='%s 00:00:00' %self.orderList['预订入住']
        arrDate = datetime.strptime(arr, '%Y-%m-%d 00:00:00')
        return arrDate
    def depDate(self):
        dep = '%s 00:00:00' %self.orderList['预订离店']
        depDate = datetime.strptime(dep,'%Y-%m-%d 00:00:00')
        return depDate
    def bkrn(self):
        arrdate = self.arrDate()
        depdate = self.depDate()
        bkrn = depdate-arrdate
        return bkrn.days
    def actualArrDate(self):
        actualArrDate = self.orderList['实际入住时间']
        if actualArrDate == '':
            return None
        else:
            actualArrDate = datetime.strptime('%s 00:00:00' % self.orderList['实际入住时间'], '%Y-%m-%d 00:00:00')
            return actualArrDate
    def actualDepDate(self):
        actualDepdate = self.orderList['实际离店时间']
        if actualDepdate == '':
            return  None
        else:
            actualDepdate = datetime.strptime('%s 00:00:00' % self.orderList['实际离店时间'], '%Y-%m-%d 00:00:00')
            return actualDepdate
    def actualRn(self):
        try:
            if self.actualDepDate()   is  None:
                print('房单未离店')
                return None
            else:
                actualRn = self.actualDepDate() - self.actualArrDate()
                return actualRn.days

        except Exception as e:
            print(e)
    def rateCode(self):
        rateCode = self.orderList['价格码']
        return rateCode
    def amount(self):
        amount = self.orderList['金额']
        return int(amount)*100
    def paySource(self):
        paySource = self.orderList['支付来源']
        if paySource == '':
            return None
        else:
            return str(paySource)
    def payments(self):
        payments = self.orderList['支付金额']
        if payments == '':
            return None
        else:
            return int(payments)*100
    def payType(self):
        payments = self.payments()
    #    print(payments)
        if payments is not None and payments > 0:
            payType = 1
            return payType
        elif self.refundAmount() is not None and self.refundAmount() >0:
            payType = 2
            return payType
        else:
            payType = 0
            return payType
    def refundSource(self):
        refundSource = self.orderList['退款来源']
        if refundSource == '':
            return None
        else:
            return str(refundSource)
    def refundAmount(self):
        refundAmount = (self.orderList['退款金额'])
        if  refundAmount ==  '' :
            return None
        else:
            return int(refundAmount)*100
    def couponAmount(self):
        coupongAmount = self.orderList['优惠券金额']
        if coupongAmount == '':
            return None
        else:
            return int(coupongAmount)*100
    def couponType(self):
        couponType = self.orderList['优惠券类型']
        if couponType == '':
            return None
        else:
            return couponType
    def barer(self):
        barer = self.orderList['承担方']
        if barer == '':
            return None
        else:
            return barer
    def barerAmount(self):
        barerAmount = self.orderList['承担金额']
        if barerAmount == '':
            return None
        else:
            return int(barerAmount)*100
    def barerType(self):
        coupon = self.barer()
        if coupon == "1":
            barerType = "WeHotel"
            return barerType
        elif coupon == "2":
            barerType = "平台"
            return barerType
        else:
            return None
    def saleType(self):
        saleType = self.orderList['saleType']
        if saleType == '':
            return None
        else:
            return int(saleType)
    def batchNo(self):
        batchNo = self.orderList['账期']
        return str(batchNo)
    def reward(self):
        reward = self.orderList['酬金']
        if reward == '':
            return None
        else:
            return int(reward)*100
    def is_micro_room(self):
        micro_room = self.orderList['是否微官网客房单']
        if micro_room == '是':
            return True
        else:
            return False
    def micro_amount(self):
        micro_amount = self.orderList['微官网商品金额']
        if micro_amount == '':
            return 0
        else:
            return int(micro_amount)*100



if __name__ == '__main__':
    t = order('../file/订单数据.xlsx',db='breeze_rules_db')
    print(t.orderinfo(2))
  #  print(type(t.payments()))
    print(t.payType())
 #   t.hotelCode()




