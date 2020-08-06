from database import mysqlunit
import mongounit
import pprint

class verify_legal:
    def __init__(self):
        self.item_order_info = None
    def find_one(self, filter_dict):
        try:
            self.item_order_info = testunit.mongo.collection.find_one(filter_dict)
            pprint.pprint(self.item_order_info)
        except Exception as e:
            print('查询数据失败:%s' % e)
        finally:
            return self.item_order_info

    def is_leagl(self):
        hotel_info = testunit.mysql.hotel_config()
        print(hotel_info)
        i = 0
        while i < len(hotel_info):
            billtype = hotel_info[i].get('bill_type')
            print(billtype)
            i +=1





if __name__ =='__main':
    testunit = verify_legal()
    testunit.mongo = mongounit.Mongounit('mongodb://root:root123456@172.25.32.144:40001/')
    testunit.mysql = mysqlunit.MysqlUnit()
    testunit.mongo.change_collection(table='item_order')
  #  testunit.find_one(filter_dict={'guid':1212})
    testunit.is_leagl()
