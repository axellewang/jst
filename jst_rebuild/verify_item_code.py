import mongounit

from database import mysqlunit


class Verify_item_code:
    #这是查询item_order表中所有直销/分销记账科目的房单号的方法
    def verify_item(self):
        mysqlitem =  test.mysql.itemSourceType() #调用mysqlunit的查询直销/分销/线下记账科目方法
        ##调用mongounit查询记账科目表数据
        test.mongo.change_collection('item_order')
        result = test.mongo.find_item_code(filter_dict={'weHotelCode':'1000060'})
        count = 0
        #将查询出的记账科目表数据,查询itemId是否在对应渠道中,根据结果范围folioId
        while count < len(result):
            a = result[count]
            folioId = a.get('folioId')
            itemid = a.get('itemId')
            if str(itemid) in mysqlitem:
                print('folioId:%d' % folioId,'itemId %d'% itemid)
            else:
                pass
            count += 1



if __name__ == '__main__':
    test = Verify_item_code()
    test.mysql = mysqlunit.MysqlUnit()
    test.mongo = mongounit.Mongounit('mongodb://root:root123456@172.25.32.144:40001/')
    test.verify_item()
