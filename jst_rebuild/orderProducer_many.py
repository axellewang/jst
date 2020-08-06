#coding:utf-8
import datetime
import json

from kafka import KafkaProducer

from common_script import xlsx_operator


class orderProducer:
    def __init__(self,host,topic):
        self.host = host
        self.topic = topic



    def producer(self):
        p = KafkaProducer(bootstrap_servers = [self.host])
        now = datetime.datetime.now()
        formattime = datetime.datetime.strftime(now, '%Y-%m-%d %H:%M:%S')
        order = opt.get_data()
        countNum = 0
        for i in order :
            data = json.dumps({
            "orderCode": str(i),
            "orderState": 5,
            "sendTime": formattime,
            "innId": "2121",
            "innName": "锦江都城齐程标准酒店",
            "sourceType": 105,
            "payState": 0,
            "payType": 0,
            "roomTypeId": "DD",
            "roomTypeName": "商务房A",
            "rateCode": "WHCOR1",
            "origArrDate": "2019-10-18 12:00:00",
            "origDepDate": "2019-10-19 12:00:00",
            "arrDate": "2019-10-23 00:00:00",
            "depDate": "2019-10-24 00:00:00",
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
            "roomSourceType": "JinJiang",
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
            "bkMebId": 181293087,
            "channelSourceType": 105,
            "refundAccountItems": None,
            "businessExt": None
        })
            p.send(self.topic,value=data.encode('utf-8'))
            countNum +=1
            p.flush()
        print("推送完成,共计%d条"%countNum)

if __name__ =='__main__':
    producer = orderProducer('172.25.33.84:9092','tpOrderBalanceInfo.test')
    opt = xlsx_operator.Operator('D:\orderfile.xlsx')
    producer.producer()




