import requests
from common_script.xlsx_operator import Operator
import json

class order_task:
    def push_item_order(self,hotelCode,orderCode,folioId,transId):
        url = 'http://172.25.33.1:30559/itemOrder/pushOptionItemOrder'
        header = {"Content-Type":"application/json"}
        data = json.dumps({"weHotelCode": hotelCode,
                "folioId": transId,
                "transId": folioId,
                "orderCode": orderCode,
                "terminateState": 0,
                "ifPage": False})
        req = requests.post(url=url,headers= header,data=data)

      #  print(data)

    def push_folio(self,folio,hotelCode):
        url = 'http://172.25.33.1:30559/folioOrder/pushOptionalFolioOrder'
        header = {"Content-Type":"application/json"}
        data =json.dumps( {"terminateState":0,
                "weHotelCode":hotelCode,
                "folioId":folio,
                "ifPage":False})
        req = requests.post(url=url, headers=header, data=data)

    def push_order(self,hotelCode,orderCode):
        url = 'http://172.25.33.1:30559/order/pushOptionOrder'
        header = {"Content-Type": "application/json"}
        data = json.dumps({"terminateState": 0,
                "weHotelCode": hotelCode,
                "orderCode": orderCode,
                "ifPage": False})
        req = requests.post(url=url,headers=header,data=data)

    def push_gift(self,hotelCode,giftId):
        url = 'http://172.25.33.1:30559/gift/pushOptionGiftOrder'
        header = {"Content-Type": "application/json"}
        data = json.dumps({"page": 0,
                "size": 10,
                "weHotelCode": hotelCode,
                "giftId":giftId,
                "terminateState": 0
                })
        req = requests.post(url=url,headers=header,data=data)

    def push_micromall(self,hotelCode,orderCode):
        url = 'http://172.25.33.1:30559/shop/pushOptionShopOrder'
        header = {"Content-Type": "application/json"}
        data = json.dumps({"weHotelCode":hotelCode,
                           "orderCode":orderCode,
                           "terminateState":0})
        req = requests.post(url=url, headers=header, data=data)

    def push_WhFeeOrder(self, hotelCode):
        url = 'http://172.25.33.1:30559/whFeeOrder/pushOptionWhFeeOrder'
        header = {"Content-Type": "application/json"}
        data = json.dumps({"weHotelCode": hotelCode,
                           "terminateState": 0})
        print(data)
        req = requests.post(url=url, headers=header, data=data)
        print(req.text)

    def push_scoreOrder(self,hotelCode):
        url = 'http://172.25.33.1:30559/score_patch/pushBatchScoreOrderByReq'
        header = {"Content-Type": "application/json"}
        data = json.dumps({
              "terminateStates": [0],
               "weHotelCodes": [hotelCode]
            })
        req = requests.post(url=url, headers=header, data=data)
        print(req.text)
if __name__ == '__main__':
    t = order_task()
   # t.push_item_order(hotelCode='5353',orderCode='211469921011',folioId='211469921',transId="211469922")
   # t.push_micromall(hotelCode='JJ69876',orderCode='182024351012')
  #  t.push_order(hotelCode='5353',orderCode='212320531011')
    #t.push_WhFeeOrder(hotelCode='5353')
    t.push_scoreOrder(hotelCode='5353')