import time

import pymysql

from common_script.time_opt import datetime_strftime, date
from database.mysqlunit import MysqlUnit


class data_maker:
    def __init__(self,dbname):
        self.db = MysqlUnit()
        self.conn = self.db.dblink(dbname)
        self.cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)


    def give_log(self,mebId,loopcount,giftId,t,giveNo):#形参定义:循环次数,用户归属品牌,礼包id,操作的日期
        i = 0
        brandcode = ['137']
        while i < loopcount:
            for brand in brandcode:
                reqGiveNo = giveNo + str(i)
                sql = "  INSERT INTO wepoint_test.t_bonus_give_log (USER_ID, USER_TYPE, CODE, MOBILE, NAME, JOB, STORE_ID, BRAND_ID, STORE_CODE, STORE_NAME, GIFT_TYPE_ID, GIFT_NAME, GIFT_ID, RIGHTS_ARRIVE, GIVE_VALUE, GIVE_NO, STATUS, REMARK, OPERATOR, UPDATE_DT, CREATE_DT, FREEZE_DT, WE_DEAL_TYPE)\
                                VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                val = (mebId, 1, '50106854610', '18964719947', '礼包测试用户', '店长', 2121, brand, None, '康铂酒店(外滩店)', '7559', '测试礼包',
                       giftId, True,  1.56, reqGiveNo, 0, '礼包id：%s'%giftId,
                       'SYS_OPERATOR', '2019-12-10 13:03:27', datetime_strftime(t), datetime_strftime(t), 4)
                try:
                    self.conn.ping(reconnect=True)#保持连接
                    req = self.cursor.execute(sql, val)  # sql提交,组合字段和数据
                    print("插入数据%s"%reqGiveNo)
                    self.conn.commit()  # 确认提交
                except Exception as e:
                    print(e)
                i += 1
        print('give_log表插入数据完成，共计%d条'%loopcount)
        self.conn.close()  # 关闭链接

    def in_out_log(self,mebId,loopcount,giftId,t,giveNo):
        i = 0
        while i < loopcount:
            reqGiveNo = giveNo + str(i)
            sql = "INSERT INTO wepoint_test.t_account_in_out_log_09 (USER_ID, NICK_NAME, TYPE, BONUS_VALUE, EXTRACT_BALANCE, GIFT_ID, EXCHANGE_NO, STATUS, REMARK, OPERATOR, UPDATE_DT, CREATE_DT, WE_DEAL_TYPE)\
                       VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            val = (mebId, 0xE59095E5AE8FE4B89A, 1, 1.56, None, giftId, reqGiveNo, 0, '新增数据', '系统提现中任务更新',datetime_strftime(t), datetime_strftime(t), 4)
            try:
                self.conn.ping(reconnect=True)#保持连接
                req = self.cursor.execute(sql,val)
                print("插入数据%s" % reqGiveNo)
                self.conn.commit()
                i+=1
            except Exception as e:
                print(e)
        print('in_out_log表插入数据完成，共计%d条' % loopcount)
        self.conn.close()

    def audit(self,loopcount):
        i = 0
        while i < loopcount:
            sql =  " INSERT INTO wepoint_test.t_bonus_give_audit (batch_no, audit_status, remark, operator_id, operator_name, total_num, total_amount, flush_flag, audit_time, create_time, source_type)\
                     VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            val = (date(i), 1, None, 32645, 'test222331', 35, 9360, 1.56, '2019-12-27 14:47:52', '2019-12-27 14:25:04', 2)
            try:
                self.conn.ping(reconnect=True)
                req = self.cursor.execute(sql,val)
                self.conn.commit()
                i+=1
            except Exception as e:
                print(e)
        print('audit表插入完成,共计%d条'%loopcount)
        self.conn.close()



    def run_method(self,method,loopcount,giftId,t,giveNo,mebId):
        if method == 'give_log':
            run = data_maker.give_log(self,loopcount=loopcount,giftId=giftId,t=t,giveNo=giveNo,mebId=mebId)
        elif method == 'in_out_log':
            run = data_maker.in_out_log(self,loopcount=loopcount,giftId=giftId,t=t,giveNo=giveNo,mebId=mebId)
        else:
            print('请求输入错误')

    def run_2method(self,loopcount,giftId,t,giveNo,mebId):
        data_maker.give_log(self,loopcount=loopcount,giftId=giftId,t=t,giveNo=giveNo,mebId=mebId)
        print('3秒后开始导入in_out_log数据')
     #   print(self.conn)
        time.sleep(3)
        data_maker.in_out_log(self,loopcount=loopcount,giftId=giftId,t=t,giveNo=giveNo,mebId=mebId)
        print("in_out_log数据导入完成")


if __name__ == '__main__':
    db = data_maker('wepoint_test')
   # db.run_method(method= 'in_out_log',loopcount=10 ,giftId= 9899849,t=-1,giveNo='WE_NO_900000000')
    db.run_2method(loopcount=5 ,giftId= 9899849,t=-1,giveNo='WE_NO_900000000',mebId=1348088755)
  #  db.audit(loopcount=300)