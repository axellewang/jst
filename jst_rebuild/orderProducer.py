#coding:utf-8
import datetime
import json

from kafka import KafkaProducer


class orderProducer:
    def __init__(self,host,topic):
        self.host = host
        self.topic = topic



    def producer(self,orderCode,mebId):
        p = KafkaProducer(bootstrap_servers = [self.host])
        now = datetime.datetime.now()
        formattime = datetime.datetime.strftime(now, '%Y-%m-%d %H:%M:%S')
        data = json.dumps({
        "orderCode": orderCode,
        "orderState": 4,
        "sendTime": formattime,
        "innId": "JJ1090",
        "innName": "锦江都城齐程标准酒店",
        "sourceType": 501,
        "payState": 0,
        "payType": 0,
        "roomTypeId": "DD",
        "roomTypeName": "商务房A",
        "rateCode": "WHCOR1",
        "origArrDate": "2020-02-27 00:00:00",
        "origDepDate": "2019-10-19 12:00:00",
        "arrDate": "2020-03-11 00:00:00",
        "depDate": "2020-03-12 00:00:00",
        "roomOrigRate": 95.0,
        "roomTotalRate": 95.0,
        "roomPayRate": 95.0,
        "backCash": 0,
        "pointAmout": None,
        "giftAmout": 0,
        "payAmout": 500.0,
        "payOrderNo": None,
        "payChannel": None,
        "dayLength": 1,
        "roomQty": 1,
        "sellerId": 309488,
        "createTime": "2019-10-24 19:23:03",
        "roomSourceType": "7days",
        "externalId": None,
        "currency": "CNY",
        "brandId": "JJINN",
        "lstGuests": [
            {
                "name": "入住人",
                "mobile": "18964719947",
                "email": "1658426364@qq.com"
            }
        ],
        "gOrderNo": None,
        "gOrderAmout": None,
        "fineAmout": None,
        "gxwxDistRule": None,
        "updateTime": formattime,
        "lstCoupons": None,
        "businessMebId": 200045171,
        "itemIds": None,
        "saleType": 1,
        "refundedAmount": None,
        "accountItems": None,
        "bkMebId": mebId,
        "channelSourceType": 501,
        "refundAccountItems": None,
        "businessExt": None
    })
        p.send(self.topic,value=data.encode('utf-8'))
        p.flush()

if __name__ =='__main__':
    producer = orderProducer('172.25.33.84:9092','tpOrderBalanceInfo.test')
    producer.producer(orderCode='101004084173',mebId=181824103)




