from common_script import  xlsx_operator
from database import mongounit
from datetime import datetime
from database.mysqlunit import MysqlUnit
import math

class folio_order:
    def __init__(self,file_add):
        self.file_add = file_add
        self.folio = xlsx_operator.Operator(self.file_add).get_data()
        self.folioList = {}
    def folioInfo(self,count):
        self.folioList = self.folio[count]
        return self.folioList

    def hotelCode(self):
        hotelCode = self.folioList['酒店号']
        if type(hotelCode) is float:
            return math.trunc(hotelCode)
        else:
            return str(hotelCode)
    def end_of_day(self):
        eod = self.folioList['营业日']
        return   eod
    def roomRate(self):
        roomRate = self.folioList['roomRate']
        if roomRate == '':
            return None
        else:
            return int(roomRate)
    def actualRate(self):
        actualRate = self.folioList['actualRoomRate']
        if actualRate == '':
            return None
        else:
            return int(actualRate)*100
    def actualDayRate(self):
        actualDayRate = self.folioList['actualDayRoomRate']
        if actualDayRate == '':
            return None
        else:
            return int(actualDayRate)*100
    def folioState(self):
        folioState = self.folioList['房单状态']
        return folioState
    def arrDate(self):
        arrDate = self.folioList['到店日']
        if arrDate == '':
            return None
        else:
            return arrDate
    def depDate(self):
        depDate = self.folioList['离店日']
        if depDate == '':
            return  None
        else:
            return depDate
    def realRn(self):
        if self.arrDate() == '':
            return  None
        else:
            arrDate = datetime.strptime(self.arrDate(), '%Y-%m-%d 00:00:00')
            depDate = datetime.strptime(self.depDate(), '%Y-%m-%d 00:00:00')
            realRn = depDate-arrDate
            return realRn.days
    def sourceType(self):
        sourceType = self.folioList['渠道来源']
        return int(sourceType)
    def isoffline(self):
        isoffline = self.folioList['是否线下单']
        if isoffline == '是':
            return  True
        else:
            return False




if __name__ == '__main__':
    t = folio_order(file_add='D:\测试\测试内容\结算\测试excel数据\房单数据.xlsx')
    t.folioInfo(0)
    print(t.hotelCode())
