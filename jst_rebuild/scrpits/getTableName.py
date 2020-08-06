import requests

from common_script.xlsx_operator import Operator
from jst_rebuild.getHash import getHash
import math
import hashlib


class getTableName():
    def getItemTable(self,wehotelCode):


        url = 'http://172.25.33.1:30547/getBillItemDetailTableName/'+str(wehotelCode)
        req = requests.get(url=url)
    #    print(req.text)
        return req.text

#查询直销服务费账单酒店归属表
    def getDsl_Resv_Table(self,hotelCode):

       url = 'http://172.25.33.1:30547/getBillDslReservationDetailTableName/'+str(hotelCode)
       req = requests.get(url=url)
      # print(req.text)
       return req

    def getGiftTable(self,hotelCode):
        hashcode = abs(getHash.getHashCode(hotelCode))
        #print(hashcode)
        a = hashcode % 3
     #   print(a)
        tableName = 'T_BILL_GP_RESERVATION_'+str(a)
     #   print(tableName)
        return  tableName

    def getDisTable(self,hotelCode):
        hashcode = abs(getHash.getHashCode(hotelCode))

      #  print(hashcode)
        a = hashcode % 3
        tableName = 'T_BILL_DIS_DETAIL_' + str(a)
      #  print(tableName)
     #   print('酒店%s的分表为：' % hotelCode + tableName)
        return tableName

    def module(self,weHotelCode,dividedNum,file=None):
        xls = Operator(file_address=file)
        if file is not None:
            hotelCode = xls.get_data()
            for hotel in hotelCode:
                hashcode = hash(hotel)
                a = hashcode % dividedNum
                tableName = 'TEST' + '_' + str(a)
                print('酒店%s的分表为：'%hotel+tableName)
        else:
                hashcode = getHash().getHashCode(value=str(weHotelCode))
                a = hashcode % dividedNum
                print(a)
                tableName = 'TEST' + '_' + str(a)
                print('酒店%s的分表为：'%weHotelCode+tableName)


if __name__ == '__main__':
    testmoudle = getTableName()
 #   testmoudle.getTable(file_add='D:\hotelcode.xlsx')
    testmoudle.getGiftTable(hotelCode='5353')
   # testmoudle.getDslTable(hotelCode='5353')
  #  testmoudle.test_module(weHotelCode='3564',dividedNum=121)