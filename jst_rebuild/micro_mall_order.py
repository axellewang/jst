import datetime
import json

import requests

from jst_rebuild import Parameters


#-*-coding:utf-8 -*-

class ComplexEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d 00:00:00')
        elif isinstance(obj, datetime.date):
            return obj.strftime('%Y-%m-%d')
        else:
            return json.JSONEncoder.default(self, obj)

class micro_order():
    def requests(self):
        url = 'http://172.25.33.1:30559/shop/pushOptionShopOrder'
       # header = {'orderCategory':'MICRO_OFFICIAL_WEBSITE_SHOP'}
        data = json.dumps({
            '''
                "uid": set_config.getUid(),
                "guid": set_config.getGuid(),
                "weHotelCode": set_config.getWeHotelCode(),
                "hotelName": set_config.getHotelName(),
                "orderCode": set_config.getOrderCode(),
                "amount": set_config.getAmount(),
                "payType": set_config.getPayType(),
                "payTime": set_config.getPayTime(),
                "payStatus": set_config.getPayStatus(),
                "memberId": set_config.getMemberId(),
                "createTime": set_config.getCreateTime(),
                "terminateState": set_config.getTerminateState(),
                "reward":set_config.getReward()
                '''
            "orderCode":"O1589351001750442021",
            "weHotelCode":"JJ1090"
            },cls=ComplexEncoder)
      #  print(data)
       # transdata = json.loads(data)
       # pprint.pprint(transdata)
        try:
            res = requests.post(url=url,data=data)
            print('微官网商品单出账请求成功,订单号:%s' %set_config.getOrderCode())
            print(res.text)
        except Exception as e:
            print('出账失败:%s' %e)


if __name__ == '__main__':
    set_config = Parameters.Parameters()
    set_config.getMicroData(filter_dict={'orderCode':'O1589351001750442021'})
    m_order = micro_order()
    m_order.requests()