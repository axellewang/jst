from common_script import xlsx_operator
from database.mysqlunit import MysqlUnit
import pymysql
import math

class fund:
    def __init__(self,file_address):

        self.xlsx_data = xlsx_operator.Operator(file_address=file_address).get_data()
        self.fund_dict = {}
#根据传入的序列获取对应dict内容
    def fund_data(self,count):
        self.fund_dict = self.xlsx_data[count]
   #     print(self.fund_dict)

        return  self.fund_dict


#以下为获取sql所需数据并返回
    def userId(self):
        userId = int(self.fund_dict['userId'])
   #     print(userId)
        return userId
    def userType(self):
        userType = self.fund_dict['用户类型']
        if userType ==  ''   :

        #    print('用户类型为空')
            return None
        else:
            return int(userType)
    def userName(self):
        userName = self.fund_dict['姓名']
        return str(userName)
    def code(self):
        code = self.fund_dict['工号']
        return code
    def job(self):
        job = self.fund_dict['岗位']
        if job == '':
            return None
        else:
            return str(job)
    def phoneNumber(self):
        phoneNumber = math.trunc(self.fund_dict['手机号'])
        return str(phoneNumber)
    def hotelCode(self):
        hotelCode = self.fund_dict['酒店号']
        if hotelCode == ''  :
        #    print('酒店号为空')
            return None
        else:
            if type(hotelCode) == float :
            #    print((math.trunc(hotelCode)))
                return str(math.trunc(hotelCode))
            else:
                return str(hotelCode)
    def hotelName(self):
        hotelName = self.fund_dict['酒店名']
        if hotelName == '':
            return None
        else:
            return str(hotelName)
    def brand(self):
        brand = self.fund_dict['品牌']
        if brand == '' :
        #    print('品牌为空')
            return None
        else:
            if type(brand) == float:
             #   print((math.trunc(brand)))
                return str(math.trunc(brand))
            else:
                return str(brand)
    def giftTypeId(self):
        giftTypeId = self.fund_dict['礼包类型id']
        if giftTypeId == '':
            return None
        else:
            return str(math.trunc(giftTypeId))
    def giftName(self):
        giftName = self.fund_dict['礼包名']
        if giftName == '':
            return None
        else:
            return giftName
    def giftId(self):
        giftId = self.fund_dict['礼包id']
        if giftId == '':
            return None
        else:
            return str(math.trunc(giftId))
    def amount(self):
        amount = self.fund_dict['金额']
      #  print(amount)
        return amount
    def we_deal_type(self):
        we_deal_type = int(self.fund_dict['we奖励类型'])
        return we_deal_type
    def status(self):
        status = self.fund_dict['是否有效']
        return status
    def update_time(self):
        update_time = self.fund_dict['时间']
    #    print(update_time)
        return update_time
    def channel(self):
        channel = self.fund_dict['售卖渠道']
        if channel == None:
            return None
        else:
            return channel








if __name__ == '__main__':
    test = fund(file_address= 'D:\测试\测试内容\结算\测试excel数据\资产测试数据-可调整数据 - 副本.xlsx')
    test.fund_data(1)
    print(test.userId())
  #  id = test.update_time()


