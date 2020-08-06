#coding:utf-8
import mongounit
import json
import requests
import pprint
import datetime
from datetime import date,time

class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj,date):
            return obj.strftime("%Y-%m-%d")
        else:
            return json.JSONEncoder.default(self, obj)

class post_item:
    def __init__(self):
        self.list = {}
        self.json_data = {}
        self.listA = []
        self.listB = []
        self.all_list = []

    #查询mongo中数据
    def find_one(self, filter_dict):
        try:
            self.list = unit.database.collection.find_one(filter_dict)
         #   pprint.pprint(self.list)
        except Exception as e:
            print('查询数据失败:%s' % e)
        finally:
            return self.list

    #查询出账报文中所需key对应values的方法
    def item_info(self):
        #定义所需的key
        self.listA = ['_id','guid','transId','endOfDay','accDate','transDate','itemId'
                ,'itemName','amount','category','folioId','folioSellerId','folioType','folioState','arrDate'
                ,'depDate','sourceType','createTime','updateTime','weHotelCode','orderCode']
        countnum = 0
        #根据key值循环遍历出所有对应的values
        try:
            for a in self.listA:
                    ListAvalue = self.listA[countnum]
            #        print(ListAvalue)
                    list_value = self.list.get(ListAvalue)
                    self.listB.append(list_value)
                    countnum +=1
         #   pprint.pprint(self.listB)
        except Exception as e:
            print('获取Value失败:%s' % e)


    #输出json报文的方法
    def transjson(self):
        i = 0
        lenth = len(self.listA)
        #将报文所需的key和values组合成一个dict
        while i < lenth:
            dict = {self.listA[i]:self.listB[i]}
            self.json_data.update(dict)
            i +=1
        if self.json_data.get('orderCode') is None :
            self.json_data.pop('orderCode')
        else:
            pass
        self.json_data['_uid'] = self.json_data.pop('_id')#修改dict中_id的key名称
        #修改dict中时间values值的时区
        self.json_data.update({'endOfDay': self.json_data.get('endOfDay')+datetime.timedelta(hours=8)})
        self.json_data.update({'accDate': self.json_data.get('accDate')+datetime.timedelta(hours=8)})
        self.json_data.update({'arrDate':self.json_data.get('arrDate')+datetime.timedelta(hours=8)})
        self.json_data.update({'depDate': self.json_data.get('depDate')+datetime.timedelta(hours=8)})
        self.json_data.update({'transDate': self.json_data.get('transDate')+datetime.timedelta(hours=8)})
     #   self.json_data['_uid'] = '1212'
     #   print(self.json_data)
        return self.json_data

    #接口请求方法
    def request(self,url):
        data = json.dumps(self.json_data,ensure_ascii=False,indent=2,cls=DateEncoder).encode('utf-8')
        print(json.loads(data))
        header = {'Content-Type':'application/json','orderBillType':'ITEM'}
        res = requests.post(url=url,headers=header,data=data)
        print(res.text)
        return res




if __name__ == '__main__':
    unit = post_item()
    mongo = mongounit.Mongounit('mongodb://root:root123456@172.25.32.144:40001/')
    unit.database = mongo
    unit.database.change_collection(table='item_order')
    unit.find_one(filter_dict={"guid":58624335757312000})
    unit.item_info()
    unit.transjson()
    unit.request('http://172.25.33.1:30547/bill/generateBillOrder')

