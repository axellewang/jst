#coding:utf-8
from database import mongounit
import pprint
import datetime

mongo = mongounit.Mongounit()
conn = mongo.conn('jst_order_service_test')
mongo.change_collection(table='micro_official_website_shop')


class Parameters():
    def __init__(self):
        self.data_list = []
    def getMicroData(self,filter_dict):
      try:
        getData =  mongo.find_one(filter_dict)

       # clone = getData.clone()
        self.data_list.append(getData)
     #   print(self.data_list)
       # pprint.pprint(self.data_list)
        return self.data_list
      except Exception as e:
          print('查询错误,失败原因: %s' % e)

    def getUid(self):
        _id = self.data_list[0]['_id']
        return _id
    def getGuid(self):
        guid = self.data_list[0]['guid']
        return guid
    def getWeHotelCode(self):
        weHotelCode = self.data_list[0]['weHotelCode']
        return weHotelCode
    def getHotelName(self):
        hotelName = self.data_list[0]['hotelName']
        return hotelName
    def getOrderCode(self):
        orderCode = self.data_list[0]['orderCode']
        return orderCode
    def getAmount(self):
        self.amount = self.data_list[0]['amount']
        return self.amount
    def getPayType(self):
        self.payType = self.data_list[0]['payType']
        return self.payType
    def getPayTime(self):
        self.payTime = self.data_list[0]['payTime']
        payTime = createTime = datetime.datetime.strftime(self.payTime, '%Y-%m-%d %H:%M:%S')
        return payTime
    def getPayStatus(self):
        self.payStatus = self.data_list[0]['payStatus']
        return self.payStatus
    def getMemberId(self):
        self.memberId = self.data_list[0]['memberId']
        return self.memberId
    def getCreateTime(self):
        self.createTime = self.data_list[0]['createTime']
        createTime = datetime.datetime.strftime(self.createTime, '%Y-%m-%d %H:%M:%S')
        return createTime
    def getTerminateState(self):
        self.terminateState = self.data_list[0]['terminateState']
        return self.terminateState
    def getReward(self):
        self.reward = self.data_list[0]['reward']
        if self.reward == None:
            self.reward = 0
            return self.reward
        else:
            return self.reward

if __name__ == '__main__':
    test = Parameters()
    test.getMicroData(filter_dict={'orderCode':'O1589351001750442021'})
    print(test.getUid())

