from pymongo import MongoClient
from config import read_config
import pprint

#coding:utf-8

class Mongounit:
    def conn(self,dbname):
        readConfid = read_config.getconfig(dbname=dbname)
        try:
            self.clinet = None
            if len(readConfid) <5:
                self.clinet = MongoClient(
                    'mongodb://{host}:{port}/'.format(host=readConfid[0],port=readConfid[1]))
            else:
                self.clinet = MongoClient('mongodb://{username}:{password}@{host}:{port}/'.format(username=readConfid[3],password=readConfid[4],host=readConfid[0],port=readConfid[1]))
            self.database = self.clinet.get_database(readConfid[2])
            print('链接数据库成功%s'%dbname)
            self.collection = None
            return self.database,self.collection
        except  Exception as e:
            print('链接数据库失败:%s' % e)

    def change_collection(self,table):
        self.collection = self.database.get_collection(table)
     #   print('当前表:%s' % self.collection)
        return self.collection

    def count_info(self,table,filter_dict=None):
        table_size = 0
        try:
            print('开始查询')
            targetTable = Mongounit.change_collection(self,table=table)
            print('当前表%s' % targetTable)
            table_size = targetTable.count(filter_dict)
            print(table_size)
            return table_size
        except Exception as e:
            print('获取页面失败:%s'% e)
        finally:
            return table_size


    def find_one(self,filter_dict):
        result = {}
        try:
            result = self.collection.find_one(filter_dict)
        #    print(result)
           # for doc in result:
             # print(doc)
                #   self.uid = reslut.__id
                #    print(self.uid)

        except Exception as e:
                print('查询数据失败:%s' % e)
        finally:
                return result

    def find(self):
        result = {}
        try:
            results = self.collection.find({}, {'guid': 1}).sort([('guid', -1)]).limit(1)
            #    print(result)
            # for doc in result:
            # print(doc)
            #   self.uid = reslut.__id
            #    print(self.uid)
            result.update(results)
            print(result)

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





if __name__ == '__main__':
    test_mongo = Mongounit()
    test_mongo.conn(dbname='jst_order_service_test')
  #  test_mongo.change_collection(table='micro_official_website_shop')
  #  test_mongo.count_info(table="order",filter_dict={"weHotelCode":"JJ66027"})
   # test_mongo.find()
   # test_mongo.delete_info(filter_dict={'weHotelCode':'1000060'})
  #  test_mongo.find_item_code(filter_dict={'weHotelCode':'1000060'})
