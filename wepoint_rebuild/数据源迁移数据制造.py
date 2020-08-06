import time
from datetime import time

import pymysql

from common_script.time_opt import datetime_strftime
from database.mysqlunit import MysqlUnit


class sell_data_maker:
    def __init__(self, dbname):
        db = MysqlUnit()
        self.conn = db.dblink(dbname)
        self.cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)

    def sell_record (self, loopcount,userId,giftTypeId,giftId, storeId,t,):  # 形参定义:循环次数,用户id
        i = 0
        now = time.time()
        str_now = str(now*1000)
        while i < loopcount:
                sql = "  INSERT INTO wehotel_member_gift.t_gift_sell_record (member_id, member_card_no, member_name, gift_name, gift_price, gift_type_id, gift_id, user_id, store_id, brand_id, store_code, store_name, bill_no, order_id, pay_way, source, shift, remark, status, operator, update_dt, create_dt, channel)\
                         VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                val = (181724839, '', '测试储值', '1020数据全', 100.00, giftTypeId, giftId, userId, storeId, '1', storeId,
                    'wehotel内部测试（下单无效', '1539099',str_now , '1', 1, 'A', '会员通PC购买礼包', 1, 'test', datetime_strftime(t),
                    datetime_strftime(t), 2)
                try:
                    req = self.cursor.execute(sql, val)  # sql提交,组合字段和数据
                    self.conn.commit()  # 确认提交
                except Exception as e:
                    print(e)
                i += 1
        print('sell_record表插入数据完成，共计%d条' % loopcount)
        self.conn.close()  # 关闭链接

if __name__ == '__main__':
    db = sell_data_maker('wepoint_test')
    db.sell_record( loopcount=1, giftId=9901113, t=-1, userId=50002818,giftTypeId='7559',storeId='5353')