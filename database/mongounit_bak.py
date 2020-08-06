from pymongo import MongoClient
from config import read_config

#coding:utf-8
linstr = 'mongodb://root:root123456@172.25.32.144:40001/'
MongoHost,MongoPort,MongoUser,MongoPassowrd,Mongodb,MongoTable =\
'172.25.32.144',40001,'root','root123456','jst_order_service_test','gift_order'

class Mongounit:
    def __init__(self,host=MongoHost,port=MongoPort,db=Mongodb):
        try:
            self.client = None
            self.client = MongoClient(host,port)
            self.database = self.client.get_database(db)
            self.collection = None
        except  Exception as e:
            self.close_conn()
            print('链接数据库失败:%s' % e)

    def change_collection(self,table=MongoTable):
        self.collection = self.database.get_collection(table)
        print('当前表:%s' % table)

    def count_info(self,table=MongoTable,filter_dict=None):
        table_size = 0
        try:
            self.collection =self.database.get_collection(table)
            table_size = self.collection.count(filter_dict)
          #  print(table_size)
            return table_size
        except Exception as e:
            print('获取页面失败:%s'% e)
        finally:
            return table_size


    def find_one(self,filter_dict):
        result = {}
        try:
            result = self.collection.find_one(filter_dict)
                #    pprint.pprint(reslut)
                #   self.uid = reslut.__id
                #    print(self.uid)

        except Exception as e:
                print('查询数据失败:%s' % e)
        finally:
                return result


    def delete_info(self,filter_dict):
        result = False
        try:
            self.collection.remove(filter_dict)
            result = True
            print('删除%s成功'% filter_dict)
        except Exception as e:
            print('删除失败:%s' % e)
        finally:
            return result

    def find_item_code(self,filter_dict):
        result = []
        try:
            for i in self.collection.find(filter_dict):
                result.append(i)
        except Exception as e:
            print('查询失败:%s' % e)
        finally:
           # print(result)
            return result


    def close_conn(self):
        if self.client:
            self.client.close()



if __name__ == '__main__':
    test_mongo = Mongounit('mongodb://root:root123456@172.25.32.144:40001/')
    test_mongo.change_collection(table='item_order')
   # test_mongo.count_info(table="gift_order",filter_dict={"giftType":4154})
    #test_mongo.find_one(filter_dict={"orderCode":"102544504053"})
   # test_mongo.delete_info(filter_dict={'weHotelCode':'1000060'})
  #  test_mongo.find_item_code(filter_dict={'weHotelCode':'1000060'})
