import time

import pymysql

from common_script.xlsx_operator import Operator
from database.mysqlunit import MysqlUnit
from wepoint_rebuild.scrpits.fund import fund
from wepoint_rebuild.scrpits.gift_sell_record import gift_sell_record
from wepoint_rebuild.scrpits.getInOutTable import getInOurTable
import math


class data_scrpit:
    def __init__(self,dbname,file_add):
        self.db = MysqlUnit()
        self.conn = self.db.dblink(dbname)
        self.cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)
        self.row_numbers =  Operator(file_address=file_add).get_rows()
        self.read_data = fund(file_address=file_add)
        self.sell_record = gift_sell_record(file_address=file_add)
        self.reqNo = 'WE_NO_' + str(int(time.time()*1000))

    def give_log(self,t=-1):
        i = 0
        rows = self.row_numbers
        while i < rows:
             try:
                Fund = self.read_data.fund_data(i)#先获取本次循环的dict数据源
                reqGiveNo = self.reqNo + str(i)
            #    print('give_log%s'%reqGiveNo)

                sql = "  INSERT INTO wepoint_test.t_bonus_give_log (USER_ID, USER_TYPE, CODE, MOBILE, NAME, JOB, STORE_ID, BRAND_ID, STORE_CODE, STORE_NAME, GIFT_TYPE_ID, GIFT_NAME, GIFT_ID, RIGHTS_ARRIVE, GIVE_VALUE, GIVE_NO, STATUS, REMARK, OPERATOR, UPDATE_DT, CREATE_DT, FREEZE_DT, WE_DEAL_TYPE,CHANNEL)\
                                         VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                if self.read_data.we_deal_type() not in (6,7):
                    val = (
                    self.read_data.userId(), self.read_data.userType(), self.read_data.code(), self.read_data.phoneNumber(), self.read_data.userName(), self.read_data.job(), self.read_data.hotelCode(), self.read_data.brand(), None, self.read_data.hotelName(), self.read_data.giftTypeId(), self.read_data.giftName(),
                    self.read_data.giftId(), True, self.read_data.amount(), reqGiveNo, self.read_data.status(), '资产测试数据',
                    'SYS_OPERATOR',self.read_data.update_time(), self.read_data.update_time(), self.read_data.update_time(), self.read_data.we_deal_type(),self.read_data.channel())
           #         print(val)
                    self.conn.ping(reconnect=True)  # 保持连接
                    req = self.cursor.execute(sql, val)  # sql提交,组合字段和数据
                    print("插入数据%s" % reqGiveNo)
                    self.conn.commit()  # 确认提交
                else:
                    pass
             except Exception as e:
                         print(e)
             i += 1

    def in_out_log(self):
        i = 0
        rows = self.row_numbers
        while i < rows:
             try:
                Fund = self.read_data.fund_data(i)#先获取本次循环的dict数据源
                reqGiveNo  = self.reqNo + str(i)
            #    print('in_out_log%s'%reqGiveNo)
                if self.read_data.we_deal_type() in (2,3,4,5):
                    type = 1
                    bonus_amout = self.read_data.amount()
                    extract_amout = None
                else:
                    type = 2
                    bonus_amout = None
                    extract_amout = self.read_data.amount()
                accounttable = getInOurTable().getInOurTable(self.read_data.userId())
                sql = "  INSERT INTO {table} (USER_ID, NICK_NAME, TYPE, BONUS_VALUE, EXTRACT_BALANCE, GIFT_ID, EXCHANGE_NO, STATUS, REMARK, OPERATOR, UPDATE_DT, CREATE_DT, WE_DEAL_TYPE)\
                                         VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)".format(table = accounttable)
                val = (
                self.read_data.userId(),None,type,bonus_amout,extract_amout,self.read_data.giftId(),reqGiveNo,self.read_data.status(),'测试数据','SYS_OPERATOR',
                self.read_data.update_time(),self.read_data.update_time(),self.read_data.we_deal_type())
       #         print(val)
                self.conn.ping(reconnect=True)  # 保持连接
                req = self.cursor.execute(sql, val)  # sql提交,组合字段和数据
                print("插入in_out表数据%s" % reqGiveNo)
                self.conn.commit()  # 确认提交

             except Exception as e:
                         print(e)
             i += 1

    def extract_log(self,t=-1):
        i = 0
        rows = self.row_numbers
        while i < rows:
            try:
                Fund = self.read_data.fund_data(i)#先获取本次循环的dict数据源
                reqGiveNo = self.reqNo + str(i)
           #     print('extract %s'%reqGiveNo)
                sql = "  INSERT INTO wepoint_test.t_bonus_extract_log (USER_ID, USER_TYPE, CODE, MOBILE, NAME, JOB, STORE_ID, BRAND_ID, STORE_CODE, STORE_NAME, EXTRACT_VALUE, EXCHANGE_NO, COMMERCIAL_NO, PUBLIC_CODE_SOURCE, STATUS, REMARK, OPERATOR, UPDATE_DT, CREATE_DT,  WE_DEAL_TYPE)\
                                                    VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                if self.read_data.we_deal_type()  in (6, 7):
                    val = (
                        self.read_data.userId(), self.read_data.userType(), self.read_data.code(), self.read_data.phoneNumber(), self.read_data.userName(), self.read_data.job(), self.read_data.hotelCode(), self.read_data.brand(), None, self.read_data.hotelName(), self.read_data.amount(),reqGiveNo,
                        '0000000000000000000000000000',5, self.read_data.status(), '资产测试数据',
                        '系统提现中任务更新' , self.read_data.update_time(), self.read_data.update_time(), self.read_data.we_deal_type())
          #          print(val)
                    self.conn.ping(reconnect=True)
                    req = self.cursor.execute(sql,val)
                    self.conn.commit()
                    print('插入数据%s' % reqGiveNo)
                else:
                    pass
            except Exception as e:
                print(e)
            i +=1

    def gift_sell_record(self):
        i = 0
        rows = self.row_numbers
        while i <rows:
            try:
                sql1 = "select max(gift_id) from wehotel_member_gift.t_gift_sell_record "
                req1 = self.cursor.execute(sql1)
                fetchone = self.cursor.fetchone()
                maxid = int(fetchone['max(gift_id)'])+1
          #      print(type(maxid))
                Sell_record = self.sell_record.gift_sell_data(i)#先获取本次循环的dict数据源
                sql = "INSERT INTO wehotel_member_gift.t_gift_sell_record (member_id, member_card_no, member_name, gift_name, gift_price, gift_type_id, gift_id, user_id, store_id, brand_id, store_code, store_name, bill_no, order_id, pay_way, source, shift, remark, status, operator, update_dt, create_dt, channel)\
                      VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                val =  ( self.sell_record.meb_id(), '', self.sell_record.meb_name(), self.sell_record.gift_name(), self.sell_record.gift_price(), self.sell_record.gift_type(),maxid,
                         self.sell_record.user_id(), self.sell_record.store_id(), self.sell_record.brand_code(),self.sell_record.store_id(),self.sell_record.store_name() ,
                         '1542156', str(math.ceil(time.time())), '1', 1, 'B', '会员通PC购买礼包', 1, '测试zzy', self.sell_record.crate_dt(), self.sell_record.crate_dt(), self.sell_record.channel())
           #     print(val)
                req = self.cursor.execute(sql,val)
                self.conn.commit()
                print('插入数据成功,礼包id:%s'%maxid)
                i +=1
            except Exception as e:
                print(e)






if __name__ == '__main__':
    test = data_scrpit(dbname= 'wepoint_test',file_add= 'D:\测试\测试内容\结算\测试excel数据\资产测试数据-可调整数据 - 副本.xlsx')
    test.give_log(t=0)
    test.in_out_log()
    #test.extract_log(t=0)
  #  test.gift_sell_record()

